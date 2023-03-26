from typing import Optional
from pydantic import BaseModel, EmailStr

class Response_Operator_SignUp(BaseModel):
    operator_id: str
    message = 'registered'
    class Config:
        orm_mode=True


class Operator_SignUp(BaseModel):    
    operator_id: str
    password: str

    class Config:
        orm_mode=True

