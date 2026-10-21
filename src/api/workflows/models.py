from sqlmodel import Field, Session, SQLModel, create_engine, select


class Workflow(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True)