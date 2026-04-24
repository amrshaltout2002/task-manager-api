from app.db.database import Base
from sqlalchemy import String, Integer, Column, ForeignKey, DateTime, func, Boolean
from sqlalchemy.orm import relationship
"""
tasks

id — primary key, integer, auto-increment
title — string, not null
description — string, nullable
is_completed — boolean, default false
priority — string, default "medium"
created_at — timestamp, default now
updated_at — timestamp, updates automatically
owner_id — foreign key → users.id
"""

class Task(Base):
    __tablename__ = "tasks"

    task_id = Column("task_id", Integer, primary_key=True, autoincrement=True)
    title = Column("title", String(255), nullable=False)
    description = Column("description", String(255), nullable=True)
    is_completed = Column("is_completed", Boolean, default=False)
    created_at = Column("created_at", DateTime, server_default=func.now())
    updated_at = Column("updated_at", DateTime, onupdate=func.now())
    
    owner_id = Column("owner_id", ForeignKey("users.user_id"), nullable=False)
    owner = relationship("User", back_populates="tasks")