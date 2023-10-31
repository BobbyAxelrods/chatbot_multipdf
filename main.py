import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template
from langchain.llms import HuggingFaceHub

# 2. Function Section 

def get_pdf_text(files_uploaded):
    # empty list 
    text = ""
    # Read the files first
    for pdf in files_uploaded:
        files = PdfReader(pdf)
        # read the pages 1 by 1 in loop then extract it 
        for file in files.pages:
            text += file.extract_text()
    return text 
        
def get_chunk_text(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_chunk_ingest(chunk):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=chunk,embedding=embeddings)
    return vectorstore

def get_conversation(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm, # language model based on api key define,
        retriever=vectorstore.as_retriever(), # save 
        memory=memory 
    )

    return conversation_chain

def handle_user_input(user_question):
    response = st.session_state.conversation({'question':user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        # for odd numbers 
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}",message.content),unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}",message.content),unsafe_allow_html=True)

# 3. Main UI Section 

def main():
    #to access secrets 
    load_dotenv()
    st.set_page_config(page_title="Chatbot")

    # set the html files to be access here in main page 
    st.write(css,unsafe_allow_html=True)

    # set the session state to be None if it hasnt been initialized 

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    
    st.header("Sumaarize multi pdf") 
    user_question = st.text_input("Ask a question ")
    if user_question:
        handle_user_input(user_question)



    with st.sidebar:
        st.subheader("Your documents")
        files_uploaded = st.file_uploader("Upload your file here and we accept multiple files", accept_multiple_files=True )        
        if st.button("Process"): 
            with st.spinner("Reading "):
                # Here input multi function 
                # 1. extract text from multi pdf and concat into 1 variables 
                raw_text = get_pdf_text(files_uploaded)
                # 2. Chunck extracted text 
                chunk = get_chunk_text(raw_text)
                # 3. Ingest chunk into embdedding and vectorstore 
                vectorstore = get_chunk_ingest(chunk)
                
                # 4. Conversation history 
                st.session_state.conversation = get_conversation(vectorstore)


if __name__ == '__main__':
    main()