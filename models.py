from sqlalchemy import Column, Integer, String, DateTime
from database import Base
import datetime

class Scan(Base):
    __tablename__ = "scans"

    id = Column(Integer, primary_key=True, index=True)
    image_path = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    location = Column(String)
    description = Column(String)
    risk_level = Column(String)
    category = Column(String)
    recommendation = Column(String)
    model_mode = Column(String)
