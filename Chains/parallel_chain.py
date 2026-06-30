from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task = "text-generation"
)

prompt1 = PromptTemplate(
    template='Generate a detailed report on  {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a quiz which contains 5 questions that test the basic understanding of the  {topic}',
    input_variables=['topic']
)

prompt3 = PromptTemplate(
    template='merge the following notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes','quiz']

)
model = ChatHuggingFace(llm = llm)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes' : prompt1 | model | parser,
    'quiz' : prompt2 | model | parser
})

merge_chain = prompt3 | model | parser

chain = parallel_chain | merge_chain

result = chain.invoke({'topic' : 'trading'})

print(result)

chain.get_graph().print_ascii()

