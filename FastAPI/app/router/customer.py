from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from ..database import get_db, Session
from .. import models, schemas, oauth, utils

router = APIRouter(tags=['Customer'])

@router.post('/register', status_code=status.HTTP_201_CREATED)
def registerCustomer(cust_info: schemas.Register_Customer, db: Session = Depends(get_db), user: oauth.get_current_user = Depends()):
    if user.operator_id!=cust_info.operator_id: raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='invalid credentails(opreated_id)')
    elif utils.phoneNoValidater(cust_info)==False: raise HTTPException(status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION, detail='invalid phone no')
    
    search_user = db.query(models.Customers).filter(models.Customers.customer_id==cust_info.customer_id).first() 
    if search_user is not None: raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='customer id already registerd')
    search_user = db.query(models.Customers).filter(models.Customers.customer_email==cust_info.customer_email).first() 
    if search_user is not None: raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='email address is already registerd')
    search_user = db.query(models.Customers).filter(models.Customers.phone_number==cust_info.phone_number).first() 
    if search_user is not None: raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='phone no is already registerd')

    register_cust = models.Customers(**cust_info.dict())
    db.add(register_cust)
    db.commit()
    db.refresh(register_cust)
    return register_cust

@router.get('/recent/customers',response_model=List[schemas.Recent_Customer])
def registerCustomer(db: Session = Depends(get_db), user: oauth.get_current_user = Depends()):
    operator = user.operator_id
    recCust = db.query(models.Customers).filter(models.Customers.operator_id==operator).limit(10).all()
    return recCust