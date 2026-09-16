from fastapi import FastAPI, Depends
from schemas import Todo as TodoSchema, TodoCreate
from database import SessionLocal, Base, engine
from sqlalchemy.orm import Session
from models import Todo

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/todo", response_model=TodoSchema)
def create(todo: TodoCreate, db: Session = Depends((get_db))):
    db_todo = Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

