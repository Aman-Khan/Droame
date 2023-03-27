from passlib import context
from . import schemas
pwd_context = context.CryptContext(schemes=['bcrypt'], deprecated='auto')

def hash(pwd):
    return pwd_context.hash(pwd)

def verify(pwd, hash_pwd):
    return pwd_context.verify(pwd, hash_pwd)

def phoneNoValidater(cust_info: schemas.Register_Customer):
    phone_no = cust_info.phone_number
    phone_no_len = len(phone_no)
    if phone_no_len<10 or phone_no_len>15: return False
    elif len(phone_no[:-10])>5: return False 
    for i in phone_no[-10:]:
        if i.isdigit()==False: return False
    country_c = ''
    for i in phone_no[:-10]:
        if i.isdigit():
            country_c+=i
    cust_info.country_code = country_c  
    cust_info.phone_number = phone_no[-10:]  
    return True
