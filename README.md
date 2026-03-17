# AI Software Development Assistant (Multi-Agent System)

## Objective :
The primary aim of this project is to build a conversational AI system that assists developers in writing, debugging, testing, and documenting code automatically. The system uses a multi-agent architecture where specialized AI agents collaborate to handle different stages of the software development lifecycle through natural language interactions.

---

## Overview :
This project is an AI-powered coding assistant that simulates a real-world development workflow. Instead of a single AI model handling everything, the system is divided into multiple intelligent agents, each responsible for a specific task.

The system takes a user query (e.g., "Create a Python function for binary search") and processes it through multiple stages such as code generation, debugging, testing, and documentation.

---

## System Architecture :

User Input  
↓  
Code Generation Agent  
↓  
Debug Agent  
↓  
Test Generation Agent  
↓  
Documentation Agent  
↓  
Final Output  

---

## Key Features :

- Multi-Agent AI Architecture  
- Natural Language to Code Generation  
- Automatic Bug Detection & Fixing  
- Unit Test Generation  
- Code Documentation Generation  
- Local LLM execution (no paid API required)  
- API-based deployment support  

---

## Technologies Used :

- Python  
- LangGraph (for multi-agent workflow orchestration)  
- LangChain (LLM integration framework)  
- Ollama (local LLM execution)  
- FastAPI (backend API deployment)  

---

ai-dev-assistant
│
├── agents
│   ├── code_agent.py
│   ├── debug_agent.py
│   ├── test_agent.py
│   └── docs_agent.py
│
├── graph
│   └── workflow.py
│
├── llm.py
├── main.py
├── api.py
└── README.txt

---

## Workflow Description :

1. **Code Agent** → Generates initial code from user input  
2. **Debug Agent** → Fixes errors and improves code quality  
3. **Test Agent** → Creates unit test cases  
4. **Documentation Agent** → Generates readable documentation  

Each agent updates the shared state and passes it to the next agent using a graph-based workflow.

---

## Installation & Setup :

### Step 1: Clone Repository

git clone <your-repo-link>
cd ai-dev-assistant


### Step 2: Create Virtual Environment

python -m venv venv
venv\Scripts\activate


### Step 3: Install Dependencies

pip install langchain langgraph langchain-community ollama fastapi uvicorn


### Step 4: Install Ollama
Download and install Ollama from:
https://ollama.com

### Step 5: Pull Model

ollama pull deepseek-coder


---

## Running the Project :

### Run CLI Assistant

python main.py


Example Input:

Create a Python function for binary search


---

### Run API Server

uvicorn api:api --reload


Open:

http://127.0.0.1:8000/docs


---

## Example Output :

- Generated Python Code  
- Unit Test Cases  
- Documentation  

---

## Future Improvements :

- Add more agents (Security, Code Review, Refactoring)  
- Integrate GitHub repository analysis  
- Add UI using Streamlit or React  
- Enable code execution sandbox  
- Add memory for conversational context  

---

## Final Model :
A fully functional Multi-Agent AI Software Development Assistant capable of automating key parts of the coding workflow using local AI models.

---

## Author :
Toran V Athani

