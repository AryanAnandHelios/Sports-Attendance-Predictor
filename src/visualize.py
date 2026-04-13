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