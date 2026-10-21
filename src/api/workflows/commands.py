from typing import Annotated

from fastapi.params import Depends
from sqlmodel import Session

from api.database import get_session
from api.workflows.models import Workflow
from api.workflows.schemas import CreateWorkflowCommand, CreateWorkflowResponse


def create_workflow(command: CreateWorkflowCommand, session: Session):
    workflow = Workflow(title=command.title)
    
    session.add(workflow)
    session.commit()
    session.refresh(workflow)

    response = CreateWorkflowResponse(title=workflow.title)

    return response