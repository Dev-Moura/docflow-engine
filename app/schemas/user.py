from uuid import UUID
from datetime import datetime


from pydantic import BaseModel, ConfigDict, EmailStr

class UserCreate(BaseModel):
    nome : str
    email : EmailStr
    password : str

class UserResponse(BaseModel):
    id : UUID
    nome : str
    email : EmailStr
    created_at : datetime

    model_config = ConfigDict(
        from_attributes=True
    )