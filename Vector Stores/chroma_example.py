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

doc3 = Document(
    page_content="In East of Eden, James Dean played Cal Trask, a troubled young man searching for love and acceptance from his father. His performance showed his natural acting style and emotional depth.",
    metadata={"topic": "film"}
)

doc4 = Document(
    page_content="James Dean was known for his unique style, including jeans, plain white T-shirts, leather jackets, and a cool but sensitive personality. His fashion became an important part of his image.",
    metadata={"topic": "style"}
)

doc5 = Document(
    page_content="James Dean died in a car accident at the age of 24. Even though he appeared in only a few major films, his legacy continued to influence actors, fashion, and popular culture.",
    metadata={"topic": "legacy"}
)

docs = [doc1, doc2, doc3, doc4, doc5]

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

# Add documents with fixed IDs
ids = ["doc1", "doc2", "doc3", "doc4", "doc5"]

vector_store.add_documents(
    documents=docs,
    ids=ids
)

# View documents
output = vector_store.get(include=["documents", "metadatas"])
print(output)

# Similarity search
results = vector_store.similarity_search(
    query="What made James Dean famous?",
    k=2
)

print("\nSimilarity Search Results:")
for result in results:
    print(result.page_content)
    print(result.metadata)
    print()

# Similarity search with score
results = vector_store.similarity_search_with_score(
    query="Why is James Dean remembered as a cultural icon?",
    k=2
)

print("\nSimilarity Search With Score:")
for doc, score in results:
    print("Score:", score)
    print(doc.page_content)
    print(doc.metadata)
    print()

# Metadata filtering
results = vector_store.similarity_search_with_score(
    query="Tell me about James Dean movies",
    k=2,
    filter={"topic": "film"}
)

print("\nMetadata Filter Results:")
for doc, score in results:
    print("Score:", score)
    print(doc.page_content)
    print(doc.metadata)
    print()

# Update document
updated_doc1 = Document(
    page_content="James Dean was a famous American actor whose short career left a lasting mark on cinema. He became a symbol of youth, rebellion, sensitivity, and emotional honesty in acting.",
    metadata={"topic": "biography"}
)

vector_store.update_document(
    document_id="doc1",
    document=updated_doc1
)

# Delete document
vector_store.delete(ids=["doc1"])