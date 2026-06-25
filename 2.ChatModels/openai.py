from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

model = ChatOpenAI(model='gpt-4',temperature=1.5)
#if normal deterministic tasks bring temperature close to 0 if creative task bring near 1.5

result = model.invoke("Describe the pros and cons if the same hyderabad located on the sea side ")

print(result)