from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import find_dotenv, load_dotenv


import os

load_dotenv(find_dotenv(raise_error_if_not_found=True))

# You can access the environment variables as such, and any variables from the .env file will be loaded in for you to use.
# os.getenv("DB_HOST")

# Start Here

db_host = os.getenv("DB_HOST")
db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
db_database = os.getenv("DB_DATABASE")
db_port = os.getenv("DB_PORT")


engine = create_engine('mysql://%s:%s@%s:%s/%s' %(db_username,db_password,db_host,db_port,db_database),echo=False)
Session = sessionmaker(bind=engine)

Base = declarative_base()
