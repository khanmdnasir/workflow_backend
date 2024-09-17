# models/user.py

from pydantic import BaseModel, Field


class DocumentModel(BaseModel):
    nodes: str
    edges: str
    name: str
    user_id: int

    class Config:
        from_attributes = True
