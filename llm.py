from langchain_ollama import OllamaLLM

# Make sure this model is pulled locally with ollama pull deepseek-coder
llm = OllamaLLM(model="deepseek-coder")