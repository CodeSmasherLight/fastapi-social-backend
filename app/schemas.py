from pydantic import BaseModel, EmailStr
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

# post
class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    owner_id: int
    owner: 'UserOutput'
    # created_at: datetime
    pass

# user
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOutput(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        from_attributes = True

# authentication
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: int | None = None