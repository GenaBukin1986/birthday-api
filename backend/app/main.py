from typing import Optional

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session

from . import database, models

app = FastAPI(title="Birthday Tracker API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
models.Base.metadata.create_all(bind=database.engine)


class PersonCreate(BaseModel):
    surname: Optional[str] = ""
    name: str
    patronymic: Optional[str] = ""
    year: int
    month: int
    day: int
    group: str
    note: Optional[str] = ""
    photo: Optional[str] = None


@app.get("/api/people")
def get_people(db: Session = Depends(database.get_db)):
    return db.query(models.Person).all()


@app.post("/api/people")
def create_person(person: PersonCreate, db: Session = Depends(database.get_db)):
    db_person = models.Person(**person.dict())
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person


@app.delete("/api/people/{person_id}")
def delete_person(person_id: int, db: Session = Depends(database.get_db)):
    db_person = db.query(models.Person).filter(models.Person.id == person_id).first()
    if not db_person:
        raise HTTPException(status_code=404, detail="Человек не найден")
    db.delete(db_person)
    db.commit()
    return {"status": "ok"}
