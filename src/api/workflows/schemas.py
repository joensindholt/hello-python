from pydantic import BaseModel

class CreateWorkflowCommand(BaseModel):
    title: str


class CreateWorkflowResponse(BaseModel):
    title: str


class ListWorkflowsResponse(BaseModel):
    workflows: list[ListWorkflowResponse] = []

class ListWorkflowResponse(BaseModel):
    title: str