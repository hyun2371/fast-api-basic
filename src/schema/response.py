from typing import List
from pydantic import BaseModel

class ToDoSchema(BaseModel): # todoResponse
    id: int
    contents: str
    is_done: bool

    class Config: # ORM 객체 -> Pydantic DTO
        orm_mode = True

class ToDoListSchema(BaseModel): # todoListResponse
    todos: List[ToDoSchema]