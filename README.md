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
3. Set Up Pinecone:
Create an account at Pinecone and obtain your API key.
Create a Pinecone index and note down the index name.

4. Configure Environment Variables:
Create a .env file in the root directory and add your Pinecone API key and index name.
```env
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX_NAME=your_pinecone_index_name
```
5. Run the Flask Application:
```bash
flask run
```
6. Access the ChatBot:
Open your web browser and go to <http://127.0.0.1:5000> to interact with the chatbot.

## Usage
Enter your medical queries in the chat interface, and the chatbot will provide responses based on the Gale Encyclopedia of Medicine. The chatbot leverages embeddings and retrieval-augmented generation to offer accurate and contextually relevant answers.

## Acknowledgments
- Hugging Face: For providing the models and tools.
- Pinecone: For the vector database.
- Langchain: For the RAG framework.
- Flask: For the web framework.
- Gale Encyclopedia of Medicine: For the data source.


