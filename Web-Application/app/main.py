from fastapi import FastAPI, Depends
from .database import get_db, Session, text
from .router import operator, customer 
from . import schemas
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/hell')
def sayHello(db: Session = Depends(get_db)):

    print("hello")
    return {'message':'Hello'}

app.include_router(operator.router)
app.include_router(customer.router)
