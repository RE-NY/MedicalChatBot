import os
from dotenv import load_dotenv
from langchain.vectorstores import Pinecone
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
from flask import Flask, render_template, redirect, url_for, request

from src.prompt import *
from src.utils import download_hugging_face_embeddings_model

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')



embeddings = download_hugging_face_embeddings_model()


pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))

index_name = "medical-chatbot"

##Creating the retriever to retrieve from existing index.
docsearch = Pinecone.from_existing_index(index_name, embeddings)


## Final prompt template
medical_prompt_template=PromptTemplate(input_variables=["context", "question"], template=prompt_template)



## LLM used is imported from the model folder. It is a bin file downloaded from huggingface and loaded by
# using CTransformers library.
llm=CTransformers(model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
                  model_type="llama",
                  config={'max_new_tokens':512,
                          'temperature':0.75})


chain_type_kwargs={"prompt": medical_prompt_template}


## Initializing the retrievelQA chain. Notice the kwargs of retriever, the k value is used by k-nearest neighbour algorithm
## for sementic search and returns 'k' most relavent chunks from the namespace of index relavent to the question.
qa = RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    chain_type_kwargs=chain_type_kwargs,
    retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True
    )


@app.route("/")
def index():
    return render_template('index.html')



@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    
    result=qa({"query": input})
    print("Response : ", result["result"])
    return str(result["result"])
    



if __name__ == '__main__':
    app.run(debug= True)
