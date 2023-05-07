from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    surname = Column(String)
    email = Column(String, unique=True)
    phone = Column(String)
    birthday = Column(Date)
    additional_info = Column(String, nullable=True)
