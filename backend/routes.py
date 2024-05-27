# Importing necessary modules
from fastapi import APIRouter, status, UploadFile, File, Form, Depends
from typing import Dict, Any, Union, List
from sqlalchemy.orm import Session

# Importing the necessary functions from repository
import repositories as rp
import database as dbpdf

# Creating a router object
router = APIRouter(
    tags = ["PDF Chat bot"]
)


# Defining the routes
# --------------------------------------------------------------------------------------------------
# Route to upload the PDF file
@router.post('/upload_pdf', status_code = status.HTTP_201_CREATED)
async def upload_pdf(files: list[UploadFile] = File(None), db: Session = Depends(dbpdf.get_db)):
    return await rp.upload_pdf(files, db)

# Route to get the answer from the chatbot
@router.post('/chat', status_code = status.HTTP_200_OK)
async def get_answer(query: Dict[str, Any], db: Session = Depends(dbpdf.get_db)):
    return await rp.get_answer(query, db)

# Route to get the information about a perticulat PDF file
@router.get('/chat_info', status_code = status.HTTP_200_OK)
async def get_pdf_info(db: Session = Depends(dbpdf.get_db)):
    return await rp.get_pdf_info(db)

# Route to get the chat information from the chatbot
@router.post('/chat_hist', status_code = status.HTTP_200_OK)
async def get_chat_hist(route: Dict[str, Any], db: Session = Depends(dbpdf.get_db)):
    return await rp.get_chat_hist(route, db)

@router.delete('/delete_chat/{route}', status_code = status.HTTP_200_OK)
async def delete_chat(route: str, db: Session = Depends(dbpdf.get_db)):
    return await rp.delete_chat(route, db)