# Blogify API

A RESTful API for a blogging platform built with FastAPI, Python, and asynchronous PostgreSQL. This project supports user authentication (signup/login), JWT-based token management, and complete CRUD operations for blog posts.

## 🚀 Features

- 🔐 User authentication with JWT access and refresh tokens
- 📝 Create, Read, Update, Delete (CRUD) operations for blog posts
- ⚡ FastAPI for high-performance asynchronous API
- 🗄️ PostgreSQL with async support for robust data storage
- 🔄 Database migrations managed via Alembic
- 🧪 Modular structure for easy testing and scaling

---

## 📁 Project Structure

The folder structure is organized for clarity, scalability, and modularity:

```
blogify-api/
├── .env.example                # Environment variables template
├── .gitignore                 # Git ignored files
├── alembic.ini                # Alembic configuration file
├── migrations/                # Alembic migration scripts
├── requirements.txt           # Project dependencies
├── src/
│   ├── main.py                # FastAPI app entry point and server initialization
│   ├── config.py              # Pydantic-based settings and environment configuration
│   ├── utils.py               # Utility functions (e.g., password hashing, token generation)
│   ├── db/
│   │   ├── models.py          # SQLAlchemy ORM models for User and Blog
│   │   ├── session.py         # Database connection and async session management
│   ├── auth/
│   │   ├── routes.py          # Authentication routes (signup, login)
│   │   ├── services.py        # Business logic for authentication
│   │   ├── schema.py          # Pydantic schemas for auth endpoints
│   ├── blogs/
│   │   ├── routes.py          # Blog CRUD routes
│   │   ├── services.py        # Blog-related business logic
│   │   ├── schema.py          # Pydantic schemas for blog endpoints
```

---

## 🛠️ Technologies Used

- Python 3.10+
- FastAPI
- PostgreSQL (asyncpg)
- SQLAlchemy (1.4+ async support)
- Alembic (for DB migrations)
- JWT (for secure token-based auth)
- Pydantic (for validation and config)
- Uvicorn (ASGI server)

---

## 🔧 Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/your-username/blogify-api.git
cd blogify-api
```

2. Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Setup environment variables:

```bash
cp .env.example .env
# Fill in your database URL, secret keys, etc. in the new .env file
```

4. Run migrations:

```bash
alembic upgrade head
```

5. Start the development server:

```bash
uvicorn src.main:app --reload
```

---

## 📬 API Endpoints Overview

- Auth:

  - POST /signup
  - POST /signin

- Blog:
  - GET /blogs
  - GET /blogs/{id}
  - POST /blogs
  - PUT /blogs/{id}
  - DELETE /blogs/{id}

---

## 📌 Future Improvements

- Role-based access control
- Pagination and filtering
- API rate limiting
- Unit and integration tests
- Swagger customization

---

## 📜 License

This project is licensed under the MIT License.
