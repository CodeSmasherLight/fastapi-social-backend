# FastAPI Social Backend

A RESTful API backend for a social media platform(generic) built with Fastapi and Postgresql

## Live Link

**API Documentation:** https://fastapi-social-backend.onrender.com/docs (will be invalid in first week of dec 2025 as project is temporary hosted on render's free tier)

The API is deployed on Render, visit the link above to explore and interact with all available endpoints through the Swagger UI.

## Features

- Create Users 
- User authentication & authorization with JWT tokens
- CRUD operations for posts
- Voting/like system for posts
- Query parameters for pagination and search
- Owner based authorization for posts

## Why I Built This

I created this project with a specific goal in mind: to show how you can build a solid backend API from the ground up, one step at a time. Instead of dumping everything into a few massive commits, i broke down the entire process into small, logical steps.

### What's Special About This Repo

The real value here is in the commit history. Each commit represents one clear step - whether that's setting up the database, adding authentication or implementing the voting system. You can literally go through the commits and see exactly how the project evolved from a basic api endpoints to a full featured social media backend.

This approach makes it perfect for:
- Learning Fastapi without getting overwhelmed
- Understanding how different backend pieces connect together
- Seeing real patterns for auth, database design and testing
- Having a reference when you are building your own projects

### How You Can Use This

Clone it, mess around with the code and most importantly, check out the commit history. You can jump to any commit to see what the project looked like at that stage. Want to see just the basic CRUD operations before auth was added? There is a commit for that. Curious about how i integrated Alembic? Thats its own step too.

Feel free to rebuild it yourself by following along commit by commit, thats honestly the best way to learn.

## Tech Stack

- **FastAPI** - Python web framework for building APIs
- **PostgreSQL** - Relational database
- **Psycopg3** - PostgreSQL adapter 
- **Pydantic** - Data validation using Python type hints
- **SQLAlchemy** - ORM for database interactions
- **Alembic** - Database migrations
- **JWT** - Token based authentication

## API Endpoints

- `POST /users` - Create a new user
- `POST /login` - User authentication
- `GET /users/{id}` - Get specific user details
- `GET /posts` - Get all posts (with pagination & search)
- `POST /posts` - Create a new post
- `GET /posts/{id}` - Get a specific post
- `PUT /posts/{id}` - Update a post
- `DELETE /posts/{id}` - Delete a post
- `POST /vote` - Vote on a post

## This is how i built this project step by step, you can check git commit history for better understanding:

- [x] Set up basic FastAPI application
- [x] Connect PostgreSQL database
- [x] Implement basic CRUD operations
- [x] Complete database migration for all endpoints
- [x] Integrate SQLAlchemy ORM
- [x] Implement user authentication & authorization
- [x] Add voting/like system
- [x] Add Alembic for database migrations
- [x] Deploy to production (Render)
- [x] Add comprehensive tests
- [x] Set up GitHub Actions CI pipeline(not CD coz render auto deploys on push to main)
