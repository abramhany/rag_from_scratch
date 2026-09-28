from sentence_transformers import SentenceTransformer

def embedding_model():

    model = SentenceTransformer("Qwen/Qwen3-Embedding-0.6B")

    
    return model