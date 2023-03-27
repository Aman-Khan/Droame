from fastapi import APIRouter, Depends
from ..database import get_db, Session
from .. import models, schemas

router = APIRouter(tags=['Customer'])

# @router.post('/{}/register')
# def registerCustomer(db: Session = Depends(get_db))