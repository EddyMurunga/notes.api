from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# This creates/connects to a file called notes.db in your project folder
DATABASE_URL = "sqlite:///./notes.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# This function gives each API request its own database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()