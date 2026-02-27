from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas, crud
from database import SessionLocal, engine

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="JobFair Admin API")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "JobFair Admin API"}

# Dashboard endpoint - MATCHES YOUR IMAGE
@app.get("/api/dashboard", response_model=schemas.DashboardSummary)
def get_dashboard(db: Session = Depends(get_db)):
    return crud.get_dashboard_summary(db)

# Applicants endpoints
@app.get("/api/applicants", response_model=List[schemas.Applicant])
def read_applicants(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    applicants = crud.get_applicants(db, skip=skip, limit=limit)
    return applicants

@app.post("/api/applicants", response_model=schemas.Applicant)
def create_applicant(applicant: schemas.ApplicantCreate, db: Session = Depends(get_db)):
    return crud.create_applicant(db=db, applicant=applicant)

# Companies endpoints
@app.get("/api/companies", response_model=List[schemas.Company])
def read_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    companies = crud.get_companies(db, skip=skip, limit=limit)
    return companies

@app.post("/api/companies", response_model=schemas.Company)
def create_company(company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    return crud.create_company(db=db, company=company)

# Events endpoints
@app.get("/api/events", response_model=List[schemas.Event])
def read_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    events = crud.get_events(db, skip=skip, limit=limit)
    return events

@app.post("/api/events", response_model=schemas.Event)
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    return crud.create_event(db=db, event=event)

# Activities endpoints
@app.get("/api/activities", response_model=List[schemas.Activity])
def read_activities(limit: int = 10, db: Session = Depends(get_db)):
    activities = crud.get_recent_activities(db, limit=limit)
    return activities

@app.post("/api/activities", response_model=schemas.Activity)
def create_activity(activity: schemas.ActivityCreate, db: Session = Depends(get_db)):
    return crud.create_activity(db=db, activity=activity)