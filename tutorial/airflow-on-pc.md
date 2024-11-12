![](https://github.com/gnosia93/airflow-on-aws/blob/main/images/airflow-logo.png)

로컬 PC 에 aws cli 및 credentials 설정이 완료되었다고 가정한다. 만약 그렇지 않은 경우 [config 및 credentials](https://docs.aws.amazon.com/ko_kr/cli/latest/userguide/cli-configure-files.html) 참고하여 aws cli 를 먼저 설정한다.

## 에어플로우 설치 ##
아래의 명령어를 이용하여 PC에 airflow 를 설치합니다.

```
% pip install apache-airflow

% airflow info

% cd airflow
% ls -la
total 152
drwxr-xr-x    4 soonbeom  staff    128  4  7 16:30 .
drwxr-x---+ 109 soonbeom  staff   3488  4  7 16:30 ..
-rw-------    1 soonbeom  staff  76164  4  7 16:30 airflow.cfg
drwxr-xr-x    3 soonbeom  staff     96  4  7 16:30 logs

% mkdir dags

% airflow users create \
          --username admin \
          --firstname admin \
          --lastname admin \
          --role Admin \
          --email admin@example.org

% airflow db init

% airflow scheduler &
 
% airflow webserver -p 8080 &
[2024-04-07T17:43:28.831+0900] {configuration.py:2066} INFO - Creating new FAB webserver config file in: /Users/soonbeom/airflow/webserver_config.py
  ____________       _____________
 ____    |__( )_________  __/__  /________      __
____  /| |_  /__  ___/_  /_ __  /_  __ \_ | /| / /
___  ___ |  / _  /   _  __/ _  / / /_/ /_ |/ |/ /
 _/_/  |_/_/  /_/    /_/    /_/  \____/____/|__/
Running the Gunicorn Server with:
Workers: 4 sync
Host: 0.0.0.0:8080
Timeout: 120
Logfiles: - -
Access Logformat:
```

* 로컬 pc 에서 8080 포트로 접속한다.
  
![](https://github.com/gnosia93/airflow-on-aws/blob/main/images/airflow-1.png)

* admin 유저 생성시 설정한 패스워드를 이용하여 로그인 한다. 

![](https://github.com/gnosia93/airflow-on-aws/blob/main/images/airflow-2.png)


## aws 프로바이더 설치 ##
* https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/index.html
```
% pip install apache-airflow-providers-amazon

% pip list | grep boto
aiobotocore                              2.5.0
boto3                                    1.34.79
botocore                                 1.34.79

% aws s3 ls
...
2023-04-05 20:54:20 glue-seoul-20230405
2023-05-02 09:04:14 glue-sfdc-analysis
2023-04-04 15:07:25 glue-sink-20230404
2023-02-28 09:20:34 iceberg-bcd07468d10a-2023-02-28

```


## 트러블 슈팅 ##

* aiobotocore 2.5.0 requires botocore<1.29.77,>=1.29.76, but you have botocore 1.34.79 which is incompatible
```
% python -m pip uninstall boto3 botocore
% python3 -m pip install boto3
```

## 레퍼런스 ##
* [Amazon Web Services Connection](https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/connections/aws.html)
* https://stackoverflow.com/questions/41805265/how-to-run-a-simple-airflow-dag
