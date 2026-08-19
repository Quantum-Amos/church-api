from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel

from schemas import MemberSchemaOut, UserSchemaOut

class OfferingTypeSchemaIn(BaseModel):
    name: str

class OfferingTypeSchemaOut(OfferingTypeSchemaIn):
    id: int

class ContributionTypeSchemaIn(BaseModel):
    name: str


class ContributionTypeSchemaUpdate(BaseModel):
    id: int
    name: Optional[str] = None


class ContributionTypeSchemaOut(ContributionTypeSchemaIn):
    id: int


class ContributionSchemaIn(BaseModel):
    amount: float
    purpose: Optional[str] = None
    date: List[date]
    type_id: int
    member_id: Optional[int] = None


class ContributionSchemaUpdate(BaseModel):
    id: int
    amount: Optional[float] = None
    date: Optional[date] = None
    type_id: Optional[int] = None
    member_id: Optional[int] = None
    user_id: Optional[int] = None


class ContributionSchemaOut(BaseModel):
    id: int
    amount: float
    created_at: datetime
    date: date
    purpose: Optional[str] = None
    type: ContributionTypeSchemaOut
    member: Optional[MemberSchemaOut] = None
    user: Optional[UserSchemaOut] = None
