from typing import List
from datetime import datetime 
from fastapi import APIRouter, Depends, HTTPException, status
from ..database import get_db, Session
from .. import models, schemas, oauth, utils

router = APIRouter(tags=['Operator Operation'])

#register Customer
@router.post('/register', status_code=status.HTTP_201_CREATED)
def registerCustomer(cust_info: schemas.Register_Customer, db: Session = Depends(get_db), user: oauth.get_current_user = Depends()):
    if user.operator_id!=cust_info.operator_id: #vaidate operator
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='invalid credentails(opreated_id)')
    elif utils.phoneNoValidater(cust_info)==False: #validate phone number
        raise HTTPException(status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION, detail='invalid phone no')
    
    #check if customer already exists
    search_user = db.query(models.Customers).filter(models.Customers.customer_id==cust_info.customer_id).first() 
    if search_user is not None: 
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='customer id already registerd')
    
    search_user = db.query(models.Customers).filter(models.Customers.customer_email==cust_info.customer_email).first() 
    if search_user is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='email address is already registerd')
    search_user = db.query(models.Customers).filter(models.Customers.phone_number==cust_info.phone_number).first() 
    if search_user is not None: raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='phone no is already registerd')

    #commit in database
    register_cust = models.Customers(**cust_info.dict())
    db.add(register_cust)
    db.commit()
    db.refresh(register_cust)

    return register_cust

# get all customer 
@router.get('/recent/customers',response_model=List[schemas.Recent_Customer])
def registerCustomer(db: Session = Depends(get_db), user: oauth.get_current_user = Depends()):
    operator = user.operator_id
    recCust = db.query(models.Customers).filter(models.Customers.operator_id==operator).all()
    return recCust

#update customer details
@router.patch("/update/{customerId}")
def updateCustomerDetails(customerId: str, data: dict, db: Session = Depends(get_db), user: oauth.get_current_user = Depends()):
    get_customer = db.query(models.Customers).filter(models.Customers.customer_id==customerId).filter(models.Customers.operator_id==user.operator_id).first()
    
    email = data.get('customer_email')
    name = data.get('customer_name')
    phone = data.get('phone_number')
    
    if get_customer is None: #check (do customer exists in database)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="customer don't exist")
    elif name is not None: #validate name
        if len(name)<1: raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="invalid name")
        else: get_customer.customer_name = name
    elif email is not None: #validate email
        if utils.validateEmail(email)==False:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="invalid email")
        else: get_customer.customer_email = email
    elif phone is not None: #validate phone no
        phSc = schemas.PhoneNumber(phone_number=phone)
        if utils.phoneNoValidater(phSc)==False:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="invalid phone number")
        else:
            get_customer.phone_number = phSc.phone_number
            get_customer.country_code = phSc.country_code

    db.commit()
    return {'update':'success'}

#get customer details
@router.get("/customer/details", response_model=schemas.Customer_Details)
def read_item(search_option: str = None, search_value: str = None, db: Session = Depends(get_db), user: oauth.get_current_user = Depends()):
    if search_option is None or search_value is None: raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='invalid search')
    else:
        if search_option=='customer_id':
            search_cust = db.query(models.Customers).filter(models.Customers.customer_id==search_value).filter(models.Customers.operator_id==user.operator_id).first()
            if search_cust is None: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="customer don't exist")
            else: return search_cust
        elif search_option=='customer_name':
            search_cust = db.query(models.Customers).filter(models.Customers.customer_name==search_value).filter(models.Customers.operator_id==user.operator_id).first()
            if search_cust is None: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="customer don't exist")
            else: return search_cust
        elif search_option=='customer_email':
            search_cust = db.query(models.Customers).filter(models.Customers.customer_email==search_value).filter(models.Customers.operator_id==user.operator_id).first()
            if search_cust is None: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="customer don't exist")
            else: return search_cust
        else: raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='invalid option')
        
#delete customer 
@router.delete("/delete/{customerId}")
def deleteCutomer(customerId: str, db: Session = Depends(get_db), user: oauth.get_current_user = Depends()):
    get_customer = db.query(models.Customers).filter(models.Customers.customer_id==customerId).filter(models.Customers.operator_id==user.operator_id).first()
    if get_customer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='customer not found')
    else:
        db.delete(get_customer)
        db.commit()
        raise HTTPException(status_code=status.HTTP_202_ACCEPTED, detail='Posted is removed')
            
#drone booking
@router.post('/booking')
def bookDroneShot(book_info: schemas.Book_Drone_Shot, db: Session = Depends(get_db), user: oauth.get_current_user = Depends()):
    book_info.operator_id = user.operator_id

    #handel (booking time < present time)
    if book_info.booked_for_time < datetime.utcnow():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="You can't book slot in past")
    
    search_time_slot = db.query(models.Bookings).filter(models.Bookings.booked_for_time==book_info.booked_for_time).first()
    
    #handel (if Drone is already booked for booking_time) 
    if search_time_slot is not None:
        raise HTTPException(status_code=status.HTTP_226_IM_USED, detail='Time slot is not avaliable')   
    
    search_customer = db.query(models.Customers).filter(models.Customers.customer_id==book_info.customer_id).first()

    #handel (if customer don't exists)
    if search_customer is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Customer not found(register customer first)")
    
    search_drone_shot = db.query(models.DroneShots).filter(models.DroneShots.drone_shot==book_info.drone_shot).first()

    #handel (if invalid drone shot type is passed)
    if search_drone_shot is None: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="invalid drone shot type")
    
    #getting (drone_shot_id from drone_shot type database)
    book_info.drone_shot_id = search_drone_shot.drone_shot_id
    search_location = db.query(models.Locations).filter(models.Locations.location==book_info.location).first()
    
    #check (if location don't exist in location table register it)
    if search_location is None:
        location_entry = schemas.Location(location=book_info.location)
        new_location = models.Locations(**location_entry.dict())
        db.add(new_location)
        db.commit()
        db.refresh(new_location) 
    
    #loation id for booking location
    loc = db.query(models.Locations).filter(models.Locations.location==book_info.location).first()
    book_info.location_id = loc.location_id

    book_info_commit = schemas.Commit_Booking(
        operator_id=book_info.operator_id,
        customer_id=book_info.customer_id,
        booked_for_time=book_info.booked_for_time,
        location_id=book_info.location_id,
        drone_shot_id=book_info.drone_shot_id
    )

    booked = models.Bookings(**book_info_commit.dict())
    
    db.add(booked)
    db.commit()
    db.refresh(booked)

    #tranfer data to better response model
    booked_res = schemas.Booking_Response(
        booking_id=booked.booking_id,
        operator_id=booked.operator_id,
        location=book_info.location,
        drone_shot=book_info.drone_shot,
        customer_id=book_info.customer_id
    )

    return booked_res

