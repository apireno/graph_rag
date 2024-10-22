## About graph\_rag

This repository contains a Python implementation for creating a graph-based Retrieval-Augmented Generation (RAG) system. This implementation likely uses SurrealDB, a multi-model database that supports both graph and vector data structures, as its knowledge source.

## What is a Graph-based RAG System?

Retrieval-Augmented Generation (RAG) systems enhance language models by incorporating external knowledge sources during text generation. This specific RAG system leverages knowledge graphs to provide structured and semantically rich context, leading to more informed and coherent responses.

## SurrealDB: Leveraging Graph and Vector Capabilities

SurrealDB is a multi-model database that offers both graph and vector capabilities, which can be powerfully combined in a RAG system. 

- **Graph Capabilities**: SurrealDB allows you to store data as a graph, where entities are represented as nodes and their relationships are represented as edges. This enables the representation of complex, interconnected knowledge, which is ideal for knowledge graph construction.
- **Vector Capabilities**:  SurrealDB likely supports storing and querying vector embeddings. Vector embeddings are numerical representations of text or data, capturing semantic meaning. These embeddings facilitate semantic search and retrieval within the knowledge graph.

This demonstration leverages SurrealDB's features in the following ways:

1. **"graph\_extractor.ipynb"**: This notebook likely uses SurrealDB to store the extracted knowledge graph. Entities are stored as nodes, their relationships as edges, and potentially, vector embeddings of text are associated with nodes for semantic search.
2. **"graphRAG.ipynb"**:  This notebook uses the knowledge graph stored in SurrealDB to answer questions.  It likely performs semantic searches using vector embeddings to find relevant information within the knowledge graph. The graph structure is then traversed to retrieve connected entities and provide contextually rich answers.

## Key Components

This repository features two Jupyter notebooks:

### 1. "graph\_extractor.ipynb" - Knowledge Graph Construction

This notebook guides you through the process of building a knowledge graph from unstructured text data. The notebook likely covers:

- **Entity Recognition**: Identifying and extracting key entities like people, places, organizations, etc. 
- **Relation Extraction**: Discovering relationships between the identified entities. These relations form the edges of the knowledge graph, connecting the entities in a meaningful way.

### 2. "graphRAG.ipynb" - Building and Utilizing the RAG System

This notebook showcases how to implement and utilize the graph-based RAG system:

- **Leveraging the Knowledge Graph**: This component likely demonstrates how to use the knowledge graph created by  "graph\_extractor.ipynb" to answer questions. 
- **Question Answering**: The notebook illustrates how to query the RAG system with questions. The system then retrieves relevant information from the knowledge graph to generate comprehensive and contextually appropriate answers.

### 3. SurrealDB - A multi model database that will store the knowledge graph and use vector search for retrieval

The repository can be found here:
https://github.com/surrealdb/surrealdb

With detailed documentation here:

https://surrealdb.com/

Install SurrealDB:
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

### 4. "embedding_api.py" - A simple flask API that returns embeddings using the glove.6B.50d model

This API endpoint has one input (via GET or POST) called "text". It returns an array of floats[50]

Download the model here  https://www.kaggle.com/datasets/watts2/glove6b50dtxt and unpack it into the directory embedding_api

Start the service by running this command in a terminal:
```console
cd embedding_api
env FLASK_APP=embedding_api.py python -m flask --app embedding_api --debug run         
```

by default the service will run on http://127.0.0.1:5000/

You can test it by entering this in your browser http://127.0.0.1:5000/?text=some%20text%20to%20embed

## Getting Started

To understand and use the code in this repository, follow these steps:

1. **Execute "graph\_extractor.ipynb":** Begin by running this notebook to build the knowledge graph, which is a prerequisite for the RAG system.
2. **Execute "graphRAG.ipynb":**  After successfully creating the knowledge graph, proceed to this notebook to see how the RAG system is implemented and how it utilizes the knowledge graph for question answering.

## Languages Used 

This repository utilizes the following programming languages:

- Jupyter Notebook: Used for interactive code development and demonstration.
- Python: The primary language for implementing the core logic of the graph-based RAG system.
- SurrQL: the SQL flavor of SurrealDB

## Additional Notes

- **Microsoft/graphrag Repository:** The notebook is loosely based on a larger repository microsoft/graphrag. The microsoft/graphrag repository provides a more comprehensive, modular graph-based RAG system. This notebook focuses specifically on the knowledge graph construction aspect.
  
