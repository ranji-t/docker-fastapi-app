from sqlalchemy import Engine
from sqlmodel import SQLModel
from ..tbl_model import Items_Tbl


def create_table(engine: Engine) -> None:
    """
    Create a table in the database using the provided SQLAlchemy engine.

    Args:
        engine (Engine): The SQLAlchemy engine to use for creating the table.
    """

    # Tables in Meta Data
    Items_Tbl

    # Create the table in the database using the metadata from SQLModel
    SQLModel.metadata.create_all(engine)
