from sqlmodel import Session, select

from api.workflows.models import Workflow
from api.workflows.schemas import ListWorkflowResponse, ListWorkflowsResponse


def list_workflows_query(session: Session) -> ListWorkflowsResponse:
    workflows = session.exec(select(Workflow)).all()
    return ListWorkflowsResponse(
        workflows=[ListWorkflowResponse(title=workflow.title) for workflow in workflows]
    )
