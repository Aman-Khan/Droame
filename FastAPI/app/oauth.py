from jose import JWTError, jwt
from .config import setting
from datetime import datetime, timedelta
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from . import schemas

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = setting.secret_key
ALGORITHM = setting.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = setting.token_expire_time

def create_access_token(data: dict):
    to_encode = data.copy()
    exp = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode['exp']=exp

    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded

def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        op_id: str = payload.get('operator_id')
        if op_id is None:
            raise credentials_exception
        token_data = schemas.TokenData(operator_id=op_id)
    except JWTError:
        raise credentials_exception
    return token_data

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='could not validate credentials')
    return verify_access_token(token, credentials_exception)