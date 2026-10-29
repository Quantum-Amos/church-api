from datetime import date, datetime

from pydantic import BaseModel, Field


class AttendanceSchemaIn(BaseModel):
    date: date
    men: int = Field(ge=0)
    women: int = Field(ge=0)
    youth: int = Field(ge=0)
    children: int = Field(ge=0)


class AttendanceSchemaOut(AttendanceSchemaIn):
    id: int
    created_at: datetime
