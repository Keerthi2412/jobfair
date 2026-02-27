from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Applicant schemas
class ApplicantBase(BaseModel):
    name: Optional[str] = None
    email: str
    resume_url: Optional[str] = None

class ApplicantCreate(ApplicantBase):
    pass

class Applicant(ApplicantBase):
    id: int
    created_at: datetime
    status: str
    
    class Config:
        orm_mode = True

# Company schemas
class CompanyBase(BaseModel):
    name: str
    booth_number: Optional[str] = None

class CompanyCreate(CompanyBase):
    pass

class Company(CompanyBase):
    id: int
    registered_at: datetime
    
    class Config:
        orm_mode = True

# Event schemas
class EventBase(BaseModel):
    title: str
    event_date: datetime
    description: Optional[str] = None

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int
    created_at: datetime
    
    class Config:
        orm_mode = True

# Activity schemas
class ActivityBase(BaseModel):
    description: str
    activity_type: str

class ActivityCreate(ActivityBase):
    pass

class Activity(ActivityBase):
    id: int
    timestamp: datetime
    
    class Config:
        orm_mode = True

# Dashboard summary schema
class DashboardSummary(BaseModel):
    total_applicants: int
    applicants_change: str  # "+12.5% from last month"
    total_companies: int
    companies_change: str
    upcoming_events: int
    events_change: str
    total_placements: int
    placements_change: str
    recent_activities: list[Activity]