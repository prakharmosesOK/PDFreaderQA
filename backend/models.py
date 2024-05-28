from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from typing import List
import datetime
"""
This code defines a data model for PDF data, including attributes such as ID, filename, route name, vector database path, chat history, and date/time of last update.
from database import PDFdata
pdf_data = PDFdata(
    filename="my_pdf.pdf",
    route_name="my_pdf_route",
    vector_db_path="/path/to/vector_db",
    chat_hist=[],
    date_time=datetime.datetime.now()
)
from database import PDFdata
# Create a new PDF data object
pdf_data = PDFdata(
    filename="my_pdf.pdf",
    route_name="my_pdf_route",
    vector_db_path="/path/to/vector_db",
    chat_hist=[],
    date_time=datetime.datetime.now()
)
# Add the PDF data object to the database session
db.session.add(pdf_data)
# Commit the changes to the database
db.session.commit()
- None
- A data model for PDF data.
"""



class PDFdata(Base):
    """
    A data model for PDF data.

    **Attributes:**
    - `id`: The ID of the PDF data.
    - `filename`: The filename of the PDF file.
    - `routeName`: The route name of the PDF file.
    - `vectorDBpath`: The path to the vector database for the PDF file.
    - `chatHist`: The chat history for the PDF file.
    - `dateTime`: The date and time of the last update to the PDF data.
    """

    __tablename__ = "pdfdata"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    routeName = Column(String)
    vectorDBpath = Column(String)
    chatHist = Column(String)
    dateTime = Column(DateTime, default = datetime.datetime.now)


