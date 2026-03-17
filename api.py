from fastapi import FastAPI
from pydantic import BaseModel
from graph.workflow import app

# Create FastAPI app
api = FastAPI()

# Request structure
class TaskRequest(BaseModel):
    task: str


# Root endpoint
@api.get("/")
def home():
    return {"message": "AI Software Development Assistant API is running"}


# Main AI endpoint
@api.post("/generate")
def generate_code(request: TaskRequest):

    result = app.invoke({"task": request.task})

    return {
        "generated_code": result.get("code"),
        "tests": result.get("tests"),
        "documentation": result.get("docs")
    }