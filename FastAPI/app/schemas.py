from typing import Optional
from pydantic import BaseModel, EmailStr

class Operator_Login(BaseModel):
    operator_id: str
    
class Response_Login(BaseModel):
    token: str
    class Config:
        orm_mode=True

class Response_Operator_SignUp(BaseModel):
    operator_id: str
    message = 'registered'
    class Config:
        orm_mode=True


class Operator_SignUp(BaseModel):    
    operator_id: str
    password: str


class TokenData(BaseModel):
    opeartor_id: str
    class Config:
        orm_mode=True
    