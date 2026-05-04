from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document
import os
import pdfplumber


def load_txt_doccument(file_path: str):
    loader = TextLoader(file_path, encoding="utf-8")
    documents = loader.load()
    return documents


def clean_text(text: str):
    # Remove extra whitespace and newlines
    if not text:
        return ""
    text = text.replace("\n", " ").replace("\r", " ")
    cleaned_text = " ".join(text.split())
    return cleaned_text


def process_pdf_document(file_path: str):
    documents = []
    with pdfplumber.open(file_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            cleaned_text = clean_text(text)
            if not cleaned_text.strip():
                continue

            lang_document = Document(
                page_content=cleaned_text, metadata={"page_number": i + 1}
            )
            documents.append(lang_document)
    return documents
