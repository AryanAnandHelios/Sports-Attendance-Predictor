import pandas as pd
import numpy as np
from src.stadium_capacity import get_capacity

def load_data(matches_path, cups_path):
    matches = pd.read_csv(matches_path, encoding='utf-8')
    cups = pd.read_csv(cups_path, encoding='utf-8')
    return matches, cups

def clean_data(matches):
    matches = matches.copy()
    
    # Drop rows where attendance is missing
    matches = matches.dropna(subset=['Attendance'])
    
    # Attendance is already numeric — just convert directly
    matches['Attendance'] = pd.to_numeric(matches['Attendance'], errors='coerce')
    matches = matches.dropna(subset=['Attendance'])
    
    # Drop duplicates
    matches = matches.drop_duplicates(subset=['MatchID'])
    
    # Year is already a column — just clean it
    matches['Year'] = pd.to_numeric(matches['Year'], errors='coerce')
    matches = matches.dropna(subset=['Year'])
    matches['Year'] = matches['Year'].astype(int)
    
    print(f"Clean dataset: {matches.shape}")
    print(f"Years: {sorted(matches['Year'].unique())}")
    print(f"Attendance range: {matches['Attendance'].min():.0f} to {matches['Attendance'].max():.0f}")
    
    return matches



def engineer_features(matches):
    matches = matches.copy()
    
    knockout_stages = ['Final', 'Semi-finals', 'Quarter-finals', 
                       'Round of 16', 'Third place']
    matches['is_knockout'] = matches['Stage'].isin(knockout_stages).astype(int)
    matches['match_number'] = matches.groupby('Year').cumcount() + 1
    matches['is_final'] = (matches['Stage'] == 'Final').astype(int)
    teams_per_year = matches.groupby('Year')['Home Team Name'].nunique()
    matches['num_teams'] = matches['Year'].map(teams_per_year)
    matches_per_year = matches.groupby('Year').size()
    matches['tournament_size'] = matches['Year'].map(matches_per_year)
    
    # Add stadium capacity
    matches['capacity'] = matches['Stadium'].apply(get_capacity)
    
    # Check match rate
    matched = matches['capacity'].notna().sum()
    total = len(matches)
    print(f"Capacity matched: {matched}/{total} ({100*matched/total:.1f}%)")
    print(f"Unmatched stadiums: {matches[matches['capacity'].isna()]['Stadium'].unique()[:10]}")

    features = ['Year', 'is_knockout', 'match_number', 
                'is_final', 'num_teams', 'tournament_size', 'capacity']
    target = 'Attendance'
    
    df = matches[features + [target]].dropna()
    print(f"Feature matrix: {df.shape}")
    
    return df, features, target