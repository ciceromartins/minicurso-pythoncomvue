from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, usersModel

HOST = "localhost"
USERNAME = "root"
PASSWORD = "minicurso"
DATABASE = "pythoncomvue"

DATABASE_URL = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(engine)
dbContext = Session()