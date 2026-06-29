from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.environ.get("GROQ_API_KEY")
)

prompt = PromptTemplate(
    template = 'write a 3 line summary for this text {text}',
    input_variables = ['text']
)
loader = WebBaseLoader("https://en.wikipedia.org/wiki/Artificial_intelligence")
docs = loader.load()

print(docs[0].page_content)

parser = StrOutputParser()
chain = prompt | llm | StrOutputParser()
result = chain.invoke(docs[0].page_content)
print(result)