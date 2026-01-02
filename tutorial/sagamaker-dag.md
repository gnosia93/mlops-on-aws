* 목표 : 이번 챕터에서는 llama-3-8b 분산 훈련 스크립트를 KubernetesPodOperator 를 하나 만들어서 실행하도록 한다. 


### airflow-sa 에 Pod 관리 권한 부여 ### 
```
cat <<EOF | kubectl apply -f -
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: airflow
  name: airflow-pod-manager-role
rules:
- apiGroups: [""]
  resources: ["pods", "pods/log", "pods/exec"]
  verbs: ["get", "list", "watch", "create", "patch", "update", "delete"]
- apiGroups: [""]
  resources: ["events"]
  verbs: ["list", "watch"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: airflow-pod-manager-binding
  namespace: airflow
subjects:
- kind: ServiceAccount
  name: airflow-sa
  namespace: airflow
roleRef:
  kind: Role
  name: airflow-pod-manager-role
  apiGroup: rbac.authorization.k8s.io
EOF
```





---

## TODO : LLM 파이프라인 개발 워크플로우 ##
* 코드 수정: 로컬 IDE에서 DAG 파일(예: llm_finetune_dag.py)을 작성합니다.
* Git Push: git push origin main으로 코드를 올립니다.
* 자동 반영: EKS에 떠 있는 Airflow Git-Sync 컨테이너가 60초 이내에 새 코드를 감지하여 웹 UI에 표시합니다.
* 학습 실행: DAG가 실행되면 KubernetesPodOperator가 GPU 노드에 학습용 Pod를 띄워 파인튜닝을 시작합니다.



* https://yann.lecun.com/exdb/mnist/ 


## 참고자료 ##

* https://aws.amazon.com/ko/blogs/korea/build-end-to-end-machine-learning-workflows-with-amazon-sagemaker-and-apache-airflow/
* https://github.com/aws-samples/sagemaker-ml-workflow-with-apache-airflow/blob/master/src/dag_ml_pipeline_amazon_video_reviews.py
* [Amazon Web Services Connection](https://airflow.apache.org/docs/apache-airflow-providers-amazon/3.4.0/connections/aws.html#authenticating-to-aws)
