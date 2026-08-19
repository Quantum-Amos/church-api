from typing import List

from fastapi import APIRouter, Depends, Security
from sqlalchemy.orm import Session

from core import NotFound, get_db_session
from models import (OfferingType)
from schemas import (OfferingTypeSchemaIn, OfferingTypeSchemaOut)
from services import IsAuthenticated

offering_type_router = APIRouter(
    prefix="/api/offering-type",
    tags=["Offering Type"],
)

@offering_type_router.get("/", response_model=List[OfferingTypeSchemaOut], dependencies=[Security(IsAuthenticated())])
def get_all_offering_types(db: Session = Depends(get_db_session)):
    return OfferingType.get_all(session = db)

@offering_type_router.post("/", response_model=OfferingTypeSchemaOut, dependencies=[Security(IsAuthenticated())])
def create_offering_type(offering_type: OfferingTypeSchemaIn, db: Session = Depends(get_db_session)):
    return OfferingType.create(session = db, data = offering_type.model_dump())

@offering_type_router.delete("/{id}", dependencies=[Security(IsAuthenticated())])
def delete_offering_type(id: int, db: Session = Depends(get_db_session)):
    NotFound(db, {OfferingType: [id]}).__call__()
    return OfferingType.delete(db, id)