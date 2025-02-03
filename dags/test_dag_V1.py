from datetime import datetime
from airflow import DAG
from airflow.operators.dummy import DummyOperator

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 1),  # Set an appropriate start date
    'retries': 1,
}

# Define the DAG
with DAG(
    dag_id='test_dag',
    default_args=default_args,
    description='A simple test DAG',
    schedule_interval='@daily',  # Run the DAG once a day
    catchup=False,  # Do not perform backfill for past dates
) as dag:
    
    # Define tasks
    start_task = DummyOperator(
        task_id='start'
    )
    
    end_task = DummyOperator(
        task_id='end'
    )
    
    # Set task dependencies: start_task runs before end_task
    start_task >> end_task
