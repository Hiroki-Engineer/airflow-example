create-env:
    # https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#setting-the-right-airflow-user
    echo "AIRFLOW_UID=$(id -u)" > .env
