import numpy as np

def cosine_similarity(quary,embbeding):


    quary = np.array(quary)

    similarities = []

    if len(np.shape(embbeding)) == 1:
        embbeding = [embbeding]



    for embd in embbeding:

        embd = np.array(embd)

        dot_prodcut = np.dot(quary,embd)

        quary_norm = np.linalg.norm(quary)

        embbeding_norm = np.linalg.norm(embd)

        result = dot_prodcut / (quary_norm * embbeding_norm)

        similarities.append(result)

    return [float(x) for x in similarities]






