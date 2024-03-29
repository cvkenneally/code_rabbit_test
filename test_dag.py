from airflow import DAG
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator
from datetime import datetime, timedelta 

dag_owner = 'cvkenneally'

default_args = {'owner': dag_owner,
        'depends_on_past': False,
        'retries': 2,
        'retry_delay': timedelta(minutes=5)
        }

with DAG(dag_id='test_dag',
        default_args=default_args,
        description='This is a test DAG',
        start_date=datetime(2021, 1, 1),
        schedule_interval=None,
        catchup=False,
        tags=['test']
):

    start = EmptyOperator(task_id='start')

    @task
    def task_1():
        return 'Task 1 complete.'

    end = EmptyOperator(task_id='end')

    start >> task_1() >> end