from fastapi import FastAPI
from contextlib import asynccontextmanager


from api.workflows.endpoints import init as init_workflows
from api.database import create_db_and_tables, init_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Initializing database and creating tables...")
    init_database()
    create_db_and_tables()
    yield
    pass


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

init_workflows(app)
