from os import environ

from dotenv import find_dotenv, load_dotenv
from pymongo import MongoClient


load_dotenv(find_dotenv())

cluster = MongoClient(environ.get('CONNECTION_PROPERTIES'))

db = cluster.shad112_Gaganovs_petroject

from db import data_manipulation
from db import init_db
from db import work_functions
from db import data_functions