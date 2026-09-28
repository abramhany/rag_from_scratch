from PyPDF2 import PdfReader

def pdf_retriver(document):

    pages = []
    reader = PdfReader(document)
    for page in reader.pages:
        pages.append(page.extract_text())

    return pages


def text_retriever(text):
    with open(text,'r',encoding="utf-8") as file :
        lines = file.readlines()
    file.close()

    return lines