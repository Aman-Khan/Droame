from .database import Base, engine
from sqlalchemy import Column, INTEGER, VARCHAR, ForeignKey, TIMESTAMP, text

class Operators(Base):
    __tablename__  = 'operators'
    operator_id    = Column(VARCHAR(100), primary_key=True, nullable=False)
    password       = Column(VARCHAR(100), nullable=False)

class Customers(Base):
    __tablename__  = 'customers'
    customer_id    = Column(VARCHAR(100), primary_key=True, nullable=False)
    operator_id    = Column(VARCHAR(100), ForeignKey('operators.operator_id', ondelete='CASCADE'), nullable=False)
    customer_name  = Column(VARCHAR(100), nullable=False)
    customer_email = Column(VARCHAR(100), unique=True, nullable=False)
    phone_number   = Column(VARCHAR(10), unique=True, nullable=False)
    country_code   = Column(VARCHAR(3), nullable=False)

class Locations(Base):
    __tablename__  = 'locations'
    location_id    = Column(INTEGER, primary_key=True, nullable=False)
    location       = Column(VARCHAR(100), unique=True, nullable=False)

class DroneShots(Base):
    __tablename__  = 'drone_shots'
    drone_shot_id  = Column(INTEGER, primary_key=True, nullable=False)
    drone_shot     = Column(VARCHAR(100), unique=True, nullable=False)

class Bookings(Base):
    __tablename__  = 'bookings'

    booking_id     = Column(INTEGER, primary_key=True, autoincrement=True, nullable=False)
    customer_id    = Column(VARCHAR(100), ForeignKey('customers.operator_id', ondelete='CASCADE'))
    location_id    = Column(INTEGER, ForeignKey('locations.location_id'), nullable=False)
    drone_shot_id  = Column(INTEGER, ForeignKey('drone_shots.drone_shot_id'), nullable=False)
    created_time   = Column(TIMESTAMP, server_default=text('NOW()'), nullable=False)

Base.metadata.create_all(bind=engine)