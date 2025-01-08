from sqlalchemy import Engine
from sqlmodel import create_engine


def get_engine() -> Engine:
    """
    Function to create a SQLAlchemy engine.

    Returns:
        sqlalchemy.engine.base.Engine: A SQLAlchemy engine.
    """
    # Create a database engine using SQLAlchemy and psycopg2
    engine = create_engine(
        "postgresql+psycopg2://postgres:mysecretpassword@postgres_db:5432/example"
    )
    # Return Eingine
    return engine


def get_engine_test() -> Engine:
    """
    Function to create a SQLAlchemy engine.

    Returns:
        sqlalchemy.engine.base.Engine: A SQLAlchemy engine.
    """
    # Create a database engine using SQLAlchemy and psycopg2
    engine = create_engine(
        "postgresql+psycopg2://postgres:mysecretpassword@localhost:5433/example"
    )
    # Return Eingine
    return engine
