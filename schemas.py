from pydantic import BaseModel, field_validator

# User schemas
class UserCreate(BaseModel):
    username: str
    password: str

    @field_validator('password')
    def password_length(cls, v):
        if len(v) > 72:
            raise ValueError('Password must be 72 characters or less')
        if len(v) < 6:
            raise ValueError('Password must be at least 6 characters')
        return v

class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True

# Token schema
class Token(BaseModel):
    access_token: str
    token_type: str

# Note schemas
class NoteCreate(BaseModel):
    text: str

class NoteResponse(BaseModel):
    id: int
    text: str
    owner_id: int

    class Config:
        from_attributes = True