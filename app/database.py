from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import psycopg
from psycopg.rows import dict_row
import time
from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql+psycopg://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# while True:
#     try:
#         conn = psycopg.connect(host="settings.database_hostname", dbname="settings.database_name", user="settings.database_username", 
#                                 password="settings.database_password", row_factory=dict_row)
#         cursor = conn.cursor()
#         print("Database connected successfully!!")
#         break
#     except Exception as error:
#         print("Database connection failed!!")
#         print("Error: ", error)  
#         time.sleep(2)        