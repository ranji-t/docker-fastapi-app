from sqlmodel import SQLModel, Field


# Define a table model using SQLModel
class Items_Tbl(SQLModel, table=True):
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
