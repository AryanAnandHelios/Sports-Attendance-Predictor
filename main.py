from src.features import load_data, clean_data, engineer_features
from src.models import time_split, run_complexity_curves, get_best_results
from src.visualize import plot_complexity_curves, plot_best_models, plot_feature_importance, plot_actual_vs_predicted

matches, cups = load_data('data/WorldCupMatches.csv', 'data/WorldCups.csv')
matches = clean_data(matches)
df, features, target = engineer_features(matches)
X_train, X_test, y_train, y_test = time_split(df, target)
results = run_complexity_curves(X_train, X_test, y_train, y_test)
plot_complexity_curves(results)
best = get_best_results(X_train, X_test, y_train, y_test)
plot_best_models(best)
plot_feature_importance(X_train, y_train, features)
plot_actual_vs_predicted(X_train, X_test, y_train, y_test)