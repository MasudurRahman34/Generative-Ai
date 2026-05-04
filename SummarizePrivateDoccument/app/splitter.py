from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)
    return texts

def split_pdf_documents(pages):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, separators=["\n\n", "\n", " ", ""])
    chunks=text_splitter.split_documents(pages)
    return chunks

    
