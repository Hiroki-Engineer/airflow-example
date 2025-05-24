# Airlow

init-airflow:
    # AIRFLOW_UID
    # https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#setting-the-right-airflow-user
    # AIRFLOW__API_AUTH__JWT_SECRET
    # This is the temporary solution
    # https://github.com/apache/airflow/issues/49646#issuecomment-2827640289
    echo "AIRFLOW_UID=$(id -u)" > .env
    echo "AIRFLOW__API_AUTH__JWT_SECRET='$(openssl rand -base64 16)'" >> .env

up-airflow:
    docker compose up

down-airflow:
    docker compose down

# Python

check:
    uv run ruff check
    uv run ruff format --diff
    uv run pyright

fix:
    uv run ruff check --fix
    uv run ruff format
