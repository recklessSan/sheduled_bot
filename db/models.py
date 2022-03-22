from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Float, String, ForeignKey, Boolean, DateTime, Integer
import uuid


Base = declarative_base()


class Keys(Base):
    __tablename__ = 'keys'
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    token = Column(String())

