from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ScanBase(BaseModel):
    location: Optional[str] = None
    description: Optional[str] = None

class ScanCreate(ScanBase):
    pass

class Scan(ScanBase):
    id: int
    image_path: str
    created_at: datetime
    risk_level: str
    category: str
    recommendation: str
    model_mode: str

    class Config:
        from_attributes = True
