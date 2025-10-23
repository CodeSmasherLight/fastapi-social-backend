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