import streamlit as st
from backend.file_parser import extract_text_from_pdf, extract_text_from_ppt
from backend.summarizer import summarize_text
from backend.mindmap import generate_mindmap
from backend.qa_bot import create_qa_chain

st.set_page_config(page_title="\ud83d\udcda StudyBot", layout="wide")
st.title("\ud83d\udcd6 StudyBot - Your Study Companion")

uploaded_file = st.file_uploader("Upload a PDF or PPT file", type=["pdf", "pptx"])

if uploaded_file:
    if uploaded_file.name.endswith(".pdf"):
        text = extract_text_from_pdf(uploaded_file)
    else:
        text = extract_text_from_ppt(uploaded_file)

    st.subheader("\u2705 Summary")
    summary = summarize_text(text)
    st.markdown(summary)

    st.subheader("\ud83e\udde0 Mind Map")
    image_path = generate_mindmap(summary)
    st.image(image_path)

    st.subheader("\u2753 Ask a Question")
    qa_chain = create_qa_chain(text)
    query = st.text_input("Type your question below:")

    if query:
        response = qa_chain.run(query)
        st.success(response)
