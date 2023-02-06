from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_URL = 'sqlite:////home/l4m3r/Documents/Projects/CRUD_App/Chinook_Sqlite.sqlite'

engine = create_engine(DB_URL, echo=True)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


print(DB_URL)
