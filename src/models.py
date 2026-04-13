import numpy as np
from sklearn.linear_model import Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def time_split(df, target, test_year=2010):
    train = df[df['Year'] < test_year]
    test = df[df['Year'] >= test_year]
    features = [c for c in df.columns if c != target]
    X_train = train[features]
    y_train = train[target]
    X_test = test[features]
    y_test = test[target]
    print(f"Train: {len(X_train)} matches ({df['Year'].min()} - {test_year-1})")
    print(f"Test: {len(X_test)} matches ({test_year} - {df['Year'].max()})")
    return X_train, X_test, y_train, y_test

def evaluate(name, model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    train_preds = model.predict(X_train)
    test_preds = model.predict(X_test)
    train_r2 = r2_score(y_train, train_preds)
    test_r2 = r2_score(y_test, test_preds)
    mae = mean_absolute_error(y_test, test_preds)
    rmse = np.sqrt(mean_squared_error(y_test, test_preds))
    print(f"{name:35} | MAE: {mae:8.0f} | RMSE: {rmse:8.0f} | Train R²: {train_r2:.3f} | Test R²: {test_r2:.3f}")
    return train_r2, test_r2, mae, rmse

def run_complexity_curves(X_train, X_test, y_train, y_test):
    results = {}

    print("\n=== RIDGE ===")
    alphas = [0.001, 1, 10, 100, 1000, 10000]
    train_r2s, test_r2s = [], []
    for alpha in alphas:
        tr, te, _, _ = evaluate(f"Ridge alpha={alpha}", Ridge(alpha=alpha),
                                X_train, X_test, y_train, y_test)
        train_r2s.append(tr)
        test_r2s.append(te)
    results['Ridge'] = {'x': alphas, 'train': train_r2s, 'test': test_r2s, 'xlabel': 'Alpha'}

    print("\n=== LASSO ===")
    train_r2s, test_r2s = [], []
    for alpha in alphas:
        tr, te, _, _ = evaluate(f"Lasso alpha={alpha}", Lasso(alpha=alpha),
                                X_train, X_test, y_train, y_test)
        train_r2s.append(tr)
        test_r2s.append(te)
    results['Lasso'] = {'x': alphas, 'train': train_r2s, 'test': test_r2s, 'xlabel': 'Alpha'}

    print("\n=== DECISION TREE ===")
    depths = [1, 2, 3, 5, 8, 10, 15, 20]
    train_r2s, test_r2s = [], []
    for depth in depths:
        tr, te, _, _ = evaluate(f"DecisionTree depth={depth}",
                                DecisionTreeRegressor(max_depth=depth, random_state=42),
                                X_train, X_test, y_train, y_test)
        train_r2s.append(tr)
        test_r2s.append(te)
    results['Decision Tree'] = {'x': depths, 'train': train_r2s, 'test': test_r2s, 'xlabel': 'Max Depth'}

    print("\n=== RANDOM FOREST ===")
    n_trees = [10, 25, 50, 100, 200, 500]
    train_r2s, test_r2s = [], []
    for n in n_trees:
        tr, te, _, _ = evaluate(f"RandomForest n={n}",
                                RandomForestRegressor(n_estimators=n, random_state=42),
                                X_train, X_test, y_train, y_test)
        train_r2s.append(tr)
        test_r2s.append(te)
    results['Random Forest'] = {'x': n_trees, 'train': train_r2s, 'test': test_r2s, 'xlabel': 'N Estimators'}

    print("\n=== XGBOOST ===")
    train_r2s, test_r2s = [], []
    for n in n_trees:
        tr, te, _, _ = evaluate(f"XGBoost n={n}",
                                XGBRegressor(n_estimators=n, random_state=42, verbosity=0),
                                X_train, X_test, y_train, y_test)
        train_r2s.append(tr)
        test_r2s.append(te)
    results['XGBoost'] = {'x': n_trees, 'train': train_r2s, 'test': test_r2s, 'xlabel': 'N Estimators'}

    return results

def get_best_results(X_train, X_test, y_train, y_test):
    best = {}

    model = Lasso(alpha=10000)
    model.fit(X_train, y_train)
    best['Lasso'] = {
        'train_r2': r2_score(y_train, model.predict(X_train)),
        'test_r2': r2_score(y_test, model.predict(X_test))
    }

    model = Ridge(alpha=10000)
    model.fit(X_train, y_train)
    best['Ridge'] = {
        'train_r2': r2_score(y_train, model.predict(X_train)),
        'test_r2': r2_score(y_test, model.predict(X_test))
    }

    model = DecisionTreeRegressor(max_depth=5, random_state=42)
    model.fit(X_train, y_train)
    best['Decision Tree'] = {
        'train_r2': r2_score(y_train, model.predict(X_train)),
        'test_r2': r2_score(y_test, model.predict(X_test))
    }

    model = RandomForestRegressor(n_estimators=500, random_state=42)
    model.fit(X_train, y_train)
    best['Random Forest'] = {
        'train_r2': r2_score(y_train, model.predict(X_train)),
        'test_r2': r2_score(y_test, model.predict(X_test))
    }

    model = XGBRegressor(n_estimators=25, random_state=42, verbosity=0)
    model.fit(X_train, y_train)
    best['XGBoost'] = {
        'train_r2': r2_score(y_train, model.predict(X_train)),
        'test_r2': r2_score(y_test, model.predict(X_test))
    }

    return best