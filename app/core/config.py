from typing import List

from fastapi.templating import Jinja2Templates
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

config = Config(".env")

templates = Jinja2Templates(directory="app/templates")

PROJECT_NAME = config("PROJECT_NAME", default="FastAPI Project")
DATABASE_URL = config("DATABASE_URL", default="sqlite:///./app/db.sqlite3")
SECRET_KEY = config("SECRET_KEY", default="secret")
DEBUG = config("DEBUG", cast=bool, default=False)
ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS", cast=CommaSeparatedStrings, default=""
)
