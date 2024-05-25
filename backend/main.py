# Imporitng the libraries and the modules
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importing the routes
from . import routes

# Defining the origins that are allowed to access the backend
origins = ["http://127.0.0.1:3000"]

# Creating the FastAPI app
app = FastAPI()

# Allowing frontend to access the backend and setting the desired configurations
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = False,            # Set to True to allow cookies
    allow_methods = ["*"],
    allow_headers = ["*"],
)

# Including desired routers
app.include_router(routes)