from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("dp_fibonacci_knapsack_problems.pdf")

docs = loader.load()

print(type(docs[0]))