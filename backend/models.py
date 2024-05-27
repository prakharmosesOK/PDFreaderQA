from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from typing import List
import datetime


class PDFdata(Base):
    __tablename__ = "pdfdata"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    routeName = Column(String)
    vectorDBpath = Column(String)
    chatHist = Column(String)
    dateTime = Column(DateTime, default = datetime.datetime.now)