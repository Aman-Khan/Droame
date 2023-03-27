from typing import Optional
from pydantic import BaseModel, EmailStr

class Operator_Login(BaseModel):
    operator_id: str

class Response_Login(BaseModel):
    token: str
    class Config:
        orm_mode=True

class TokenData(BaseModel):
    operator_id: str
    class Config:
        orm_mode=True
    
class Register_Customer(BaseModel):
    operator_id: str
    customer_id: str
    customer_name: str
    customer_email: EmailStr
    phone_number: str
    country_code: Optional[str] = 91


class Response_Register_Customer(BaseModel):
    operator_id: str
    customer_name: str
    customer_email: EmailStr
    phone_number: str
    country_code: str

    class Config:
        orm_mode = True

# class Operator_SignUp(BaseModel):    
#     operator_id: str
#     password: str

# class Response_Operator_SignUp(BaseModel):
#     operator_id: str
#     message = 'registered'
#     class Config:
#         orm_mode=True
