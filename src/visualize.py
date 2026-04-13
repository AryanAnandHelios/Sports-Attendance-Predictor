import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

def plot_complexity_curves(results):
    fig = plt.figure(figsize=(18, 12))
    fig.suptitle('Model Complexity vs. Generalization\nFIFA World Cup Attendance Prediction', 
                 fontsize=16, fontweight='bold', y=0.98)
    
    gs = gridspec.GridSpec(2, 3, hspace=0.4, wspace=0.3)
    
    axes = [fig.add_subplot(gs[0,0]), fig.add_subplot(gs[0,1]), fig.add_subplot(gs[0,2]),
            fig.add_subplot(gs[1,0]), fig.add_subplot(gs[1,1])]
    
    benchmark = 0.633
    
    for ax, (model_name, data) in zip(axes, results.items()):
        x_vals = data['x']
        train_r2 = data['train']
        test_r2 = data['test']
        x_label = data['xlabel']
        
        ax.plot(range(len(x_vals)), train_r2, 'b-o', label='Train R²', linewidth=2)
        ax.plot(range(len(x_vals)), test_r2, 'r-o', label='Test R²', linewidth=2)
        ax.axhline(y=benchmark, color='green', linestyle='--', 
                   linewidth=1.5, label=f'Benchmark R²={benchmark}')
        
        ax.set_xticks(range(len(x_vals)))
        ax.set_xticklabels([str(x) for x in x_vals], rotation=45, fontsize=9)
        ax.set_xlabel(x_label, fontsize=11)
        ax.set_ylabel('R²', fontsize=11)
        ax.set_title(model_name, fontsize=13, fontweight='bold')
        ax.legend(fontsize=9)
        ax.set_ylim(-0.5, 1.05)
        ax.grid(True, alpha=0.3)
        ax.axhline(y=0, color='black', linewidth=0.5)
    
    # Hide the empty 6th subplot
    fig.add_subplot(gs[1,2]).set_visible(False)
    
    plt.savefig('results/complexity_curves.png', dpi=150, bbox_inches='tight')
    print("Saved: results/complexity_curves.png")
    plt.show()

def plot_best_models(best_results):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    models = list(best_results.keys())
    test_r2 = [best_results[m]['test_r2'] for m in models]
    train_r2 = [best_results[m]['train_r2'] for m in models]
    
    x = np.arange(len(models))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, train_r2, width, label='Train R²', color='steelblue')
    bars2 = ax.bar(x + width/2, test_r2, width, label='Test R²', color='tomato')
    ax.axhline(y=0.633, color='green', linestyle='--', 
               linewidth=2, label='Benchmark (Al-Buenain et al. 2024)')
    
    ax.set_xlabel('Model', fontsize=12)
    ax.set_ylabel('R²', fontsize=12)
    ax.set_title('Best Configuration per Model Family\nTrain vs. Test R²', 
                 fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(models, fontsize=11)
    ax.legend(fontsize=10)
    ax.set_ylim(0, 1.05)
    ax.grid(True, alpha=0.3, axis='y')
    
    for bar in bars1:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
                f'{bar.get_height():.3f}', ha='center', va='bottom', fontsize=9)
    for bar in bars2:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
                f'{bar.get_height():.3f}', ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    plt.savefig('results/best_models.png', dpi=150, bbox_inches='tight')
    print("Saved: results/best_models.png")
    plt.show()

def plot_feature_importance(X_train, y_train, feature_names):
    from sklearn.linear_model import Lasso
    import matplotlib.pyplot as plt
    
    model = Lasso(alpha=10000)
    model.fit(X_train, y_train)
    
    coefficients = model.coef_
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    colors = ['tomato' if c < 0 else 'steelblue' for c in coefficients]
    bars = ax.barh(feature_names, coefficients, color=colors)
    
    ax.axvline(x=0, color='black', linewidth=0.8)
    ax.set_xlabel('Coefficient Value', fontsize=12)
    ax.set_title('Lasso Feature Coefficients (alpha=10000)\nNon-zero = Feature Selected by Lasso', 
                 fontsize=13, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='x')
    
    for bar, coef in zip(bars, coefficients):
        if coef != 0:
            ax.text(coef + (0.001 * max(abs(coefficients))), 
                   bar.get_y() + bar.get_height()/2,
                   f'{coef:.1f}', va='center', fontsize=9)
    
    plt.tight_layout()
    plt.savefig('results/feature_importance.png', dpi=150, bbox_inches='tight')
    print("Saved: results/feature_importance.png")
    plt.show()

def plot_actual_vs_predicted(X_train, X_test, y_train, y_test):
    from sklearn.linear_model import Lasso
    import matplotlib.pyplot as plt
    import numpy as np
    
    model = Lasso(alpha=10000)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    
    fig, ax = plt.subplots(figsize=(8, 8))
    
    ax.scatter(y_test, preds, alpha=0.6, color='steelblue', edgecolors='white', s=60)
    
    min_val = min(y_test.min(), preds.min())
    max_val = max(y_test.max(), preds.max())
    ax.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, label='Perfect Prediction')
    
    from sklearn.metrics import r2_score, mean_absolute_error
    r2 = r2_score(y_test, preds)
    mae = mean_absolute_error(y_test, preds)
    
    ax.text(0.05, 0.95, f'R² = {r2:.3f}\nMAE = {mae:.0f}',
            transform=ax.transAxes, fontsize=12,
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    ax.set_xlabel('Actual Attendance', fontsize=12)
    ax.set_ylabel('Predicted Attendance', fontsize=12)
    ax.set_title('Actual vs. Predicted Attendance\nBest Model: Lasso (alpha=10000)', 
                 fontsize=13, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('results/actual_vs_predicted.png', dpi=150, bbox_inches='tight')
    print("Saved: results/actual_vs_predicted.png")
    plt.show()