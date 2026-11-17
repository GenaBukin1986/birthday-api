import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# URL берём из переменной окружения (для Docker) или используем локальный
DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql+psycopg://admin:admin@localhost:5432/birthdays"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
