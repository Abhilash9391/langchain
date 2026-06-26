from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)


research_paper = st.selectbox(
    "Select a Research Paper",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "YOLOv8: Real-Time Object Detection",
        "ResNet: Deep Residual Learning for Image Recognition",
        "CLIP: Learning Transferable Visual Models",
        "DALL·E 2",
        "AlphaGo",
        "Llama 3",
        "DeepSeek-R1"
    ]
)


style_input = st.selectbox(
    "Select Summary Style",
    [
        "Beginner",
        "Technical",
        "Academic",
        "Bullet Points",
        "Detailed Explanation"
    ]
)


length_output = st.selectbox(
    "Select Output Length",
    [
        "Short",
        "Medium",
        "Long"
    ]
)


template = PromptTemplate(
    template="""
You are an expert research assistant.

Summarize the research paper: "{paper_name}"

Requirements:
- Summary Style: {style}
- Output Length: {length}

The summary should include:
1. Main objective of the paper.
2. Key methodology used.
3. Important findings.
4. Advantages.
5. Limitations.
6. Real-world applications.
7. A concise conclusion.

Generate the summary in a clear and well-structured format.
""",
    input_variables=["paper_name", "style", "length"]
)

prompt = template.invoke({
    "paper_name" : research_paper ,
    "style" :  style_input,
    "length" : length_output

})

if st.button("Summarize"):
    result = model.invoke(prompt)
    st.write(result.content)

