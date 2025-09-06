from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import sys

# Make sure Airflow can import your ETL modules
sys.path.insert(0, "/opt/airflow/etl")

from extract import extract_data
from transform import transform_data
from load import load_data

CSV_PATH = "/opt/airflow/mock_transactions.csv"
DB_PATH = "/opt/airflow/pipeline.db"

def run_etl():
    df_raw = extract_data(CSV_PATH)
    df_clean = transform_data(df_raw)
    load_data(df_clean, DB_PATH)

default_args = {
    "owner": "darshan",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="etl_pipeline",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",     # change to "@once" for one-off tests
    catchup=False,
    description="Simple ETL: CSV -> transform -> SQLite"
) as dag:

    etl_task = PythonOperator(
        task_id="run_etl",
        python_callable=run_etl
    )

    etl_task
