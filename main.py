from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from auth import hash_password, create_access_token, verify_password, get_current_user
from database import SessionLocal
from models import User
from schemas import UserCreate
from datetime import timedelta
import schemas
from models import Task
import crud

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Task Manager API!"}

# ✅ Dependency: Get Database Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Register a New User
@app.post("/register/", response_model=schemas.UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed_password = hash_password(user.password)
    new_user = User(username=user.username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user  # ✅ Return user data

# ✅ User Login & Get JWT Token
@app.post("/login/")
def login_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    access_token = create_access_token(data={"sub": user.username}, expires_delta=timedelta(minutes=30))
    return {"access_token": access_token, "token_type": "bearer"}

# ✅ Get All Tasks (Protected)
@app.get("/tasks/", response_model=list[schemas.TaskResponse])
def read_tasks(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return crud.get_tasks(db)

# ✅ Create a Task (Protected)
@app.post("/tasks/", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return crud.create_task(db, task)

# ✅ Get Task by ID (Protected)
@app.get("/tasks/{task_id}", response_model=schemas.TaskResponse)
def read_task(task_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    task = crud.get_task_by_id(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# ✅ Update Task (Protected)
@app.put("/tasks/{task_id}", response_model=schemas.TaskResponse)
def update_task(task_id: int, task_data: schemas.TaskUpdate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    updated_task = crud.update_task(db, task_id, task_data)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

# ✅ Delete Task (Protected)
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    success = crud.delete_task(db, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}



