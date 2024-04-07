이번 챕터에서는 로컬 PC에 airflow 를 설치하고 간단한 glue job 을 만들어서 등록한 후 호출하는 실습을 진행합니다.

```
% conda env list
# conda environments:
#
base                  *  /Users/soonbeom/anaconda3

% pip install apache-airflow

% airflow info

% cd airflow
(base) soonbeom@bcd07468d10a airflow % ls -la
total 152
drwxr-xr-x    4 soonbeom  staff    128  4  7 16:30 .
drwxr-x---+ 109 soonbeom  staff   3488  4  7 16:30 ..
-rw-------    1 soonbeom  staff  76164  4  7 16:30 airflow.cfg
drwxr-xr-x    3 soonbeom  staff     96  4  7 16:30 logs


```




## 참고자료 ##

* [[airflow] 맥 터미널에서 에어플로우 설치하기](https://velog.io/@jenori_dev/airflow-%EB%A7%A5-%ED%84%B0%EB%AF%B8%EB%84%90%EC%97%90%EC%84%9C-%EC%97%90%EC%96%B4%ED%94%8C%EB%A1%9C%EC%9A%B0-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0)