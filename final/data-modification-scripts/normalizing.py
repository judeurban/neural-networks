from pandas import DataFrame, read_csv
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Load your data
translated_df = pd.read_csv("translated.df.csv")

numerical_columns = translated_df.columns[1:-1]

# Normalize the numerical data columns using StandardScaler
scaler = StandardScaler()
translated_df[numerical_columns] = scaler.fit_transform(translated_df[numerical_columns])

translated_df.drop(columns='Unnamed: 0', inplace=True)
translated_df.to_csv("translated-normalized-df.csv", index=False)
