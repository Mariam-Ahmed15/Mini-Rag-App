from pydantic import BaseModel, Field, field_validator
from typing import Optional
from bson.objectid import ObjectId  # type: ignore # Ensure pymongo provides this

class DataChunk(BaseModel):
    _id: Optional[ObjectId]
    chunk_text: str = Field(..., min_length=1)
    chunk_metadata: dict
    chunk_order: int = Field(..., gt=0)
    chunk_project_id: ObjectId

    @field_validator("chunk_text")
    @classmethod
    def validate_chunk_text(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("chunk_text cannot be empty or whitespace")
        return value

    class Config:
        arbitrary_types_allowed = True

