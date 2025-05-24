from airflow.sdk import dag, task


@dag()
def hello_world() -> None:
    print_hello_world(hello=create_hello_str(), world=create_world_str())  # type: ignore [reportArgumentType]


@task
def create_hello_str() -> str:
    return "Hello"


@task
def create_world_str() -> str:
    return "World"


@task
def print_hello_world(hello: str, world: str) -> None:
    import logging

    hello_world = f"{hello} {world}!"

    logger = logging.getLogger(__name__)
    logger.info(hello_world)


hello_world()
