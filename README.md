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

## Getting Started

To understand and use the code in this repository, follow these steps:

1. **Execute "graph\_extractor.ipynb":** Begin by running this notebook to build the knowledge graph, which is a prerequisite for the RAG system.
2. **Execute "graphRAG.ipynb":**  After successfully creating the knowledge graph, proceed to this notebook to see how the RAG system is implemented and how it utilizes the knowledge graph for question answering.

## Languages Used 

This repository utilizes the following programming languages:

- Jupyter Notebook: Used for interactive code development and demonstration.
- Python: The primary language for implementing the core logic of the graph-based RAG system.
- SurQL: the SQL flavor of SurrealDB

## Additional Notes

- **Microsoft/graphrag Repository:** The notebook is loosely based on a larger repository microsoft/graphrag. The microsoft/graphrag repository provides a more comprehensive, modular graph-based RAG system. This notebook focuses specifically on the knowledge graph construction aspect.
  
