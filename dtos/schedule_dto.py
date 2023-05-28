from typing import List, Any
from dtos.course_dto import OpenedCourseSearchDto
from datetime import datetime

class ScheduleDto:
    name: str
    courses: List[OpenedCourseSearchDto] = None
    term: str = None
    score: int = None
    future_plan: List[Any] = None
    preferences: List[str] = None
    student_id: str = None
    time: datetime = None    
