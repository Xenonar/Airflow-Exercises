import datetime
import logging

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Create greeting function
def greet():
    logging.info('Hello World')


dag = DAG(
        'lesson1.exercise1',
        start_date=datetime.datetime.now())

# Connect to Airflow
greet_task = PythonOperator(
   task_id="greet_task",
   python_callable=greet,
   dag=dag
)
