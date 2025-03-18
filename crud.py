from sqlalchemy.orm import Session
from models import Task
from schemas import TaskCreate, TaskUpdate

# ✅ Create Task (INSERT)
def create_task(db: Session, task: TaskCreate):
    db_task = Task(title=task.title, description=task.description, completed=False)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# ✅ Read All Tasks (SELECT)
def get_tasks(db: Session):
    return db.query(Task).all()

# ✅ Read a Single Task by ID (SELECT)
def get_task_by_id(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

# ✅ Update a Task (UPDATE)
def update_task(db: Session, task_id: int, task_data: TaskUpdate):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task:
        db_task.title = task_data.title if task_data.title else db_task.title
        db_task.description = task_data.description if task_data.description else db_task.description
        db_task.completed = task_data.completed if task_data.completed is not None else db_task.completed
        db.commit()
        db.refresh(db_task)
    return db_task

# ✅ Delete a Task (DELETE)
def delete_task(db: Session, task_id: int):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
        return True
    return False
