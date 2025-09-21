import models
from typing import Annotated
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import engine,SessionLocal
from fastapi import FastAPI, Depends,HTTPException, status

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class Employee(BaseModel):
    employeeID : int
    employeeName : str
    hashSalt : str
    password : str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/getAll")
async def getAll(db:db_dependency):
    msg = db.query(models.Employee).all()
    return {"message": msg}

@app.post("/addEmployee")
async def addEmployee(emp: Employee, db:db_dependency):
    #do something
    employee = models.Employee(**emp.model_dump())
    # print(employee.employeeID)
    try:
        db.add(employee)
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{e}")
    return {"Employee Added with ID": emp.employeeID}