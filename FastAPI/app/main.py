from fastapi import FastAPI, Depends
from .database import get_db, Session, text
from . import models

app = FastAPI()

@app.get('/')
def sayHello(db: Session = Depends(get_db)):
    data = db.execute(text('SHOW DATABASES')).fetchall()
    print(data)
    return {'message':'Hello'}

