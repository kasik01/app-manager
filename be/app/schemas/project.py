from typing import Optional
from pydantic import BaseModel


class ProjectBase(BaseModel):
    name: str
    description: str = None
    is_active: bool = True

    class Config:
        from_attributes = True

class ProjectCreateRequest(BaseModel):
    user_id: Optional[int] = None
    name: Optional[str] = None
    is_active: Optional[bool] = True
    description: Optional[str] = None
    url: Optional[str] = None

class ProjectDetailResponse(BaseModel):
    user_id: Optional[int] = None
    name: Optional[str] = None
    is_active: Optional[bool] = True
    description: Optional[str] = None
    url: Optional[str] = None

class ProjectUpdateRequest(BaseModel):
    name: Optional[str] = None
    is_active: Optional[bool] = True
    description: Optional[str] = None
    url: Optional[str] = None
