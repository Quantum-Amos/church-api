from typing import List

from fastapi import APIRouter, Depends, Security
from sqlalchemy.orm import Session

from core import NotFound, get_db_session
from models import AttendanceMapper
from schemas import AttendanceSchemaIn, AttendanceSchemaOut
from services import IsAuthenticated

attendance_router = APIRouter(
    prefix="/api/attendance",
    tags=["ATTENDANCE"],
)


@attendance_router.get("", response_model=List[AttendanceSchemaOut], dependencies=[Security(IsAuthenticated())])
async def get_all(session: Session = Depends(get_db_session)):
    return AttendanceMapper.get_all(session)


@attendance_router.post("", response_model=AttendanceSchemaOut, dependencies=[Security(IsAuthenticated())])
async def post(data: AttendanceSchemaIn, session: Session = Depends(get_db_session)):
    return AttendanceMapper.create(session=session, data=data.model_dump())


@attendance_router.delete("/{id}", dependencies=[Security(IsAuthenticated())])
async def delete(id: int, session: Session = Depends(get_db_session)):
    NotFound(session, {AttendanceMapper: [id]}).__call__()
    return AttendanceMapper.delete(session, id)
