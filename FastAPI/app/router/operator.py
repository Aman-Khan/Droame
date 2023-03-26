from fastapi import APIRouter, Depends, HTTPException, status
from ..database import get_db, Session
from .. import models, schemas, utils

router = APIRouter(tags=['Operator'])

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

