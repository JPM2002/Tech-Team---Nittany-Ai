from openai import OpenAI
import numpy as np

client = OpenAI(api_key="<api key>")

#===== Creating an embedding with the openai api =======
# https://platform.openai.com/docs/guides/embeddings
response = client.embeddings.create(
    input="Your text string goes here",
    model="text-embedding-3-small"
)
# print(response.data[0].embedding)
# ======================================================



# ==== Use case example ======
query = "Who is the greatest basketball player of all time?"

resource1 = "Lebron james is likely the greatest NBA player of all time."
resource2 = "Messi is likely the greatest soccer player of all time"
resource3 = "RAG stands for Retrieval Augmented Generation"

query_embedding = client.embeddings.create(
        input=query,
        model="text-embedding-3-small"
    ).data[0].embedding

resource_responses = client.embeddings.create(
            input=[resource1, resource2, resource3],
            model="text-embedding-3-small"
    ).data

resource1_embedding = resource_responses[0].embedding
resource2_embedding = resource_responses[1].embedding
resource3_embedding = resource_responses[2].embedding

query = np.array(query_embedding)

resource1_embedding = np.array(resource1_embedding)
resource2_embedding = np.array(resource2_embedding)
resource3_embedding = np.array(resource3_embedding)

def cosine_simularity(A, B):
    return np.dot(A,B) / ( np.linalg.norm(A) * np.linalg.norm(B) )

simularity1 = cosine_simularity(query_embedding, resource1_embedding)
simularity2 = cosine_simularity(query_embedding, resource2_embedding)
simularity3 = cosine_simularity(query_embedding, resource3_embedding)

print(f"Simularity of query and resource1: {simularity1}")
print(f"Simularity of query and resource2: {simularity2}")
print(f"Simularity of query and resource3: {simularity3}")
