from pydantic import BaseModel

class NoteCreate(BaseModel):
    text: str

class NoteResponse(BaseModel):
    id: int
    text: str

    class Config:
        from_attributes = True