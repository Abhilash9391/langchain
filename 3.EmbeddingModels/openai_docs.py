from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)

documents = [
    "paris is the capital of france",
    "delhi is the capital of india",
    "rome is the capital of italy"
]


vectors = embedding.embed_documents(documents)

print(str(vectors))