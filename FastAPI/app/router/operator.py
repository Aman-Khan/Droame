from fastapi import APIRouter, Depends, HTTPException, status
from ..database import get_db, Session
from .. import models, schemas, utils, oauth

router = APIRouter(tags=['Operator'])

@router.post('/login', response_model=schemas.Response_Login,status_code=status.HTTP_201_CREATED)
def login(op_cred: schemas.Operator_Login , db: Session = Depends(get_db)):
    search_user = db.query(models.Operators).filter(models.Operators.operator_id==op_cred.operator_id).first() 
    if search_user is None: #checking if operator already exists
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='invalid credentials')
    else:
        data  = {'operator_id':op_cred.operator_id}
        jwt_token = oauth.create_access_token(data)
        return schemas.Response_Login(token=jwt_token)









@router.post('/signup', response_model=schemas.Response_Operator_SignUp,status_code=status.HTTP_201_CREATED)
def signUp(op_cred: schemas.Operator_SignUp, db: Session = Depends(get_db)):
    
    search_user = db.query(models.Operators).filter(models.Operators.operator_id==op_cred.operator_id).first() 
    
    if search_user is None: #checking if operator already exists
        #hashing password using bcrypt
        unhash_password = op_cred.password 
        hash_password = utils.hash(unhash_password)
        op_cred.password = hash_password
        
        register = models.Operators(**op_cred.dict())
        db.add(register)
        db.commit()
        db.refresh(register)
        return register
    else: raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='user already exists') 

# @router.post('/signin', status_code=status.HTTP_201_CREATED)
# def logIn(op_cred: schemas.Operator_SignUp, db: Session = Depends(get_db)):
#     search_user = db.query(models.Operators).filter(models.Operators.operator_id==op_cred.operator_id).first() 

#     if search_user is None or not utils.verify(op_cred.password, search_user.password): 
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='invalid credentials')
#     else:
#         data  = {'operator_id':op_cred.operator_id}
#         jwt_token = oauth.create_access_token(data)
#         return {'token':jwt_token}