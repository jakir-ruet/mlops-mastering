
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import os

DATA_PATH = "/opt/airflow/data/data.csv"
MODEL_PATH = "/opt/airflow/data/model.pkl"


# Task 1: Fetch Data
def fetch_data():
    df = pd.DataFrame({
        "x": range(100),
        "y": [0 if i < 50 else 1 for i in range(100)]
    })
    df.to_csv(DATA_PATH, index=False)
    print("Data created")


# Task 2: Preprocess
def preprocess():
    df = pd.read_csv(DATA_PATH)
    X = df[["x"]]
    y = df["y"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    os.makedirs("/opt/airflow/data/processed", exist_ok=True)
    X_train.to_csv("/opt/airflow/data/processed/X_train.csv", index=False)
    X_test.to_csv("/opt/airflow/data/processed/X_test.csv", index=False)
    y_train.to_csv("/opt/airflow/data/processed/y_train.csv", index=False)
    y_test.to_csv("/opt/airflow/data/processed/y_test.csv", index=False)

    print("Preprocessing done")


# Task 3: Train Model
def train_model():
    X_train = pd.read_csv("/opt/airflow/data/processed/X_train.csv")
    y_train = pd.read_csv("/opt/airflow/data/processed/y_train.csv")

    model = LogisticRegression()
    model.fit(X_train, y_train.values.ravel())

    joblib.dump(model, MODEL_PATH)
    print("Model trained")


# Task 4: Evaluate Model
def evaluate():
    model = joblib.load(MODEL_PATH)

    X_test = pd.read_csv("/opt/airflow/data/processed/X_test.csv")
    y_test = pd.read_csv("/opt/airflow/data/processed/y_test.csv")

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    print(f"Accuracy: {acc}")


# DAG Definition
with DAG(
    dag_id="mlops_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    t1 = PythonOperator(task_id="fetch_data", python_callable=fetch_data)
    t2 = PythonOperator(task_id="preprocess", python_callable=preprocess)
    t3 = PythonOperator(task_id="train_model", python_callable=train_model)
    t4 = PythonOperator(task_id="evaluate", python_callable=evaluate)

    t1 >> t2 >> t3 >> t4
