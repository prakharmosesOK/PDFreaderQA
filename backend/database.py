from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
"""
This code sets up a SQLAlchemy engine, declarative base, and sessionmaker for database interaction.
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)
from database import engine, Base, Session
# Create a database session
session = Session()
# Query the database
results = session.query(User).all()
# Close the session
session.close()
- None
- A SQLAlchemy engine, declarative base, and sessionmaker.
"""

SQLALCHEMY_DATABASE_URL = "sqlite:///./pdfDatabase.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
"""
This code sets up a SQLAlchemy engine, declarative base, and sessionmaker for database interaction with a SQLite database.
from database import engine, SessionLocal, Base
# Create a database session
db = SessionLocal()
# Query the database
results = db.query(User).all()
# Commit changes to the database
db.commit()
# Close the session
db.close()
- None
- A SQLAlchemy engine, sessionmaker, and declarative base for SQLite database interaction.
"""

def get_db():
    """
    Get a database session.

    This function provides a thread-local database session.
    It creates a new session on the first call and closes it on the last call.

    Usage:
    ```
    from database import get_db

    db = get_db()
    results = db.query(User).all()
    db.close()
    ```

    Returns:
        A SQLAlchemy database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


