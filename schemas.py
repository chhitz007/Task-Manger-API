from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):  # ✅ Fix: Add this missing schema
    id: int
    username: str

    class Config:
        from_attributes = True  # Ensures SQLAlchemy model compatibility

class TokenData(BaseModel):
    username: str

# ✅ Schema for Creating a Task
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

# ✅ Schema for Updating a Task
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

# ✅ Schema for Returning Task Data (Response Model)
class TaskResponse(TaskCreate):
    id: int
    completed: bool

    class Config:
        from_attributes = True  # Allows SQLAlchemy model to return Pydantic model
