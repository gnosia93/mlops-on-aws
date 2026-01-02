from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# 1. DAG 인스턴스 정의 (스케줄링 및 기본 설정)
with DAG(
    dag_id='hello_airflow', # DAG의 고유 ID
    start_date=datetime(2025, 1, 1), # DAG가 처음 실행될 날짜
    schedule_interval='@daily', # 매일 실행되도록 설정
    catchup=False, # start_date와 현재 날짜 사이의 누락된 DAG 실행을 건너뜀
    tags=['simple', 'hello'] # DAG를 분류하기 위한 태그 (선택 사항)
) as dag:

    # 작업을 수행할 Python 함수 정의
    def print_hello():
        print("Hello Airflow!")
        return "Hello Airflow finished successfully."

    # 2. Operator(작업) 정의
    # PythonOperator를 사용하여 위에서 정의한 함수를 실행
    hello_task = PythonOperator(
        task_id='say_hello', # 작업의 고유 ID
        python_callable=print_hello, # 실행할 Python 함수 이름
    )

    # 3. 작업 순서 설정 (이 예시에서는 작업이 하나뿐이므로 순서는 단순함)
    # hello_task는 단독 작업
