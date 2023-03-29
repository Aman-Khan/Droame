from datetime import datetime 
from typing import Optional
from pydantic import BaseModel, EmailStr

class Booking_Response(BaseModel):
    booking_id: int
    operator_id: str
    location: str
    drone_shot: str
    customer_id: str

    class Config:
        orm_mode=True

class Commit_Booking(BaseModel):
    booking_id: Optional[int]
    operator_id: str
    customer_id: str
    booked_for_time: datetime 
    drone_shot_id: int
    location_id: int


class Location(BaseModel):
    location: str
    location_id: Optional[int]

class Book_Drone_Shot(BaseModel):
    customer_id: str
    booked_for_time: datetime 
    location: str
    drone_shot: str

    drone_shot_id: Optional[int]
    operator_id: Optional[str]
    location_id: Optional[int]

class PhoneNumber(BaseModel):
    phone_number: str
    country_code: Optional[str] = 91

class UserEmail(BaseModel):
    email: EmailStr

class Customer_Details(BaseModel):
    customer_id: str
    customer_name: str
    customer_email: EmailStr
    phone_number: str
    country_code: Optional[str] = 91
    class Config:
        orm_mode=True

class Recent_Customer(BaseModel):
    customer_id: str
    customer_name: str
    class Config:
        orm_mode=True
        
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

class Operator_SignUp(BaseModel):    
    operator_id: str
    password: str

class Response_Operator_SignUp(BaseModel):
    operator_id: str
    message = 'registered'
    class Config:
        orm_mode=True
