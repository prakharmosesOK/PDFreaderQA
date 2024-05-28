from fastapi import HTTPException, UploadFile, File, Form, Depends
from typing import Dict, Any, Union, List
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import os
import json
import datetime
from ChatPDF import chat_file as cf
from ChatPDF import chat_link as cl
import database as dbpdf
import models
"""
This code imports all necessary modules and classes for the ChatPDF API.
from api import app
from api import app
app.get("/")(lambda: {"Hello": "World"})
- None
- A collection of modules and classes for the ChatPDF API.
"""

async def upload_pdf(files: list[UploadFile] = File(None), db: Session = Depends(dbpdf.get_db)):
    """
    Uploads a PDF file and creates a new entry in the database.
    **Usage**:
    ```
    from api import upload_pdf
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
    if files:
        filename, raw_text = await cf.get_pdf_text(files)
        folder = "chatHistAndUtils/"
        vectorstoarage_path = f"{folder}faiss_index_{filename}"
        if not os.path.exists(vectorstoarage_path):
            text_chunks = cf.get_text_chunks(raw_text)
            vectorstoarage_path = cf.get_vector_store(text_chunks, filename, vectorstoarage_path)
        # Handle database mechanism
        new_pdfChat = models.PDFdata(
            filename = filename,
            routeName = filename[:10],
            vectorDBpath = vectorstoarage_path
        )
        db.add(new_pdfChat)
        db.commit()
        db.refresh(new_pdfChat)
        return JSONResponse({"output": [new_pdfChat.routeName, new_pdfChat.id]})
    else:
        return JSONResponse({"output": "No files or PDF link provided"})
async def get_answer(query: Dict[str, Any], db: Session = Depends(dbpdf.get_db)):
    """
    Gets the answer to a user's question from a specific PDF file.
    **Usage**:
    ```
    from api import get_answer
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
    if query:
        print("The query is: ", query)
        route, question = query["route"], query["question"]
        vecDBpath, chats = db.query(models.PDFdata.vectorDBpath, models.PDFdata.chatHist).filter(models.PDFdata.id == int(route)).first()
        print("The chat actually is: ", chats)
        if chats is not None:
            chatActual = json.loads(chats)
        else:
            chatActual = []
        answer = cf.user_input(question, vecDBpath)
        chatActual.append({"question": question, "answer": answer})
        chatActual = json.dumps(chatActual)
        db.query(models.PDFdata).filter(models.PDFdata.id == route).update({"chatHist": chatActual, "dateTime": datetime.datetime.now()})
        db.commit()
        return JSONResponse({"output": answer})
    else:
        return JSONResponse({"output": "No question provided"})
async def get_pdf_info(db: Session = Depends(dbpdf.get_db)):
    """
    Gets information about all PDF files in the database.
    **Usage**:
    ```
    from api import get_pdf_info
    @router.get("/getpdfinfo")
    async def get_pdf_info_route(db: Session = Depends(dbpdf.get_db)):
        return await get_pdf_info(db)
    ```
    **Arguments**:
    - `db`: A database session.
    **Returns**:
    - A JSON response with a list of PDF file information.
    """
    raw_pdf_info = db.query(models.PDFdata.id, models.PDFdata.filename).order_by(models.PDFdata.dateTime.desc()).all()
    pdf_info = []
    for info in raw_pdf_info:
        pdf_info.append([info[0],info[1]])
    return JSONResponse({"output": pdf_info})
async def get_chat_hist(route: Dict[str, Any], db: Session = Depends(dbpdf.get_db)):
    """
    Gets the chat history for a specific PDF file.
    **Usage**:
    ```
    from api import get_chat_hist
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
    route = route["route"]
    if route:
        chat_hist = db.query(models.PDFdata.chatHist).filter(models.PDFdata.id == int(route)).first()
        chat_hist = chat_hist[0]
        if chat_hist is not None:
            chat_hist = json.loads(chat_hist)
            chat_hist = chat_hist[-11::]
        else:
            chat_hist = []
        return JSONResponse({"output": chat_hist})
    else:
        return JSONResponse({"output": "No route provided."})
async def delete_chat(route: str, db: Session = Depends(dbpdf.get_db)):
    """
    Deletes the chat history for a specific PDF file.
    **Usage**:
    ```
    from api import delete_chat
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
    if route:
        db.query(models.PDFdata).filter(models.PDFdata.id == int(route)).delete(synchronize_session=False)
        db.commit()
        return JSONResponse({"output": "Chat history deleted"})
    else:
        return JSONResponse({"output": "No route provided."})"""

