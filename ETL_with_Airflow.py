# import the libraries
from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash_operator import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago

#defining DAG arguments
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'ice jdk',
    'start_date': days_ago(0),
    'email': ['josaphakamdem@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
dag=DAG(
    dag_id='ETL_toll_data',
    default_args=default_args,
    description='Apache Airflow Final Assignment',
    schedule_interval=timedelta(1),
)
#task creation unzip data
unzip_data=BashOperator(
    task_id='unzip_data',
    bash_command="/home/project/airflow/dags/unzip_data.sh",
    dag=dag,
) 

#task extract_data_from_csv 
extract_data_from_csv=BashOperator(
    task_id='extract_data_from_csv',
    bash_command="/home/project/airflow/dags/extract_data_from_csv.sh",
    dag=dag,
) 
#task extract_data_from_tsv 
extract_data_from_tsv=BashOperator(
    task_id='extract_data_from_tsv',
    bash_command="/home/project/airflow/dags/extract_data_from_tsv.sh",
    dag=dag,
) 
#task extract_data_from_txt 
extract_data_from_fixed_width=BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command="/home/project/airflow/dags/extract_data_from_fixed_width.sh",
    dag=dag,
) 
#task consolidate data
consolidate_data=BashOperator(
    task_id='consolidate_data',
    bash_command="/home/project/airflow/dags/consolidate.sh",
    dag=dag,
) 
#task consolidate data
transform_data=BashOperator(
    task_id='transform_data',
    bash_command="/home/project/airflow/dags/transform_data.sh",
    dag=dag,
) 
# task pipeline
unzip_data
extract_data_from_csv
extract_data_from_tsv
extract_data_from_fixed_width
consolidate_data
transform_data