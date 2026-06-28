from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

loader = TextLoader("RAG.txt", encoding="utf8")


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.environ.get("GROQ_API_KEY")
)

prompt = PromptTemplate(
    template = 'write a summary for this text {text}',
    input_variables = ['text']
)
docs = loader.load()
parser = StrOutputParser()
chain = prompt | llm | StrOutputParser()


result = chain.invoke(docs[0].page_content)
print(result)
