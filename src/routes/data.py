from fastapi import FastAPI, APIRouter, Depends, UploadFile, status # type: ignore
from fastapi.responses import JSONResponse # type: ignore
import os
from helper.config import get_settings, Settings
from controllers import DataController

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"],
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id: int, file: UploadFile,
                      apee_settings: Settings = Depends(get_settings)):
    # validate the file properties
    is_valid, result_signal = DataController().validate_uploaded_file(file=file)

    return is_valid, result_signal

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": result_signal
            }
        )