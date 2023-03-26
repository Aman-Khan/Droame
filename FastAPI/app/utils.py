from passlib import context
pwd_context = context.CryptContext(schemes=['bcrypt'], deprecated='auto')

def hash(pwd):
    return pwd_context.hash(pwd)

def verify(pwd, hash_pwd):
    return pwd_context.verify(pwd, hash_pwd)

