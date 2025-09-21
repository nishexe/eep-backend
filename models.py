import os
from database import Base
from dotenv import load_dotenv
from sqlalchemy import Boolean, Column, Integer, String

load_dotenv()

AWS_RDS_MYSQL_TABLE_TestLogin = os.getenv("AWS_RDS_MYSQL_TABLE_TestLogin")

class Employee(Base):
    __tablename__ = AWS_RDS_MYSQL_TABLE_TestLogin
    employeeID = Column(Integer, primary_key=True, index = True)
    employeeName = Column(String(256))
    hashSalt = Column(String(256))
    password = Column(String(256))
