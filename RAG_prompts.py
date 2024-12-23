# Copyright (c) 2024 
# Licensed under the MIT License

"""A file containing prompts definition."""

STD_RAG_PROMT = """
-Goal-
You are a researcher who is providing answers to a question for you client based on documents provided you. Answer the questions to the best of your ability given the documents.

<question>
{question}
</question>

 """
GRAPH_RAG_PROMT = """
-Goal-
You are a researcher who is providing answers to a question for you client based on documents provided you. You also have access to a knowledge graph based on the documents provided. Answer the questions to the best of your ability given the documents and knowledge graph.

<knowledge graph>
{knowledge_graph}
</knowledge graph>

<question>
{question}
</question>

 """

