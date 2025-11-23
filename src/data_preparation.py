import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

def check_missing_values(df):
    return df.isnull().sum()

def select_features(df):
    # sélec des variables numériques pertinentes
    # on exclut CustomerID (id) et gender 
    features = df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']].copy()
    return features

def normalize_features(df):
    scaler = StandardScaler()
    normalized_df = pd.DataFrame(
        scaler.fit_transform(df),
        columns=df.columns,
        index=df.index
    )
    return normalized_df, scaler

