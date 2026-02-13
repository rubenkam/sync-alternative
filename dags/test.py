from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="single_echo_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,  # trigger manually
    catchup=False,
    tags=["example"],
) as dag:

    echo_task = BashOperator(
        task_id="echo_hello",
        bash_command='echo "Hello from Airflow!"'
    )

    echo_task