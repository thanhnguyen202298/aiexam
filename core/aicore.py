
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
#from langchain import FAISS
#from langchain.chains.question_answering import load_qa_chain
#from langchain.llms import OpenAI

import openai
import os
import msMLAIapp as msai
import config as apiSetting

keyAI = apiSetting.config["apiKey"]

openai.api_key = keyAI  
os.environ["OPENAI_API_KEY"] = keyAI

def ask2Bot(questionList):
    params = dict(model="gpt-3.5-turbo", messages=questionList)
    response = openai.ChatCompletion.create(**params)

def msAsking(question):
     return msai.callBot(question)[1]

def ask_question(question):
    content = ask2Bot()

print(keyAI)