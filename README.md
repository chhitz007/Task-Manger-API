# 🚀 Task Manager API

## 📌 Overview
A **FastAPI-based Task Manager API** that allows users to:
- **Register & Login** with JWT authentication 🔐
- **Create, Read, Update, and Delete (CRUD) tasks** 📋
- **Use PostgreSQL as the database** with SQLAlchemy ORM
- **Test API endpoints easily via Swagger UI**

## 🛠 Tech Stack
- **FastAPI** (Backend Framework)
- **PostgreSQL** (Database)
- **SQLAlchemy** (ORM)
- **JWT Authentication** (Security)
- **Alembic** (Database Migrations)
- **Uvicorn** (Server)

## ⚙️ Setup & Run Instructions
1️⃣ **Clone the repository:**
```sh
git clone https://github.com/your-username/Task-Manager-API.git
cd Task-Manager-API
```
2️⃣ **Create a virtual environment & install dependencies:**
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
3️⃣ **Setup PostgreSQL & Apply Migrations:**
```sh
alembic upgrade head
```
4️⃣ **Run the server:**
```sh
uvicorn main:app --reload
```
✅ **API is now running at:** `http://127.0.0.1:8000`

## 📌 API Endpoints
| Method  | Endpoint         | Description         |
|---------|-----------------|---------------------|
| `POST`  | `/register/`     | Register a user    |
| `POST`  | `/login/`        | Login & get JWT    |
| `GET`   | `/tasks/`        | Get all tasks      |
| `POST`  | `/tasks/`        | Create a new task  |
| `PUT`   | `/tasks/{id}`    | Update a task      |
| `DELETE`| `/tasks/{id}`    | Delete a task      |

## 📄 Testing & Documentation
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc UI**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)



