from retriever.document_retriver import pdf_retriver , text_retriever
from embedding.embedding_model import embedding_model


data =pdf_retriver(r"src\data\large_text.txt")

print(data)

e_model =embedding_model()

emedding = e_model.encode(data)

print(emedding)

