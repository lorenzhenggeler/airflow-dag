from datetime import datetime, timedelta

from airflow import DAG
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2017, 7, 13),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

company_onboarding = DAG('kube-operator',
                         default_args=default_args,
                         schedule_interval=None,catchup=False)
with company_onboarding:
    t1 = KubernetesPodOperator(namespace='airflow',
                               image="ubuntu:16.04",
                               cmds=["bash", "-cx"],
                               arguments=["echo", "hello world"],
                               labels={'runner': 'airflow'},
                               name="pod1",
                               task_id='pod1',
                               is_delete_operator_pod=True,
                               hostnetwork=False,
                               )

    company_onboarding.doc_md = __doc__

    t1