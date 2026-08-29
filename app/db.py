from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base 
from app.config import settings

#creating engine
engine = create_engine(settings.database_url)

#creating a session factory
SessionLocal = sessionmaker(bind=engine)

#create a base
Base = declarative_base()

def get_db():
    db = SessionLocal() 
    try:
        yield db
    finally:
        db.close()
    