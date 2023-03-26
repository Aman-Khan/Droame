from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import DatabaseError
from .config import setting

SQLALCHEMY_DATABASE_URL = f'mysql+mysqlconnector://{setting.database_user}:{setting.database_pwd}@{setting.database_host}:{setting.database_port}/{setting.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

