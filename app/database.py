from config import engine
from sqlalchemy.orm import sessionmaker
session = sessionmaker(bind=engine)()
