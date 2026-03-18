import pandas as pd

file_path = "sample.xlsx"
df = pd.read_excel(file_path)

print(df.head())