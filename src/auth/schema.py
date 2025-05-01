from pydantic import BaseModel, Field
from typing import Optional
import uuid

class User(BaseModel):
    uid: uuid.UUID
    user_name: str
    first_name: str
    last_name: str
    is_verified: bool = False
    email: str
    password_hash:str = Field(exclude=True)

    class Config:
        orm_mode = True

class CreateUser(BaseModel):
    user_name: str
    first_name: str
    last_name: str
    email: str
    password: str

    class Config:
        orm_mode = True

class UpdateUser(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    is_verified: Optional[bool] = None

    class Config:
        orm_mode = True

class SignIn(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True