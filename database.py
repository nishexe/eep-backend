import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

AWS_RDS_MYSQL_DB = os.getenv("AWS_RDS_MYSQL_DB")
AWS_RDS_MYSQL_USER = os.getenv("AWS_RDS_MYSQL_USER")
AWS_RDS_MYSQL_PASS = os.getenv("AWS_RDS_MYSQL_PASS")
AWS_RDS_MYSQL_ENDPOINT = os.getenv("AWS_RDS_MYSQL_ENDPOINT")

DATABASE_URL = f"mysql+pymysql://{AWS_RDS_MYSQL_USER}:{AWS_RDS_MYSQL_PASS}@{AWS_RDS_MYSQL_ENDPOINT}/{AWS_RDS_MYSQL_DB}"
# print(DATABASE_URL)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

