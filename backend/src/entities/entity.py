from datetime   import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
"""import mysql.connector 


import mysql.connector as mysql

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "teamo"
)
    """
 
db_url = 'localhost'
db_name = 'test'
db_user = 'felipe'
db_password = 'teamo'
engine = create_engine(f'mysql+mysqlconnector://{db_user}:{db_password}@{db_url}/{db_name}')

Session = sessionmaker(bind=engine)

Base = declarative_base()

print('### Base:', Base)
print('### Base:', engine)

class Entity():
    id              = Column(Integer, primary_key=True)
    created_at      = Column(DateTime)
    updated_at      = Column(DateTime)
    last_updated_by = Column(String(50))
    def __init__(self, created_by):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by


