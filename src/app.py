# Third Party Imports
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine

# App Creation
app = FastAPI()


@app.get("/")
def read_root():
    """
    Root endpoint that returns a welcome message.

    Returns:
        dict: A dictionary containing a welcome message.
    """
    return {"message": "Hello, World!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    """
    Endpoint to read an item by its ID and an optional query parameter.

    Args:
        item_id (int): The ID of the item.
        q (str, optional): An optional query parameter. Defaults to None.

    Returns:
        dict: A dictionary containing the item ID and the query parameter.
    """
    # Get engine
    engine = get_engine()
    # Retuen item ID and query parameter
    return {"item_id": item_id, "q": q}


def get_engine() -> Engine:
    """
    Function to create a SQLAlchemy engine.

    Returns:
        sqlalchemy.engine.base.Engine: A SQLAlchemy engine.
    """
    # Create a database engine using SQLAlchemy and psycopg2
    engine = create_engine(
        "postgresql+psycopg2://postgres:mysecretpassword@postgres_db/example"
    )
    # Return Eingine
    return engine
