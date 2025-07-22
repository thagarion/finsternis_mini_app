from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

from sqlalchemy import Column, Integer, String, Time
from sqlalchemy.types import JSON
from .database import Base

class ScheduledEvent(Base):
    __tablename__ = "scheduled_events"
    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String)
    time_berlin = Column(Time)
    channels = Column(JSON)