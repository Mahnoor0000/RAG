# Vector Store

A **vector store** is a system designed to store and retrieve data represented as **numerical vectors**.

## Key Features

1. **Storage**  
   Ensures that vectors and their associated metadata are retained, whether in-memory for quick lookups or on-disk for durability and large-scale use.

2. **Similarity Search**  
   Helps retrieve the vectors most similar to a query vector.

3. **Indexing**  
   Provides a data structure or method that enables fast similarity searches on high-dimensional vectors, e.g., approximate nearest neighbor lookups.

4. **CRUD Operations**  
   Manages the lifecycle of data:
   - Adding new vectors
   - Reading them
   - Updating existing entries
   - Removing outdated vectors

## Use Cases

1. Semantic Search  
2. RAG  
3. Recommender Systems  
4. Image / Multimedia Search




# Vector Store vs Vector Database

## Vector Store

- Typically refers to a lightweight library or service that focuses on storing vectors/embeddings and performing similarity search.

- May not include many traditional database features like:
  - Transactions
  - Rich query languages
  - Role-based access control

- Ideal for prototyping and smaller-scale applications.

- Example:
  - **FAISS**: You can store vectors and query them by similarity, but you handle persistence and scaling separately.

## Vector Database

- A full-fledged database system designed to store and query vectors.

- Offers additional database-like features:

  - Distributed architecture for horizontal scaling
  - Durability and persistence, such as replication and backup/restore
  - Metadata handling, such as schemas and filters
  - Potential for ACID or near-ACID guarantees
  - Authentication, authorization, and more advanced security

- Geared for production environments with significant scaling and large datasets.




# Vector Stores in LangChain

## Key Points

- **Supported Stores:**  
  LangChain integrates with multiple vector stores such as **FAISS, Pinecone, Chroma, Qdrant, Weaviate**, etc., giving you flexibility in scale, features, and deployment.

- **Common Interface:**  
  A uniform **Vector Store API** lets you swap out one backend, such as **FAISS**, for another, such as **Pinecone**, with minimal code changes.

- **Metadata Handling:**  
  Most vector stores in LangChain allow you to attach metadata, such as timestamps or authors, to each document, enabling filter-based retrieval.

## Common Methods

```python
from_documents(...) or from_texts(...)

add_documents(...) or add_texts(...)

similarity_search(query, k=...)