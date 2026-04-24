import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

df = pd.read_csv("clean-data.csv")

# 1. Feature Engineering

# Extract year from hire_date
df['hire_year'] = pd.to_datetime(df['hire_date']).dt.year

# Drop non-useful columns
df = df.drop(columns=['id', 'name', 'hire_date', 'address', 'phone', 'email'])

# 2. Define features
num_features = ['age', 'salary', 'bonus', 'hire_year']
cat_features = ['department']

# 3. Preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), num_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_features)
    ]
)

pipeline = Pipeline([
    ('preprocessing', preprocessor)
])

# Transform data
X = pipeline.fit_transform(df)

print("Transformed shape:", X.shape)
