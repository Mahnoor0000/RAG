from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import shutil

# Optional: delete old Chroma DB to avoid duplicate ID errors
CHROMA_DIR = "james_dean_chroma_db"

if os.path.exists(CHROMA_DIR):
    shutil.rmtree(CHROMA_DIR)

# Create LangChain documents about James Dean

doc1 = Document(
    page_content="James Dean was an American actor remembered as a cultural icon of teenage rebellion and emotional intensity. Although his career was short, his impact on Hollywood and youth culture became legendary.",
    metadata={"topic": "biography"}
)

doc2 = Document(
    page_content="James Dean became famous for his role as Jim Stark in the film Rebel Without a Cause. The movie made him a symbol of restless youth, loneliness, and rebellion.",
    metadata={"topic": "film"}
)



docs = [doc1, doc2]

# Sentence Transformer embeddings
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True}
)

# Create Chroma vector store using Hugging Face embeddings
vector_store = Chroma(
    collection_name="james_dean_hf",
    embedding_function=embedding_model,
    persist_directory=CHROMA_DIR
)

ids = ["doc1", "doc2"]

vector_store.add_documents(
    documents=docs,
    ids=ids
)

retriever = vector_store.as_retriever(search_kwargs = {'k':2})

query = "who is james dean?"
result = retriever.invoke(query)
print(result)
