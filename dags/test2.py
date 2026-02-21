from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
# Trigger
with DAG(
    dag_id="second_echo_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,  # trigger manually
    catchup=False,
    tags=["example"],
) as dag:

    echo_task = BashOperator(
        task_id="echo_hello",
        bash_command='echo "new release"'
    )

    echo_task