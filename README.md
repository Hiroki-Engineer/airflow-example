# Tools

| name | version | url |
| - | - | - |
| just | 1.34.0 | https://github.com/casey/just |
| docker | 27.1.1 | |

# Environment

Airflow environment is set up by [docker-compose.yaml](/docker-compose.yaml).
This file can be get from [official page](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html).

## How to set up

1. Create .env

`just create-env`

2. Start Airflow

`docker compose up`
