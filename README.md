## About graph\_rag

This repository contains a Python implementation for creating a graph-based Retrieval-Augmented Generation (RAG) system. This implementation likely uses SurrealDB, a multi-model database that supports both graph and vector data structures, as its knowledge source.

## What is a Graph-based RAG System?

Retrieval-Augmented Generation (RAG) systems enhance language models by incorporating external knowledge sources during text generation. This specific RAG system leverages knowledge graphs to provide structured and semantically rich context, leading to more informed and coherent responses.

## SurrealDB: Leveraging Graph and Vector Capabilities

SurrealDB is a multi-model database that offers both graph and vector capabilities, which can be powerfully combined in a RAG system. 

- **Graph Capabilities**: SurrealDB allows you to store data as a graph, where entities are represented as nodes and their relationships are represented as edges. This enables the representation of complex, interconnected knowledge, which is ideal for knowledge graph construction.
- **Vector Capabilities**:  SurrealDB likely supports storing and querying vector embeddings. Vector embeddings are numerical representations of text or data, capturing semantic meaning. These embeddings facilitate semantic search and retrieval within the knowledge graph.

This demonstration leverages SurrealDB's features in the following ways:

1. **"graph_extractor.ipynb"**: This notebook likely uses SurrealDB to store the extracted knowledge graph. Entities are stored as nodes, their relationships as edges, and potentially, vector embeddings of text are associated with nodes for semantic search.
2. **"chunking_and_embedding.ipynb"**: This notebook likely chunks the document for reduction of the input prompt tokens. The chunks are stored in SurrealDB with embeddings for semantic retreival. This is only needed for the Together AI hosted model due to context window restrictions.
3. **"gemini_graphRAG.ipynb"**:  This notebook uses the knowledge graph stored in SurrealDB and Gemini to answer questions.  It performs semantic searches using vector embeddings to find relevant information within the knowledge graph. The graph structure is then traversed to retrieve connected entities and provide contextually rich answers. 
4. **"deepseek_graphRAG.ipynb"**:  This notebook uses the knowledge graph stored in SurrealDB and a locally hosted deepseek R1 model to answer questions.  It performs semantic searches using vector embeddings to find relevant information within the knowledge graph. The graph structure is then traversed to retrieve connected entities and provide contextually rich answers. 
5. **"deepseek_togetherai_graphRAG.ipynb"**:  This notebook uses the knowledge graph stored in SurrealDB and a together AI (https://www.together.ai/) hosted deepseek R1 model to answer questions.  It performs semantic searches using vector embeddings to find relevant information within the knowledge graph. Due to context window restrictions it also uses chunking to limit the size of the tokens passed for the document text. The graph structure is then traversed to retrieve connected entities and provide contextually rich answers. 

### Installing SurrealDB - A multi model database that will store the knowledge graph and use vector search for retrieval

The repository can be found here:

https://github.com/surrealdb/surrealdb

With detailed documentation here:

https://surrealdb.com/

Install on MacOS:
```console
brew install surrealdb/tap/surreal

```
 Install on Linux
```console
curl --proto '=https' --tlsv1.2 -sSf https://install.surrealdb.com | sh

```
Install on Windows

```console
iwr https://windows.surrealdb.com -useb | iex
```
Starting the database:
```console
brew install surrealdb
surreal start --allow-net --log none --user root --pass root --bind 0.0.0.0:8080 "rocksdb:///<path to your project>/db"       
```

## Getting Started

To understand and use the code in this repository, follow these steps:

1. **Execute "graph_extractor.ipynb":** Begin by running this notebook to build the knowledge graph, which is a prerequisite for the RAG system.
2. **Execute "chunking_and_embedding.ipynb":**  After successfully creating the knowledge graph, proceed to this notebook to set up the chunking table.
2. **Execute the RAG example notebooks in no particular order:**  After successfully creating the knowledge graph, proceed to these notebooks to see how the RAG system is implemented and how it utilizes the knowledge graph for question answering.

## Languages Used 

This repository utilizes the following programming languages:

- Jupyter Notebook: Used for interactive code development and demonstration.
- Python: The primary language for implementing the core logic of the graph-based RAG system.
- SurrQL: the SQL flavor of SurrealDB

## Additional Notes

- **Microsoft/graphrag Repository:** The notebook is loosely based on a larger repository microsoft/graphrag. The microsoft/graphrag repository provides a more comprehensive, modular graph-based RAG system. This notebook focuses specifically on the knowledge graph construction aspect.
  
