from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#Config DB
username = 'root'
password = ''
server = 'localhost'
dbname = 'fastapi'

SQLALCHEMY_DATABSE_URL="mysql+mysqlconnector://{username}:{password}@{server}/{dbname}".format(username, password, server,dbname)

engine = create_engine (SQLALCHEMY_DATABSE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()