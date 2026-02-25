from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

class College(Base):
    __tablename__ = "colleges"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)
    country = Column(String)
    ranking = Column(Integer)
    specialization = Column(String)
    tuition = Column(Float)
    entrance_exam = Column(String)
    scholarship = Column(Boolean)
    website = Column(String)
