import pandas as pd

# 1. Load the data
df = pd.read_csv("mock_data.csv")

# 2. Print top rows
print("\n=== Top 5 Rows ===")
print(df.head())

# 3. DataFrame info
print("\n=== DataFrame Info ===")
df.info()

# 4. Total missing values
print("\n=== Missing Values ===")
print(df.isnull().sum())

# 5. Statistical summary
print("\n=== Statistical Summary ===")
print(df.describe())

# 6. Unique values in 'department'
print("\n=== Unique Departments ===")
print(df["department"].unique())
