from pydantic import BaseModel

class TodoCreate(BaseModel):
    title: str
    note: str | None = None
    completed: bool = False