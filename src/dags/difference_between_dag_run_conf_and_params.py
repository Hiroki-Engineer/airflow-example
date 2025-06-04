from datetime import UTC, datetime, timedelta

from airflow.sdk import Param, dag, task

"""
REF: https://github.com/apache/airflow/discussions/37181

scheduled
params: 5
conf: None

manual without input
params: 5
conf: 5

manual with 4
params: 4
conf: 4
"""


@dag(
    start_date=datetime.now(UTC) + timedelta(days=-1),  # yesterday
    schedule="* * * * *",
    params={"hoge": Param(5, type="integer")},
)
def difference_between_dag_run_conf_and_params() -> None:
    task1()


@task
def task1(**context) -> None:
    import logging

    logger = logging.getLogger(__name__)
    logger.info(f"params: {context['params']['hoge']}")
    logger.info(f"conf: {context['dag_run'].conf.get('hoge', None)}")


difference_between_dag_run_conf_and_params()
