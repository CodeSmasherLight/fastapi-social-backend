from fastapi import FastAPI, Body, Response, status, HTTPException, Depends
from pydantic import BaseModel
from random import randrange
import psycopg
from psycopg.rows import dict_row
import time
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, get_db
from .routers import post, user, auth


models.Base.metadata.create_all(bind=engine)


app = FastAPI()

get_db()


while True:
    try:
        conn = psycopg.connect(host="localhost", dbname="fastapi", user="postgres", 
                                password="****", row_factory=dict_row)
        cursor = conn.cursor()
        print("Database connected successfully!!")
        break
    except Exception as error:
        print("Database connection failed!!")
        print("Error: ", error)  
        time.sleep(2)



# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
#             {"title": "classes", "content": "This is class 1", "id": 2}]


# def find_post(id):
#     for post in my_posts:
#         if post['id'] == id:
#             return post

# find the index in the array that has required id         
# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i        

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

# for Post model
@app.get("/")
def read_root():
    return {"Hello": "World"}
