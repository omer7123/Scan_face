from pydantic import BaseModel


class Answers(BaseModel):
    id: str
    right: bool
    title: str

    class Config:
        orm_mode = True

