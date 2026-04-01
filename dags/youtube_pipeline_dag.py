from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import logging

from youtube_extract import fetch_trending_videos
from youtube_transform import transform_videos
from youtube_load import create_table, load_to_postgres

logger = logging.getLogger(__name__)


def extract_task(**context):
    logger.info("Starting extract task")
    data = fetch_trending_videos()
    context['ti'].xcom_push(key='raw_data', value=data)
    logger.info(f"Extracted {len(data)} raw videos")


def transform_task(**context):
    logger.info("Starting transform task")
    raw = context['ti'].xcom_pull(key='raw_data')
    clean = transform_videos(raw)
    context['ti'].xcom_push(key='clean_data', value=clean)
    logger.info(f"Transformed {len(clean)} clean videos")


def load_task(**context):
    logger.info("Starting load task")
    clean = context['ti'].xcom_pull(key='clean_data')
    create_table() 
    load_to_postgres(clean)
    logger.info("Load task completed")


with DAG(
    dag_id='youtube_pipeline',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    extract = PythonOperator(
        task_id='extract',
        python_callable=extract_task
    )

    transform = PythonOperator(
        task_id='transform',
        python_callable=transform_task
    )

    load = PythonOperator(
        task_id='load',
        python_callable=load_task
    )

    extract >> transform >> load