import os

from tools import functions, route

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser

import openai

from dotenv import load_dotenv
load_dotenv()


llm = ChatOpenAI(
    temperature=0, 
    openai_api_key=os.getenv("OPENAI_API_KEY"),
).bind(functions=functions)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are helpful but sassy assistant"),
    ("user", "{input}"),
])

openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI()
audio_file = open("gravacao2.ogg", "rb")

translation = client.audio.translations.create(
    model="whisper-1", 
    file=audio_file
    
)

chain = prompt | llm | OpenAIFunctionsAgentOutputParser() | route 

print(translation.text)
res = chain.invoke({"input": translation.text})
print(res)