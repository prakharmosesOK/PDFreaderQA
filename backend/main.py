from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import routes
import models
from database import engine
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(routes.router)
models.Base.metadata.create_all(bind=engine)
"""
This code creates a FastAPI application with a database. 
app = create_app()
from database import create_app
app = create_app()
- None
- A FastAPI application with a database.
"""

# Imporitng the libraries and the modules
# Importing the routes
# Defining the origins that are allowed to access the backend
origins = ["http://127.0.0.1:3000"]
# Creating tables in the database
models.Base.metadata.create_all(bind=engine)
# Creating the FastAPI app
app = FastAPI()
# Allowing frontend to access the backend and setting the desired configurations
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = False,            # Set to True to allow cookies
    allow_methods = ["*"],
    allow_headers = ["*"],
)
# Including desired routers
app.include_router(routes.router)
"""
This code creates a FastAPI application and sets up its CORS (Cross-Origin Resource Sharing) configuration, 
allowing requests from specified origins to access the backend API. 
It also creates tables in the database and includes routers defined in the routes module.
app = create_app()
from database import create_app
app = create_app()
- None
- A FastAPI application with CORS configuration and included routers.
"""

