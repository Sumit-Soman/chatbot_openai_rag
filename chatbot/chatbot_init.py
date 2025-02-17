import os
from dotenv import load_dotenv
import chatbot_openai_rag
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class Chatbot:
    def __init__(self):
        self.pdf_path = 'data/Library_Bookings.pdf'
        self.vectorstore = self._create_vector_db()

    def _create_vector_db(self):
        # Extract text from PDF and split into chunks
        split_docs = self._extract_text_from_pdf()
        
        # Store extracted text into ChromaDB
        embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        vectorstore = Chroma.from_documents(split_docs, embedding=embeddings, persist_directory="db")
        return vectorstore

    def _extract_text_from_pdf(self):
        loader = PyPDFLoader(self.pdf_path, mode="single")
        docs = loader.load()
        # Split documents into smaller chunks for embedding
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        split_docs = text_splitter.split_documents(docs)
        return split_docs

    def generate_response(self, query):
        # Search ChromaDB for relevant documents
        docs = self.vectorstore.similarity_search(query, k=5)
        
        # Prepare the context for OpenAI
        context = ""
        for i, doc in enumerate(docs):
            context += f"{i+1}. {doc.page_content}\n"
        
        # Generate a response using OpenAI
        response = chatbot_openai_rag.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful librarian."},
                {"role": "user", "content": f"Based on the following information:\n{context}\n\nAnswer the following question: {query}"}
            ]
        )
        
        return response.choices[0].message.content, context