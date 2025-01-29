# Copyright (c) 2024 
# Licensed under the MIT License

"""A file containing prompts definition."""

STD_RAG_PROMPT = """
-Goal-
You are a researcher who is providing answers to a question for you client based on documents provided you. Answer the questions to the best of your ability given the documents.

<question>
{question}
</question>

 """
GRAPH_RAG_PROMPT = """
-Goal-
You are a researcher who is providing answers to a question for your client based on documents provided you. You also have access to a knowledge graph based on the documents provided. Answer the questions to the best of your ability given the documents and knowledge graph.

<knowledge graph>
{knowledge_graph}
</knowledge graph>

<question>
{question}
</question>

 """



DEEPSEEK_TOGETHERAI_STD_RAG_PROMPT = """
-Goal-
You are a researcher who is providing answers to a question for your client based on documents provided you. Answer the questions to the best of your ability given the documents. The document text will be provided between the <documents> delimiters.

This is the data to respond to:
<documents>
{documents}
</documents>

 """
DEEPSEEK_TOGETHERAI_GRAPH_RAG_PROMPT = """
-Goal-
You are a researcher who is providing answers to a question for your client based on documents provided you. You also have access to a knowledge graph based on the documents provided. Answer the questions to the best of your ability given the documents and knowledge graph. The document text will be provided between the <documents> delimiters, the knowledge graph between the  <knowledge graph> delimiters.

This is the data to respond to:

<documents>
{documents}
</documents>
<knowledge graph>
{knowledge_graph}
</knowledge graph>

 """




DEEPSEEK_STD_RAG_PROMPT = """
-Goal-
You are a researcher who is providing answers to a question for your client based on documents provided you. Answer the questions to the best of your ability given the documents. The document text will be provided between the <document> delimiters and the prompt question between the <question> delimiters.

This is the data to respond to:
<documents>
{documents}
</documents>
<question>
{question}
</question>

 """
DEEPSEEK_GRAPH_RAG_PROMPT = """
-Goal-
You are a researcher who is providing answers to a question for your client based on documents provided you. You also have access to a knowledge graph based on the documents provided. Answer the questions to the best of your ability given the documents and knowledge graph. The document text will be provided between the <document> delimiters, the knowledge graph between the  <knowledge graph> delimiters, and the prompt question between the <question> delimiters.

This is the data to respond to:

<documents>
{documents}
</documents>
<knowledge graph>
{knowledge_graph}
</knowledge graph>
<question>
{question}
</question>

 """
