# FastAPI Social Backend

A RESTful API backend for a social media platform built with FastAPI and PostgreSQL.

## Project Status

Currently in active development. Building incrementally, structure and architecture will be refactored as features are added.

## Features (In Progress)

- ✅ Basic CRUD operations for posts
- ✅ PostgreSQL database integration
- ✅ RESTful API endpoints
- ✅ Migrating all operations to database
- 🔄 SQLAlchemy ORM integration
- 🔄 User authentication
- 🔄 Alembic database migrations
- 🔄 CI/CD pipeline with GitHub Actions

## Tech Stack

- **FastAPI** - Modern Python web framework for building APIs
- **PostgreSQL** - Relational database
- **Psycopg3** - PostgreSQL adapter (transitioning to SQLAlchemy)
- **Pydantic** - Data validation using Python type hints
- **SQLAlchemy** - ORM (upcoming)
- **Alembic** - Database migrations (upcoming)
- **GitHub Actions** - CI/CD (upcoming)

## Current Endpoints

```
GET    /              - Root endpoint
GET    /posts         - Get all posts
POST   /posts         - Create a new post
GET    /posts/{id}    - Get post by ID
PUT    /posts/{id}    - Update post by ID
DELETE /posts/{id}    - Delete post by ID
```

## Development Roadmap

- [x] Set up basic FastAPI application
- [x] Connect PostgreSQL database
- [x] Implement basic CRUD operations
- [x] Complete database migration for all endpoints
- [ ] Integrate SQLAlchemy ORM
- [ ] Implement user authentication & authorization
- [ ] Add voting/like system
- [ ] Add Alembic for database migrations
- [ ] Add comprehensive tests
- [ ] Set up GitHub Actions CI/CD