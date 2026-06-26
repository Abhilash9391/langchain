# LangChain Models Demo

This repository contains a collection of demo scripts demonstrating the usage of various Large Language Models (LLMs) and Chat Models through the [LangChain](https://www.langchain.com/) framework.

## Overview

The project includes example scripts for interacting with:
- OpenAI (GPT models)
- Anthropic (Claude models)
- Google (Gemini/PaLM models)
- Hugging Face (Hosted and local models)

Each script demonstrates how to initialize the model, set parameters (like temperature), and invoke the model with a sample prompt.

## Folder Structure

```
.
├── 1.LLMs/
│   └── demo.py               # Example using LLMs (legacy LangChain LLM interface)
├── 2.ChatModels/
│   ├── anthropic.py          # Anthropic Claude chat model
│   ├── google.py             # Google Gemini chat model
│   ├── huggingface.py        # Hugging Face hosted models
│   ├── huggingface_local.py  # Hugging Face local models
│   └── openai.py             # OpenAI chat model
├── 3.EmbeddingModels/
│   ├── huggingface_local.py  # Hugging Face local embeddings
│   ├── openai_docs.py        # OpenAI embeddings for document processing
│   └── openai_query.py       # OpenAI embeddings for query processing
├── Prompts/
│   ├── chatbot.py            # Interactive chatbot with prompt templates
│   ├── dynamic_prompt_ui.py  # Dynamic prompt tuning with UI
│   ├── messages.py           # Message prompt templates examples
│   └── static_prompt_ui.py   # Static prompt templates with UI
├── .env                      # Environment variables for API keys
├── requirements.txt          # Python dependencies
├── test.py                   # Simple test to check LangChain version
└── README.md
```

## Setup

1. **Clone the repository** (if you haven't already)
2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up environment variables**:
   Copy the `.env` file and fill in your API keys for the services you wish to use.
   ```bash
   cp .env.example .env   # If you have an example file
   # Or edit .env directly
   ```
   The `.env` file should contain:
   ```
   OPENAI_API_KEY="your-openai-api-key"
   ANTHROPIC_API_KEY="your-anthropic-api-key"
   GOOGLE_API_KEY="your-google-api-key"
   HUGGINGFACEHUB_API_TOKEN="your-huggingface-token"
   ```

## Usage

Run any of the example scripts to see the model in action. For example:

```bash
python 2.ChatModels/openai.py
python 2.ChatModels/anthropic.py
python 3.EmbeddingModels/openai_query.py
python Prompts/chatbot.py
```

Each script will print the model's response to a sample prompt.

### Running the Test

To verify your LangChain installation, run:
```bash
python test.py
```
This will print the installed LangChain version.

## Requirements

See `requirements.txt` for the full list. The main packages are:
- `langchain` and `langchain-core`
- Integration packages: `langchain-openai`, `langchain-anthropic`, `langchain-google-genai`, `langchain-huggingface`
- Supporting packages: `openai`, `anthropic`, `google-generativeai`, `transformers`, `huggingface-hub`, `python-dotenv`, `numpy`, `scikit-learn`

## Notes

- The scripts are for educational purposes and demonstrate basic usage.
- For production use, consider error handling, rate limiting, and secure management of API keys.
- Some models (especially Hugging Face local models) may require significant computational resources.

## Future Work
- Embedding models

