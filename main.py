from fastapi import FastAPI  # type: ignore
import os
from dotenv import load_dotenv   # type: ignore
load_dotenv()
from routes import base

app = FastAPI()
app.include_router(base.base_router)

print("APP_NAME:", os.getenv("APP_NAME"))
print("APP_VERSION:", os.getenv("APP_VERSION"))
