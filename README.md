# FastAPI Social Backend

A RESTful API backend for a social media platform(generic) built with FastAPI and PostgreSQL.

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

## Tech Stack

- **FastAPI** - Python web framework for building APIs
- **PostgreSQL** - Relational database
- **Psycopg3** - PostgreSQL adapter 
- **Pydantic** - Data validation using Python type hints
- **SQLAlchemy** - ORM for database interactions
- **Alembic** - Database migrations
- **JWT** - Token-based authentication

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