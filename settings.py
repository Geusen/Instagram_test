import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ID = os.environ.get("ID")
PW = os.environ.get("PASSWORD")
