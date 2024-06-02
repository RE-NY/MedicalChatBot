import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore


from src.utils import load_pdf, text_split, download_hugging_face_embeddings_model




extracted_data = load_pdf("data_source/")

text_chunks = text_split(extracted_data)

embeddings = download_hugging_face_embeddings_model()



load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')


pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))

index_name = "medical-chatbot"

## If index with this name is not present then create it.
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=1536, 
        metric="cosine", 
        spec=ServerlessSpec(
            cloud="aws"#, 
            #region="us-east-1"
        ) 
    ) 


# ## Create a "namespace" section inside the index for efficient search(see documentation)
# ## Pinecone allows you to partition the records in an index into namespaces.(from documentation)
# namespace = "theory-book-contents"

## This captures all the embedding data and is later used to make retriever, for retrieval.
## The from_documents() function makes records in the index.
docsearch = PineconeVectorStore.from_documents(
    documents = text_chunks,
    index_name = index_name,
    embedding = embeddings
    #namespace = namespace 
)

