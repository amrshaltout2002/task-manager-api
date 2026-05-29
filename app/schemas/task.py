from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime

class TaskCreate(BaseModel):
    title: str = Field(..., max_length= 100)
    description: str | None = Field(default= None, max_length= 255)
    priority: str = Field(default= "medium")

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    priority: str | None = None
    is_completed: bool | None = None

class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    description: str | None
    priority: str
    is_completed: bool
    created_at: datetime
    updated_at: datetime | None
    owner_id: int