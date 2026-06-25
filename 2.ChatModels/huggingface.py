from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task = "text-generation"
)


model = ChatHuggingFace(llm=llm)

result = model.invoke("Tell me the best 5 things to before going to sleep")

print(result.content)