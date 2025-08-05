from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), temperature=0.3)

def summarize_text(text):
    prompt = PromptTemplate.from_template(
        "Summarize the following content in simple bullet points:\n{text}"
    )
    chain = prompt | llm
    return chain.invoke({"text": text})