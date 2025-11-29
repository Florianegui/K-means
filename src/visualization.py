import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def plot_distributions(df):
# permet fe tracer les histogrammes de distribution des variables.
    fig, axes = plt.subplots(1, len(df.columns), figsize=(15, 4))
    for i, col in enumerate(df.columns):
        axes[i].hist(df[col], bins=20, edgecolor='black')
        axes[i].set_title(f'Distribution de {col}')
        axes[i].set_xlabel(col)
        axes[i].set_ylabel('Fréquence')
    plt.tight_layout()
    plt.show()

def plot_correlation_heatmap(df):
#permet de tracer la heatmap de corrélation    
    
    plt.figure(figsize=(10, 8))
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0,
                square=True, linewidths=1, cbar_kws={"shrink": 0.8})
    plt.title('Matrice de corrélation')
    plt.tight_layout()
    plt.show()

def plot_pairplot(df, hue=None):
#permet de trace un pairplot des variables
  
    sns.pairplot(df, hue=hue, diag_kind='hist', plot_kws={'alpha': 0.6})
    plt.suptitle('Pairplot des variables', y=1.02)
    plt.show()

def plot_clusters_2d(df, labels, x_col, y_col):
# permet de visualiser les clusters en 2D
    
    plt.figure(figsize=(10, 8))
    scatter = plt.scatter(df[x_col], df[y_col], c=labels, cmap='viridis', 
                         alpha=0.6, s=50, edgecolors='black', linewidth=0.5)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f'Clusters K-Means : {x_col} vs {y_col}')
    plt.colorbar(scatter, label='Cluster')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def plot_clusters_3d(df, labels, x_col, y_col, z_col):
    
# permet fe visualiser les clusters en 3D

    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    scatter = ax.scatter(df[x_col], df[y_col], df[z_col], 
                        c=labels, cmap='viridis', s=50, alpha=0.6,
                        edgecolors='black', linewidth=0.5)
    
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_zlabel(z_col)
    ax.set_title('Clusters K-Means en 3D')
    plt.colorbar(scatter, label='Cluster', ax=ax)
    plt.tight_layout()
    plt.show()

def plot_cluster_profiles(df, cluster_col='Cluster'):

# permet de trace les profils moyens de chaque cluster
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    numeric_cols = [col for col in numeric_cols if col != cluster_col]
    
    cluster_means = df.groupby(cluster_col)[numeric_cols].mean()
    
    fig, axes = plt.subplots(1, len(numeric_cols), figsize=(15, 5))
    for i, col in enumerate(numeric_cols):
        cluster_means[col].plot(kind='bar', ax=axes[i], color='steelblue', edgecolor='black')
        axes[i].set_title(f'Moyenne de {col} par cluster')
        axes[i].set_xlabel('Cluster')
        axes[i].set_ylabel('Moyenne')
        axes[i].tick_params(axis='x', rotation=0)
        axes[i].grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.show()

