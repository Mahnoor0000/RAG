# What are Retrievers?

A **retriever** is a component in LangChain that fetches **relevant documents** from a data source in response to a user's query.

There are multiple types of retrievers.

All retrievers in LangChain are **runnables**.


# Brief Types of Retrievers

## 1. Vector Store Retriever
Retrieves documents based on semantic similarity using embeddings and a vector store like Chroma, FAISS, Pinecone, etc.

## 2. Similarity Search Retriever
Finds documents most similar to the user's query.

## 3. MMR Retriever
Uses **Maximal Marginal Relevance** to return relevant but diverse documents, avoiding repeated information.

## 4. Multi-Query Retriever
Generates multiple versions of the user query and searches with all of them to improve retrieval.

## 5. Contextual Compression Retriever
Retrieves documents and then compresses or filters them to keep only the most relevant parts.

## 6. Parent Document Retriever
Stores small chunks for searching but returns the larger parent document for better context.

## 7. Self-Query Retriever
Uses an LLM to understand the query and apply metadata filters automatically.

## 8. Ensemble Retriever
Combines results from multiple retrievers, such as BM25 and vector search, to improve accuracy.

## 9. BM25 Retriever
A keyword-based retriever that searches using exact words instead of embeddings.