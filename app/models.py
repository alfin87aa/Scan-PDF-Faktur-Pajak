from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base                                                                                         
from sqlalchemy import Column, Integer, String, DateTime
from .database import engine

Base = declarative_base()

class LogScanPDF(Base):
    __tablename__ = 'LogScanPDF'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    full_path = Column(String)
    file_name = Column(String)
    company_code = Column(String)
    status = Column(String)
    notes = Column(String)
    created_date = Column(DateTime, server_default=func.now())

Base.metadata.create_all(engine)