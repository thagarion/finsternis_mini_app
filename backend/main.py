from fastapi import FastAPI, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from datetime import datetime, date
from pytz import timezone
import pytz

from . import models
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/schedule")
def get_schedule(tz: str = Query(...), db: Session = Depends(get_db)):
    events = db.query(models.ScheduledEvent).all()

    try:
        user_tz = timezone(tz)
    except:
        return {"error": "Invalid timezone"}

    result = []
    now = datetime.now(user_tz)

    for e in events:
        berlin = timezone("Europe/Berlin")
        today = date.today()
        dt_berlin = berlin.localize(datetime.combine(today, e.time_berlin))
        dt_user = dt_berlin.astimezone(user_tz)

        if dt_user < now:
            dt_berlin = berlin.localize(datetime.combine(today.replace(day=today.day + 1), e.time_berlin))
            dt_user = dt_berlin.astimezone(user_tz)

        delta = dt_user - now

        result.append({
            "type": e.event_type,
            "time_local": dt_user.strftime("%Y-%m-%d %H:%M"),
            "in": str(delta).split(".")[0],
            "channels": e.channels
        })

    return result