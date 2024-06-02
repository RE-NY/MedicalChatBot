## Making of prompt template for passing the context and question to LLM.

prompt_template="""
Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up any answer.

The Context is : {context}
The Question is : {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""