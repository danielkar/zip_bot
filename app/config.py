from enum import Enum
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

TOKEN = os.getenv('TOKEN')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
DB = os.getenv('DB')
DEBUG = os.getenv('DEBUG')

class States(Enum):
    
    S_START = 0
    S_LOGIN = 1
    S_PROJECT_NAME = 2
    S_SEND_ZIP = 3
