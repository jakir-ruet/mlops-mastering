import pandas as pd
import json

df = pd.read_csv("data-collection.csv")

# 1. Remove duplicates
df = df.drop_duplicates()

# 2. Handle missing values

df['age'] = df['age'].fillna(df['age'].median())
df['salary'] = df['salary'].fillna(df['salary'].mean())
df['department'] = df['department'].fillna(df['department'].mode()[0])
df['bonus'] = df['bonus'].fillna(0)

df['hire_date'] = pd.to_datetime(df['hire_date'], errors='coerce')
df['hire_date'] = df['hire_date'].fillna(pd.Timestamp("2000-01-01"))

# 3. Parse JSON profile column
def parse_profile(x):
    if pd.isna(x):
        return pd.Series([None, None, None])
    try:
        p = json.loads(x)
        return pd.Series([
            p.get("address"),
            p.get("phone"),
            p.get("email")
        ])
    except:
        return pd.Series([None, None, None])

df[['address', 'phone', 'email']] = df['profile'].apply(parse_profile)

# Drop original profile column
df = df.drop(columns=['profile'])

# 4. Feature Engineering

# Address length
df['address_length'] = df['address'].apply(lambda x: len(str(x)) if pd.notnull(x) else 0)

# Salary category (Low, Medium, High)
bins = [0, 50000, 70000, float("inf")]
labels = ['Low', 'Medium', 'High']

df['salary_category'] = pd.cut(
    df['salary'],
    bins=bins,
    labels=labels
)

# 5. Fix data types
df['age'] = df['age'].astype(int)
df['salary'] = df['salary'].astype(float)

# 6. Save cleaned + engineered data
df.to_csv("clean-data.csv", index=False)

print("✅ Data cleaning + feature engineering completed!")
