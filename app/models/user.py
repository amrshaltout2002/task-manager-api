from app.db.database import Base
from sqlalchemy import String, Integer, Column, DateTime, func, Boolean
from sqlalchemy.orm import relationship
"""
users

id — primary key, integer, auto-increment
email — string, unique, not null
username — string, unique, not null
hashed_password — string, not null
is_active — boolean, default true
created_at — timestamp, default now
"""

class User(Base):
    __tablename__ = "users"

    user_id = Column("user_id", Integer, primary_key=True, autoincrement=True)
    email = Column("email", String(255), unique=True, nullable=False)
    username = Column("username", String(255), unique=True, nullable=False)
    hashed_password = Column("hashed_password", String(255), nullable=False)
    is_active = Column("is_active", Boolean, default=True)
    created_at = Column("created_at", DateTime, server_default=func.now())

    tasks = relationship("Task", back_populates="owner")    