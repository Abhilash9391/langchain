from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.runnables import RunnableParallel,RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)


prompt1 = PromptTemplate(
    template='generate a tweet about \n {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='generate a linkedin post about \n {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

chain = RunnableParallel({
    'tweet' : RunnableSequence(prompt1,model,parser),
    'linkedin' : RunnableSequence(prompt2,model,parser)
})

print(chain.invoke({'topic' : 'AI'}))