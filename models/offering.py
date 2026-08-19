from sqlalchemy import String, Integer, select
from sqlalchemy.orm import Mapped, mapped_column, Session
from models import Base


class OfferingType(Base):
    """
    OfferingType model class.
    """
    __tablename__ = 'offering_types'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    # @classmethod
    # def get_all(cls, session: Session):
    #     """
    #     Fetch all offering types from the database.

    #     :param session: SQLAlchemy session object
    #     :return: List of OfferingType objects
    #     """
    #     return session.scalars(select(cls)).all()

    # @classmethod
    # def create(cls, session: Session, name: str):
    #     """
    #     Create a new offering type.

    #     :param session: SQLAlchemy session object
    #     :param name: Name of the offering type
    #     :return: The created OfferingType object
    #     """
    #     new_offering_type = cls(name=name)
    #     session.add(new_offering_type)
    #     session.commit()
    #     return new_offering_type