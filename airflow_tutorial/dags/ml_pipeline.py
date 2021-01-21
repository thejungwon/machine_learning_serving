#References : https://towardsdatascience.com/10-minutes-to-building-a-machine-learning-pipeline-with-apache-airflow-53cd09268977
from datetime import timedelta
from airflow import DAG

from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

from download import download
from train import train


print(1)
default_args = {
    'owner': 'Jungwon Seo',
    'depends_on_past': False,
    'start_date': days_ago(31),
    'email': ['example@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}





dag = DAG(
    'ml_pipeline',
    default_args=default_args,
    description='A simple Machine Learning pipeline',
    schedule_interval=timedelta(days=30),
)


download_images = PythonOperator(
    task_id='download',
    python_callable=download,
    dag=dag,
)
train = PythonOperator(
    task_id='train',
    depends_on_past=False,
    python_callable=train,
    retries=3,
    dag=dag,
)

serve = BashOperator(
    task_id='serve',
    depends_on_past=False,
    bash_command='touch -m ${AIRFLOW_HOME}/../serve.py  ',
    dag=dag,
)


download_images >> train >> serve


