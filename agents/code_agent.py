from llm import llm

def code_agent(state):

    task = state.get("task")

    prompt = f"Write a Python function for this task:\n{task}"

    code = llm.invoke(prompt)

    state["code"] = code

    return state