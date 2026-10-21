from typing import Annotated

from fastapi import Depends
from sqlmodel import Session

from api.database import get_session
from api.workflows.commands import create_workflow as create_workflow_command
from api.workflows.queries import list_workflows_query
from api.workflows.schemas import CreateWorkflowCommand


def init(app):
    @app.get("/workflows")
    def read_workflows(session: Annotated[Session, Depends(get_session)]):
        response = list_workflows_query(session)
        return response

    @app.post("/workflows")
    def create_workflow(command: CreateWorkflowCommand, session: Annotated[Session, Depends(get_session)]):
        response = create_workflow_command(command, session)
        return response