import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
# import all your models here 
from models import *


file_path = "db//storedb.db"

if os.name != 'nt':
    file_path = "db/storedb.db"
        
print(file_path)

# database
DATABASE_URL = "sqlite:///" + file_path

engine = create_engine(DATABASE_URL, echo=True)
Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base.query = Session.query_property()

def init_db():
    # import all your models here    
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")