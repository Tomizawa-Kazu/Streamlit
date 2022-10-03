import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv()
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')
