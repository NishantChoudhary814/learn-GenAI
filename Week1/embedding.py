from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

text = "Hello how are you? Tell my name?"

response = client.embeddings.create(
    input=text,
    model="text-embedding-3-small" #Vector Embedding model
)

print("Vector Embeddings :", response.data[0].embedding)