import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Нет переменных окружения API_KEY, API_URL и FOLDER_ID")
else:
    load_dotenv()

API_KEY: str = os.getenv("API_KEY")
API_URL: str = os.getenv("API_URL")
FOLDER_ID: str = os.getenv("FOLDER_ID")
