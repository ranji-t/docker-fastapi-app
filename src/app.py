# Third Party Imports
from fastapi import FastAPI
from sqlmodel import Session, select

# Internal Imports
from models.pg_conn import get_engine_test  # , get_engine
from models.sql_init import create_table
from models.tbl_model import Items_Tbl


# Predifined Valirable
resources = {}


# The Lifetime
async def lifespan(app: FastAPI):
    """
    The lifespan of the application.

    Returns:
        None
    """
    # Create Engine
    resources["engine"] = get_engine_test()
    # Create Table
    create_table(resources["engine"])
    # Triggered when the application stops
    yield
    # Actions Done after Shutdown
    resources.clear()


# App Creation
app = FastAPI(
    debug=True,
    title="FastAPI with SQLModel",
    description="A simple FastAPI with SQLModel example.",
    lifespan=lifespan,
)


@app.get("/")
def read_root():
    """
    Root endpoint that returns a welcome message.

    Returns:
        dict: A dictionary containing a welcome message.
    """
    return {"message": "App Ready for your service!"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    """
    Endpoint to read an item by its ID and an optional query parameter.

    Args:
        item_id (int): The ID of the item.

    Returns:
        dict: A dictionary containing the item ID and the query parameter.
    """

    # Selecte data form table
    with Session(resources["engine"]) as session:
        statement = select(Items_Tbl).where(Items_Tbl.id == item_id)
        results = session.exec(statement).first()
        # Retuen item ID and query parameter
        if not results:
            return {"error-message": "Item not found!"}
        # If No item was found
        return results


@app.post("/items/")
def create_or_update_item(item: Items_Tbl):
    """
    Endpoint to create a new item or update an existing item.

    Args:
        item (Items_Tbl): The item to be created or updated.

    Returns:
        dict: A dictionary containing the created or updated item.
    """

    # Create or update item
    with Session(resources["engine"]) as session:
        statement = select(Items_Tbl).where(Items_Tbl.id == item.id)
        existing_item = session.exec(statement).first()

        if existing_item:
            # Update existing item
            existing_item.name = item.name
            existing_item.description = item.description
            session.add(existing_item)
        else:
            # Create new item
            session.add(item)

        session.commit()
        session.refresh(item)

    return item
