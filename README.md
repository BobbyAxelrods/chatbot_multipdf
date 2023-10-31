# chatbot_multipdf+Scanner Features 
1. Chatbot accept multiple PDF - Done
2. Scanned pdf to chat - pending 2nd commit. 

**Introduction**

The MultiPDF Chat App is a Python application designed for engaging conversations with multiple PDF documents. You can inquire about the content of these PDFs using everyday language, and the application will provide relevant responses based on the document's text. It's essential to note that this app responds exclusively to questions related to the loaded PDFs.

**How It Works**

The MultiPDF Chat App operates through the following steps:

1. **PDF Loading:** The application reads and extracts text content from multiple PDF documents.
2. **Text Chunking:** Extracted text is divided into smaller, manageable chunks for more effective processing.
3. **Language Model:** The app employs a language model to create vector representations (embeddings) of the text chunks.
4. **Similarity Matching:** When you pose a question, the app compares it to the text chunks, identifying the most semantically relevant ones.
5. **Response Generation:** The chosen chunks are then processed by the language model, which generates a response based on the content of the PDFs.

**Dependencies and Installation**

To install the MultiPDF Chat App, please follow these steps:

1. Clone the repository to your local machine.
2. Install the necessary dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```
3. Acquire an API key from OpenAI and add it to the `.env` file located in the project directory. Your `.env` file should contain the following line:
   ```
   OPENAI_API_KEY=your_secret_api_key
   ```

**Usage**

To use the MultiPDF Chat App, please adhere to the following instructions:

1. Ensure you have installed the required dependencies and added the OpenAI API key to the `.env` file.
2. Run the `main.py` file using the Streamlit CLI. Execute the following command:
   ```
   streamlit run app.py
   ```
3. The application will open in your default web browser, revealing the user interface.
4. Load multiple PDF documents into the app as per the provided guidelines.
5. Engage in natural language conversations about the loaded PDFs using the chat interface.

Enjoy seamless interactions with your PDF documents using the MultiPDF Chat App!
