from dotenv import load_dotenv
import os

load_dotenv()

WEB_HOOK = os.getenv("WEB_HOOK")

API_URL = os.getenv("URL")
API_USER = os.getenv("USR")
API_PASS = os.getenv("PASS")
API_DB = os.getenv("DB")

abs_path = os.path.abspath(__file__ + "../../../")
