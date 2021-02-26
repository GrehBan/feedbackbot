from dotenv import load_dotenv
from os import getenv
import json
import re
from pathlib import Path


load_dotenv()
TOKEN=getenv("TOKEN")
SUPERUSER_ID = int(getenv("SUPERUSER_ID"))
ID_REGEXP = re.compile(r'#ID(\d+)')
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / 'data'
