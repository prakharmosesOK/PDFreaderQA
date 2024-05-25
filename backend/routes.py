# Importing necessary modules
from fastapi import APIRouter, status

# Importing the necessary functions from repository
from . import repositories as rp

# Creating a router object
router = APIRouter(
    tags = ["PDF Chat bot"]
)


# Defining the routes
# --------------------------------------------------------------------------------------------------
# Route to upload the PDF file
@router.post('/upload', status_code = status.HTTP_201_CREATED)
async def upload_pdf(file: bytes):
    return await rp.upload_pdf(file)

# Route to get the answer from the chatbot
@router.post('/chat', status_code = status.HTTP_200_OK)
async def get_answer(question: str):
    return await rp.get_answer(question)