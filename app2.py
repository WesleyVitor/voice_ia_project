import os

from tools import functions, route

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser


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

chain = prompt | llm | OpenAIFunctionsAgentOutputParser() | route 


res = chain.invoke({"input": "Pay the invoice lnbc1u1p35q4pdp5q4pdp5q4pdp5q4pdp"})
print(res)
