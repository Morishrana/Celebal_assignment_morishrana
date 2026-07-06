import streamlit as st

from chatbot import Chatbot
from vectorstore import VectorStore


def main():
    st.set_page_config(page_title="AI Question Answering Assistant", page_icon="AI", layout="centered")

    st.title("AI Question Answering Assistant")
    st.caption("Ask general questions or upload a PDF for document-based answers.")

    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    with st.sidebar:
        st.header("API Keys")
        cohere_api_key = st.text_input("Cohere API Key", type="password")
        pinecone_api_key = st.text_input("Pinecone API Key", type="password")
        st.caption("Pinecone is only required when you upload a PDF.")

    st.subheader("Ask a Question")
    uploaded_file = st.file_uploader("Upload a PDF (optional)", type="pdf")
    user_query = st.text_input(
        "Your question",
        placeholder="Example: Summarize this topic or explain a concept clearly.",
    )

    if st.button("Generate Answer", use_container_width=True) and user_query and cohere_api_key:
        vectorstore = None

        if uploaded_file:
            if not pinecone_api_key:
                st.error("A Pinecone API key is required when using PDF mode.")
                return

            with st.spinner("Processing PDF..."):
                with open("uploaded_document.pdf", "wb") as f:
                    f.write(uploaded_file.read())
                vectorstore = VectorStore("uploaded_document.pdf", cohere_api_key, pinecone_api_key)

        chatbot = Chatbot(vectorstore, cohere_api_key)

        with st.spinner("Generating response..."):
            response, retrieved_docs = chatbot.respond(user_query)
            st.session_state["chat_history"].append((user_query, response, retrieved_docs))

    if st.session_state["chat_history"]:
        st.divider()
        st.subheader("Conversation")
        for user_query, response, retrieved_docs in st.session_state["chat_history"]:
            st.markdown(f"**You**  \n{user_query}")

            accumulated_response = ""
            for event in response:
                if event.event_type == "text-generation":
                    accumulated_response += event.text

            st.markdown(f"**Assistant**  \n{accumulated_response}")


if __name__ == "__main__":
    main()
