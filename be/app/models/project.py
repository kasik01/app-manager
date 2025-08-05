from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from app.models.base import BareBaseModel
from sqlalchemy.orm import relationship


class Project(BareBaseModel):
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    is_active = Column(Boolean, nullable=True)
    url = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False) # FK to User

    # Many-to-One: Project -> User
    user = relationship("User", back_populates="projects")