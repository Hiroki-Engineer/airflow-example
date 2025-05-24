# Airflow example

This is a repository for learning Airflow, created with real-world development practices in mind as much as possible.

# Required tools

| name | version | url |
| - | - | - |
| just | 1.34.0 | https://github.com/casey/just |
| docker | 27.1.1 | |

# Environment for development

Airflow environment is set up by [docker-compose.yaml](/docker-compose.yaml).<br>
This file can be get from [official page](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html).

## How to set up environment for development

1. Create .env

```sh
just create-env
```

2. Up Airflow

```sh
just up-airflow
```

3. Down Airflow

```sh
just down-airflow
```

# Caution

## This is the temporary solution

REF1: https://github.com/apache/airflow/issues/49646<br>
REF2: https://github.com/apache/airflow/issues/50538

[docker-compose.yaml](/docker-compose.yaml)
```yaml
AIRFLOW__API_AUTH__JWT_SECRET: '${AIRFLOW__API_AUTH__JWT_SECRET}'
```

[justfile](/justfile)
```sh
echo "AIRFLOW__API_AUTH__JWT_SECRET='$(openssl rand -base64 16)'" >> .env
```
