# mlops-on-aws

In this workshop, we're going to go through how to build machine learing pipeline with apache airflow and MLflow.  
Airflow can be located in anywhere among your laptop, EKS cluster, EC2 and MWAA(Managed Workflows for Apache Airflow), here we use an airflow on your laptop.  


![](https://github.com/gnosia93/mlops-on-aws/blob/main/images/mlops-on-aws.png)


### Prerequisite ###

* _[Install apache airflow on your PC first](https://github.com/gnosia93/mlops-on-aws/blob/main/tutorial/airflow-on-pc.md)_
* _Provision EKS Cluster_


### Tutorial ###
1. [call sagemaker Dag](https://github.com/gnosia93/mlops-on-aws/blob/main/tutorial/sagamaker-dag.md)











    


## ,, ##

* workshop spec
  - Airflow Orchestration
      - PC located airflow, not cloud
      - communication with boto3 api 
  - 전처리 : Glue / Spark
  - ML training / parameter tunning / Interference -> sagemaker.
  - not embrace feature store (on/offline)
  - bucket structure is broze / silver / gold
    - delta lake / iceberg with parquet
  - no visualization support such as quicksight, tableau
  - pytorch for ml
  - pypark for sparkml & dataframe - de
  - CI/CD
      - github / github action.
      - code commit / copepipeline
  - MLflow ?? --> experiment / model 저장.
  - Spark structured streaming support with kafka ? 
* Infra : VPC, S3, EC2, Glue or EMR Spark
* Dataset : Giga byte 이상의 데이터타 셋 확보 필요.. (Regression or Classification 용)
* Storage : HDFS(EMR), S3
* Monitoring : cloudwatch X -> prometheus & grafana O
