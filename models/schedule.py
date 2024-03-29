from typing import Optional, List, Any
from .course import FuturePlan
from .time import Term
from .preferences import Preference
from beanie import Document
from datetime import datetime



class Schedule(Document):
    name: Optional[str]
    courses: Optional[List[str]] = None
    term: Optional[Term] = None
    score: Optional[int] = None
    future_plan: Optional[List[FuturePlan]] = None
    preferences: Optional[List[dict]] = None
    student_id: Optional[str] = None
    time: Optional[datetime] = datetime.now()

    class Settings:
        name = "schedules"
