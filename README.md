# Medical ChatBot with RAG
----
## Project Overview
The Medical ChatBot with RAG is an advanced AI-driven chatbot designed to provide medical information and support. By leveraging state-of-the-art models and technologies, this chatbot offers accurate and relevant responses to medical queries.

## Key Features
- **Hugging Face Embeddings Model**: Utilizes a pre-trained model from Hugging Face to generate high-quality word embeddings. These embeddings are stored in Pinecone, a vector database, enabling efficient long-term memory and retrieval of medical information.
- **Data Source**: The chatbot's knowledge base is built using the Gale Encyclopedia of Medicine, ensuring reliable and comprehensive medical information.
- **LLama-2-7b-chat Model**: Implements the Llama-2-7b-chat model from Hugging Face for generating natural and coherent responses to user queries.
- **Langchain Framework**: Utilizes the Langchain framework to implement the Retrieval-Augmented Generation (RAG) pipeline, combining information retrieval and response generation for improved accuracy and relevance.
- **Backend and Frontend**: Built with Flask for the backend and HTML for the frontend, providing a user-friendly interface for interacting with the chatbot.

## Technologies Used
- Hugging Face Models: For embedding generation and response generation.
- Pinecone: As a vector database for storing and retrieving embeddings.
- Langchain: For implementing the RAG pipeline.
- Flask: For creating a robust and scalable backend.
- HTML: For the frontend interface.

## Installation and Setup
1. Clone the Repository:
```bash
git clone https://github.com/yourusername/medical-chatbot-rag.git
cd medical-chatbot-rag
```
2. Install Dependencies:
```bash
pip install -r requirements.txt
```


## Usage
Enter your medical queries in the chat interface, and the chatbot will provide responses based on the Gale Encyclopedia of Medicine. The chatbot leverages embeddings and retrieval-augmented generation to offer accurate and contextually relevant answers.





