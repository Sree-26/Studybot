from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

def create_qa_chain(text):
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = [Document(page_content=chunk) for chunk in splitter.split_text(text)]

    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    vectordb = FAISS.from_documents(docs, embeddings)

    qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectordb.as_retriever())
    return qa