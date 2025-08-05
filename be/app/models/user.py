from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.orm import relationship

from app.models.base import BareBaseModel

class User(BareBaseModel):
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)
    role = Column(String, default='guest')
    last_login = Column(DateTime)
    
    # One-to-Many: User -> Projects
    projects = relationship("Project", back_populates="user", cascade="all, delete-orphan")
