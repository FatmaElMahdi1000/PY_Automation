import streamlit as st
from pathlib import Path
import PyPDF2
import docx
import pandas as pd

st.title("📄 Word Count Tool")
uploaded_files = st.file_uploader("Upload files", accept_multiple_files=True)

def count_words(file, suffix):
    total_text = ""
    if suffix == ".txt":
        total_text = file.read().decode("utf-8")
    elif suffix == ".pdf":
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text = page.extract_text()
            if text: total_text += text + " "
    elif suffix in [".docx", ".doc"]:
        doc_file = docx.Document(file)
        for para in doc_file.paragraphs:
            total_text += para.text + " "
    elif suffix in [".xlsx", ".csv"]:
        if suffix == ".xlsx":
            df = pd.read_excel(file)
        else:
            df = pd.read_csv(file)
        total_text = " ".join(map(str, df.values.flatten()))
    return len(total_text.split())

if uploaded_files:
    total_wc = 0
    for file in uploaded_files:
        suffix = Path(file.name).suffix.lower()
        wc = count_words(file, suffix)
        st.write(f"**{file.name}** ➜ {wc} words")
        total_wc += wc
    st.success(f"✅ Total Word Count: {total_wc}")
