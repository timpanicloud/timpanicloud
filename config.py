__author__ = 'artem'
from app.model import *
import os
from sqlalchemy import create_engine
root_path=os.path.dirname(os.path.abspath(__file__))

db_path=os.path.join(root_path, 'app.db')

engine = create_engine('sqlite:///'+db_path, echo=True)