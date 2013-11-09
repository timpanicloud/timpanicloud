__author__ = 'artem'
from app.model import *
from config import *
import os
try:
    os.remove(db_path)
except:
    pass
Base.metadata.create_all(engine)
