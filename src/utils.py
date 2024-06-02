from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings




## Function to extract data from pdf(load the pdf)
def load_pdf(data):                 #directory path as input
    loader = DirectoryLoader(data,
                             glob = "*.pdf", #glob specifies which type of files to include, we specified it using regex
                             loader_cls = PyPDFLoader)
    
    document = loader.load()
    return document

## Function to create text chunks based on sementic and other similarites
def text_split(loaded_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 200, chunk_overlap = 20)
    text_chunks = text_splitter.split_documents(loaded_data)

    return text_chunks

## Function to download the embedding model from huggingface
def download_hugging_face_embeddings_model():
    '''Downloads the all-MiniLM-L6-v2 embedding model from hugging face'''
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings


