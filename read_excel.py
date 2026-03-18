import pandas as pd

file_path = "sample.xlsx"

excel_file = pd.ExcelFile(file_path)
df = pd.read_excel(excel_file,sheet_name="FY25_결과", header=1)

print("===head===")
print(df.head())
print("\n===columns===")
print(df.columns)
print("\n===info===")
print(df.info())