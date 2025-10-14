from fastapi import FastAPI, Body, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange
import psycopg
from psycopg.rows import dict_row
import time


app = FastAPI()

# schema for Post
class Post(BaseModel):
    title: str
    content: str
    published: bool = True


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



my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "classes", "content": "This is class 1", "id": 2}]


def find_post(id):
    for post in my_posts:
        if post['id'] == id:
            return post

# find the index in the array that has required id         
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i        

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/posts")
def get_posts():
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    return {"data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute("INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *", 
                   (post.title, post.content, post.published ))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}

# # for demonstration purposes only to shpw that it works from top to bottom
# @app.get("/posts/latest")
# def get_last_post():
#     return my_posts[-1]

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    print(post)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id: {id} was not found"}
    return {"post_detail": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)

    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)

    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    
    post_dict = post.model_dump()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"data": post_dict}