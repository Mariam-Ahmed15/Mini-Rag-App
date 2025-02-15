from fastapi import FastAPI # type: ignore
from routes import base,data

app = FastAPI()
app.include_router(base.base_router)
app.include_router(data.data_router)


