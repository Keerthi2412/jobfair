from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.sql import func
from database import Base

class Applicant(Base):
    __tablename__ = "applicants"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    email = Column(String, unique=True, index=True)
    resume_url = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    status = Column(String, default="new")

class Company(Base):
    __tablename__ = "companies"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    registered_at = Column(DateTime(timezone=True), server_default=func.now())
    booth_number = Column(String, nullable=True)

class Event(Base):
    __tablename__ = "events"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    event_date = Column(DateTime)
    description = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Placement(Base):
    __tablename__ = "placements"
    
    id = Column(Integer, primary_key=True, index=True)
    applicant_id = Column(Integer, ForeignKey("applicants.id"))
    company_id = Column(Integer, ForeignKey("companies.id"))
    placement_date = Column(DateTime(timezone=True), server_default=func.now())
    position = Column(String)

class Activity(Base):
    __tablename__ = "activities"
    
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    activity_type = Column(String)  # 'registration', 'submission', 'approval', etc.