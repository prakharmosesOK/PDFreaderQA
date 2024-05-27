# Multi PDF Chat-Bot

##  📖 Introduction

The Multi PDF Chatbot is an advanced application that enables users to interact with PDF documents through natural language processing. Users can upload PDFs, ask questions, get summaries, and receive detailed explanations based on the content. The application maintains a history of conversations for easy navigation and reference. Built with React, FastAPI, SQLite, LocalStorage, and LangChain, it offers a robust and user-friendly experience for extracting and understanding information from PDFs.

##  📝 Table of Contents

1. [Overview](#overview)
2. [Key Features](#key-features)
3. [Technological Stack](#technological-stack)
4. [Getting Started](#getting_started)
5. [Usage](#usage)
6. [Architecture](#architecture)
7. [API Endpoints](#apiendpoints)
8. [Future Improvements](#future-improvements)
9. [Contribution](#contribution)
10. [Author](#author)
11. [License](#license)

##  📝 Overview

The PDF Chatbot is an innovative application designed to facilitate seamless interaction with PDF documents through natural language processing. Users can upload one or more PDF files and engage with a chatbot to ask questions, obtain summaries, and get detailed explanations based on the content of the PDFs. The application also includes a conversation history feature, allowing users to navigate and revisit previous interactions.

##  ✨ Key Features

<ul>
  <li><strong>PDF Upload</strong>: Users can easily upload multiple PDF documents to the application.</li>
  <li><strong>Interactive Q&A</strong>: Engage with the chatbot to ask questions about the uploaded PDF content and receive accurate, context-aware responses.</li>
  <li><strong>Summarization</strong>: Get concise summaries of the content within the PDFs.</li>
  <li><strong>Detailed Explanations</strong>: Request in-depth explanations of specific sections or topics within the PDFs.</li>
  <li><strong>Conversation History</strong>: Save and navigate through the history of conversations for easy reference and continuity.</li>
  <li><strong>User-Friendly Interface</strong>: An intuitive and responsive frontend designed to enhance user experience.</li>
</ul>

##  ✈️ Technological Stack

<ul>
  <li><strong>Frontend</strong>: Developed using React, providing a dynamic and interactive user interface.</li>
  <li><strong>Backend</strong>: Built with FastAPI, ensuring a fast, reliable, and scalable server-side application.</li>
  <li><strong>Database</strong>: Utilizes SQLite for efficient data storage and management.</li>
  <li><strong>File Storage</strong>: Manages PDF files using LocalStorage, ensuring quick access and retrieval.</li>
  <li><strong>LLMs</strong>: Integrates LangChain for advanced natural language processing capabilities.</li>
</ul>

##  📲 Getting Started

  ### Prerequisites
  - Javascript (for frontend)
  - Python 3.8+ (for backend)
  - SQLite (for database)
  - Git (for version control)
  
  ### Installation
  
  #### Clone the Repository
  ```ps
  git clone https://github.com/prakharmosesOK/PDFreaderQA.git;
  cd PDFreaderQA
  ```

  #### Frontend setup
  1. Navigate to the frontend directory
     ```ps
     cd frontend
     ```
  2. Install the dependencies
     ```ps
     npm install
     ```
  3. Start the server
     ```ps
     npm start
     ```

  #### Backend setup
  1. Open another terminal and create a virtual environment
     ```ps
     python -m venv pdfchat
     ```
  2. Make a .env file in root directory of the project and store you Google api key.
     ```env
     GOOGLE_API_KEY = <your-google-api-key>
     ```
  3. Activate the virtual environment and navigate to the backend directory
     ```ps
     pdfChat\Scripts\activate.ps1;
     cd backend
     ```
  4. Install all the dependencies
     ```ps
     pip install -r requirements.txt
     ```
  5. Start the backend server
     ```ps
     uvicorn main:app --reload
     ```
  <strong>Congratulations! 🥳 the application is running.</strong>


##  🧑🏽‍💻 Usage

The landing page to the users is shown below:

![image](https://github.com/prakharmosesOK/PDFreaderQA/assets/142619454/92d7d399-1f4f-44e9-93d6-0339b9f26ab5)

<ul>
  <li>Users can either upload PDFs from local system using Upload button or can give link to an online article (not functional yet)</li>
  <li>Then user has to click <strong>Submit</strong> button for the processing of the files.</li>
  <li>After first two steps, users will be directly guided to the respective endpoints of the conversation which they can switch anytime with the others in the navbar on the left.</li>
  <li>An acronym for the files the users have uploaded will be shown near on top near the link input. Upon submitting a file, submit and uploads are disabled.</li>
</ul>

Upon uploading the interface generally looks like as shown below, then the user has to sumbit the documents/links:

![image](https://github.com/prakharmosesOK/PDFreaderQA/assets/142619454/70124646-96ab-4209-b157-8e9f7cc8e12e)

Then the user's can ask questions in the space provided below related to the uploaded documents. Or can switch to any other conversation or can even delete the conversations.

![image](https://github.com/prakharmosesOK/PDFreaderQA/assets/142619454/8f3443b6-b39d-46e2-b0e4-e55d7800c160)

### <a href="https://drive.google.com/file/d/1sI4LPJ22SG9EQxAUuI5ZbZbkdjk6xGro/view?usp=sharing">🎬 Video Link</a>
<br/>

##  🏰 Architecture

  ### Frontend (React)
  <ul>
    <li><strong>User Interface</strong>: Provides an interactive and responsive interface for users to upload PDFs, interact with the chatbot, and navigate conversation history.</li>
    <li><strong>State Management</strong>: Utilizes state management via Context API to manage application state.</li>
  </ul>

  ### Backend (FastAPI)
  <ul>
    <li><strong>API Endpoints</strong>: Exposes RESTful API endpoints for handling PDF uploads, user queries, and managing conversation history.</li>
    <li><strong>Data Processing</strong>: Processing the content of PDFs, embedding for vector database and interfaces with the LangChain models to generate responses.</li>
  </ul>

  ### Database (SQLite)
  <ul>
    <li><strong>Data Storage</strong>: Stores user data, conversation history, and metadata related to the uploaded PDF files.</li>
    <li><strong>ORM</strong>: Uses SQLAlchemy for object-relational mapping, for more intutive database interaction.</li>
  </ul>

  ### File Storage (LocalStorage)
  <ul>
    <li><strong>File Management</strong>: Saves uploaded PDF files locally with systematic organization to prevent file collisions.</li>
    <li><strong>Scalability Considerations</strong>: Provides availability for future transitioning to cloud storage solutions like AWS S3 if needed.</li>
  </ul>

  ### Natural Language Processing (LangChain)
  <ul>
    <li><strong>LLM Integration</strong>: Leverages LangChain for advanced natural language understanding and response generation.</li>
  </ul>

  ### Workflow
  <ul>
    <li><strong>User Interaction</strong>: Users interact with the chatbot via the React frontend, uploading PDFs and asking questions.</li>
    <li><strong>API Requests</strong>: The frontend sends requests to the FastAPI backend to process these interactions.</li>
    <li><strong>Data Processing</strong>: The backend processes the PDF content and queries using LangChain's LLMs to generate appropriate responses.</li>
    <li><strong>Response Delivery</strong>: The backend sends the responses back to the frontend, which displays them to the user.</li>
    <li><strong>Data Storage</strong>: All interactions and conversation history are stored in SQLite, and uploaded files are saved in LocalStorage as vector database for semantic search.</li>
  </ul>

##  ☁️ API Endpoints

The PDF Chatbot backend exposes several RESTful API endpoints to manage PDF uploads, interactions with the chatbot, and conversation history. Below is a list of the available endpoints:

  ### Upload PDF
  <ul>
    <li><strong>Endpoint</strong>: /upload_pdf</li>
    <li><strong>Method</strong>: POST</li>
    <li><strong>Description</strong>: Upload one or more PDF files to the chatbot.</li>
    <li><strong>Request Body</strong>:
      <ul>
        <li><strong>files (list of UploadFile)</strong>: List of PDF files to be uploaded.</li>
      </ul>
    </li>
    <li><strong>Response</strong>: Status code 201 Created on successful upload.</li>
  </ul>

  ### Get Answer from Chatbot
  <ul>
    <li><strong>Endpoint</strong>: /chat</li>
    <li><strong>Method</strong>: POST</li>
    <li><strong>Description</strong>: Get an answer from the chatbot based on the user's query.</li>
    <li><strong>Request Body</strong>:
      <ul>
        <li><strong>query (Dict[str, Any])</strong>: The user's query in JSON format.</li>
      </ul>
    </li>
    <li><strong>Response</strong>: Status code 200 OK with the chatbot's response.</li>
  </ul>

  ### Get Information about PDFs uploaded for a conversation
  <ul>
    <li><strong>Endpoint</strong>: /chat_info</li>
    <li><strong>Method</strong>: GET</li>
    <li><strong>Description</strong>: Retrieve information about the uploaded PDFs.</li>
    <li><strong>Response</strong>: Status code 200 OK with PDF information.</li>
  </ul>

  ### Get Chat History
  <ul>
    <li><strong>Endpoint</strong>: /chat_hist</li>
    <li><strong>Method</strong>: POST</li>
    <li><strong>Description</strong>: Retrieve the chat history from the chatbot.</li>
    <li><strong>Request Body</strong>:
      <ul>
        <li><strong>route (Dict[str, Any])</strong>: Route information in JSON format.</li>
      </ul>
    </li>
    <li><strong>Response</strong>: Status code 200 OK with the chat history.</li>
  </ul>

  ### Delete Chat
  <ul>
    <li><strong>Endpoint</strong>: /delete_chat/{route}</li>
    <li><strong>Method</strong>: DELETE</li>
    <li><strong>Description</strong>: Delete a specific chat from the history.</li>
    <li><strong>Path Parameter</strong>:
      <ul>
        <li><strong>route (str)</strong>: The route identifier of the chat to be deleted.</li>
      </ul>
    </li>
    <li><strong>Response</strong>: Status code 200 OK on successful deletion.</li>
  </ul>

##  📈 Future Improvements

<ol>
  <li>Will be extended to generating response based upon the links of online articles.</li>
  <li>Application UI can be more user friendly.</li>
  <li>Should be eable to generate response combining online articles and uploaded PDFs</li>
  <li>Extensions can be added to increase the capability of the bot.</li>
  <li>JWT authentication can be used for secure communication.</li>
</ol>

##  👷 Contributing

I welcome contributions form the community. Feel free to report bugs, submit pull requests or to feature requests to improve the Multi PDF Chatbot.

##  🎓 Author
  ### GitHub
  <p> <a href="https://github.com/prakharmosesOK"><b>Prakhar Moses </b><a/></p>
  <p> <a href="https://github.com/prakharmoses"><b>Prakhar Moses </b><a/></p>
  
  ### Mail
  <p> <a href="mailto:mosesprakhar@gmail.com"><b>Prakhar Moses</b></a></p>

##  📰 License
The Multi PDF Chatbot is not under any license. Viewers can't use it for commercial gains without the written permission of the author.

Happy Conversation! 🚀
