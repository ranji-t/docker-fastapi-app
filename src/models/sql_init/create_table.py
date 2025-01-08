from sqlalchemy import Engine
from sqlmodel import SQLModel, Field


def create_table(engine: Engine) -> None:
    """
    Create a table in the database using the provided SQLAlchemy engine.

    Args:
        engine (Engine): The SQLAlchemy engine to use for creating the table.
    """

    # Define a table model using SQLModel
    class itmes_tbl(SQLModel, table=True):
        """
        SQLModel class representing the items table.

        Attributes:
            id (int): The primary key of the table.
            name (str): The name of the item.
            description (str): The description of the item.
            price (float): The price of the item.
        """

        id: int = Field(primary_key=True)
        name: str = Field(nullable=True)
        description: str = Field(nullable=True)
        price: float = Field(nullable=False)

    # Create the table in the database using the metadata from SQLModel
    SQLModel.metadata.create_all(engine)
