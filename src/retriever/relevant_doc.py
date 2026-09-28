from embedding.embedding_model import embedding_model
from retriever.cosine_similarity import cosine_similarity

def relevant_doc(quary,documents,topk):


    e_model =embedding_model()

    docments_embedding = e_model.encode(documents)
    quary_embedding = e_model.encode(quary)

    distances = cosine_similarity(quary_embedding,docments_embedding)

    vals = [(doc, dist) for doc, dist in zip(documents, distances)]

    vals.sort(reverse=True,key=lambda x:x[1])

    docs= []

    for val in vals[:topk]:
        docs.append(val[0])

    return docs