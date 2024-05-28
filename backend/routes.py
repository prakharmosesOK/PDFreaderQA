from fastapi import APIRouter, status, UploadFile, File, Form, Depends
from typing import Dict, Any, Union, List
from sqlalchemy.orm import Session
import repositories as rp
import database as dbpdf
"""
This code defines the routes for the ChatPDF API, including functions for uploading PDFs, getting answers to questions, and managing chat history.
from api import router
app.include_router(router)
from api import router
app = FastAPI()
app.include_router(router)
- None
- A FastAPI router with the defined routes.
"""

# Importing necessary modules
# Importing the necessary functions from repository
# Creating a router object
router = APIRouter(
    tags = ["PDF Chat bot"]
)
# Defining the routes
# --------------------------------------------------------------------------------------------------
# Route to upload the PDF file
@router.post('/upload_pdf', status_code = status.HTTP_201_CREATED)
async def upload_pdf(files: list[UploadFile] = File(None), db: Session = Depends(dbpdf.get_db)):
    """
    Uploads a PDF file and creates a new entry in the database.
    **Usage**:
    ```
    from api import router
    @router.post("/uploadpdf")
    async def upload_pdf_route(files: list[UploadFile] = File(None), db: Session = Depends(dbpdf.get_db)):
        return await upload_pdf(files,db)
    ```
    **Arguments**:
    - `files`: A list of PDF files to be uploaded.
    - `db`: A database session.
    **Returns**:
    - A JSON response with the routeName and id of the newly created database entry.
    """
    return await rp.upload_pdf(files, db)
# Route to get the answer from the chatbot
@router.post('/chat', status_code = status.HTTP_200_OK)
async def get_answer(query: Dict[str, Any], db: Session = Depends(dbpdf.get_db)):
    """
    Gets the answer to a user's question from a specific PDF file.
    **Usage**:
    ```
    from api import router
    @router.post("/getanswer")
    async def get_answer_route(query: Dict[str, Any], db: Session = Depends(dbpdf.get_db)):
        return await get_answer(query,db)
    ```
    **Arguments**:
    - `query`: A dictionary containing the route and question.
    - `db`: A database session.
    **Returns**:
    - A JSON response with the answer to the user's question.
    """
    return await rp.get_answer(query, db)
# Route to get the information about a perticulat PDF file
@router.get('/chat_info', status_code = status.HTTP_200_OK)
async def get_pdf_info(db: Session = Depends(dbpdf.get_db)):
    """
    Gets information about all PDF files in the database.
    **Usage**:
    ```
    from api import router
    @router.get("/getpdfinfo")
    async def get_pdf_info_route(db: Session = Depends(dbpdf.get_db)):
        return await get_pdf_info(db)
    ```
    **Arguments**:
    - `db`: A database session.
    **Returns**:
    - A JSON response with a list of PDF file information.
    """
    return await rp.get_pdf_info(db)
# Route to get the chat information from the chatbot
@router.post('/chat_hist', status_code = status.HTTP_200_OK)
async def get_chat_hist(route: Dict[str, Any], db: Session = Depends(dbpdf.get_db)):
    """
    Gets the chat history for a specific PDF file.
    **Usage**:
    ```
    from api import router
    @router.post("/getchathis")
    async def get_chat_hist_route(route: Dict[str, Any], db: Session = Depends(dbpdf.get_db)):
        return await get_chat_hist(route,db)
    ```
    **Arguments**:
    - `route`: A dictionary containing the route.
    - `db`: A database session.
    **Returns**:
    - A JSON response with the chat history.
    """
    return await rp.get_chat_hist(route, db)
@router.delete('/delete_chat/{route}', status_code = status.HTTP_200_OK)
async def delete_chat(route: str, db: Session = Depends(dbpdf.get_db)):
    """
    Deletes the chat history for a specific PDF file.
    **Usage**:
    ```
    from api import router
    @router.post("/deletechat")
    async def delete_chat_route(route: str, db: Session = Depends(dbpdf.get_db)):
        return await delete_chat(route,db)
    ```
    **Arguments**:
    - `route`: The route of the PDF file to delete the chat history for.
    - `db`: A database session.
    **Returns**:
    - A JSON response with a success message.
    """
    return await rp.delete_chat(route, db)"""

