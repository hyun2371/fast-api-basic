from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import declarative_base

from schema.request import CreateToDoRequest

Base = declarative_base()


class ToDo(Base):  # Base를 상속 받음
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    contents = Column(String(256), nullable=False)
    is_done = Column(Boolean, nullable=False)

    def __repr__(self):  # 오버라이딩
        return f"ToDo(id={self.id}, content={self.contents}, is_done={self.is_done})"

    @classmethod
    def create(cls, request: CreateToDoRequest) ->  "ToDo": # pydantic -> ORM
        return cls(
            contents=request.contents,
            is_done=request.is_done,
        )

    def done(self):
        self.is_done = True
        return self

    def undone(self):
        self.is_done = False
        return self
