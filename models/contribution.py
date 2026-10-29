from collections import defaultdict
from datetime import date, datetime

from sqlalchemy import ForeignKey, String, cast, extract, select
from sqlalchemy.orm import Mapped, Session, mapped_column, relationship
from typing_extensions import Optional

from models import Base


class ContributionMapper(Base):
    amount: Mapped[float]
    date: Mapped[date]
    purpose: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    type_id: Mapped[Optional[int]] = mapped_column(ForeignKey("contribution_type.id", ondelete="SET NULL"))
    member_id: Mapped[Optional[int]] = mapped_column(ForeignKey("member.id", ondelete="SET NULL"))
    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey("user.id", ondelete="SET NULL"))
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())

    type: Mapped["ContributionTypeMapper"] = relationship(back_populates="contribution", passive_deletes="all")
    member: Mapped["MemberMapper"] = relationship(back_populates="contribution", passive_deletes="all")
    user: Mapped["UserMapper"] = relationship(back_populates="contribution", passive_deletes="all")

    @classmethod
    def get_by_year(cls, session: Session, year: str, type_id, purpose: Optional[str] = None, month: Optional[int] = None):
        query = select(cls).where(cls.type_id == type_id, cast(cls.created_at, String).ilike(f"%{year}%"))
        if purpose:
            query = query.where(cls.purpose == purpose)
        if month is not None:
            query = query.where(extract("month", cls.created_at) == month)
        contributions = session.scalars(query).all()
        monthly_total = defaultdict(int)
        for contribution in contributions:
            month = contribution.created_at.month
            monthly_total[month] += contribution.amount
        return monthly_total

    @classmethod
    def get_by_type_id(cls, session: Session, type_id: int, year: Optional[int] = None, month: Optional[int] = None):
        query = select(cls).where(cls.type_id == type_id)
        if year is not None:
            query = query.where(extract("year", cls.created_at) == year)
            if month is not None:
                query = query.where(extract("month", cls.created_at) == month)
        return session.scalars(query).all()


class ContributionTypeMapper(Base):
    name: Mapped[str]

    contribution: Mapped["ContributionMapper"] = relationship(back_populates="type")
