import pandas as pd
from sklearn.preprocessing import normalize


def encode_labels(df: pd.DataFrame) -> pd.DataFrame:
    df['Пол'] = df['Пол'].apply(
        lambda x: 1 if x == 'М' else 0
    )
    df['Нуждается в общежитии'] = df['Нуждается в общежитии'].apply(
        lambda x: 1 if x == 'да' else 0
    )
    return df


def normalize_data(df: pd.DataFrame) -> pd.DataFrame:
    return normalize(df)
