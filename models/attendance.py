from datetime import date, datetime

from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from models import Base


class AttendanceMapper(Base):
    date: Mapped[date]
    men: Mapped[int] = mapped_column(Integer)
    women: Mapped[int] = mapped_column(Integer)
    youth: Mapped[int] = mapped_column(Integer)
    children: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
