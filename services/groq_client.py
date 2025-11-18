# dependency
import getpass
import os

from langchain_groq import ChatGroq

def get_llm_groq_model(modelName):
    #import groq api key
    if "GROQ_API_KEY" not in os.environ:
        os.environ["GROQ_API_KEY"] = getpass.getpass("Enter your Groq API key: ")
    return ChatGroq(model=modelName)


llm = get_llm_groq_model("llama3-8b-8192")
