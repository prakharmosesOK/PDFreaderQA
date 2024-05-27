# import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from io import BytesIO

load_dotenv()
gemini_api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))


# if 'conversation_history' not in st.session_state:
#   st.session_state['conversation_history'] = []


# def get_pdf_text(pdf_docs):
#     text=""
#     for pdf in pdf_docs:
#         pdf_reader= PdfReader(pdf)
#         for page in pdf_reader.pages:
#             text += page.extract_text()
#     return  text
async def get_pdf_text(files):
    raw_text = ""
    if files:
        filename = ""
        for file in files:
            filename += str(file.filename)[:5]
            try:
                pdf_bytes = await file.read()
                reader = PdfReader(BytesIO(pdf_bytes))
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
                raw_text += text
            except Exception as e:
                raw_text = f"Error reading file: {filename}"
        return filename, raw_text
    else:
        return "No file given", ""


def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks


def get_vector_store(text_chunks, filename, saving_path):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local(saving_path)
    return saving_path


def get_conversational_chain():

    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the questino is related
    to thanks or gratitude then just say "You're welcome! Feel free to ask if there are any other questions", if someone asks who is your
    author or developer or related to who made you then say "My developer prefers to remain anonymous", if the answer is not in
    provided context just say, "Answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = ChatGoogleGenerativeAI(model="gemini-pro",
                             temperature=0.3)

    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain



def user_input(user_question, vecDBpath):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    
    new_db = FAISS.load_local(f"{vecDBpath}", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()
    # context = st.session_state['conversation_history']

    
    response = chain(
        {"input_documents":docs, "question": user_question},
        return_only_outputs=True
    )
    
    # st.session_state['conversation_history'].append({"question": user_question, "answer": response["output_text"]})

    # print(st.session_state['conversation_history'])
    # st.write("Reply: ", response["output_text"])
    return response["output_text"]




# def main():
#     st.set_page_config("Chat PDF")
#     st.header("Chat with PDF using Gemini💁")

#     user_question = st.text_input("Ask a Question from the PDF Files")

#     if user_question:
#         user_input(user_question)

#     with st.sidebar:
#         st.title("Menu:")
#         pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
#         print("The PDF required is:\n", pdf_docs)
#         if st.button("Submit & Process"):
#             with st.spinner("Processing..."):
#                 raw_text = get_pdf_text(pdf_docs)
#                 text_chunks = get_text_chunks(raw_text)
#                 get_vector_store(text_chunks)
#                 st.success("Done")



# if __name__ == "__main__":
#     main()