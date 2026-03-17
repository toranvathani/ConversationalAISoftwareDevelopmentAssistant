from llm import llm

def debug_agent(state):

    code = state.get("code")

    prompt = f"Fix bugs in this code:\n{code}"

    fixed = llm.invoke(prompt)

    state["code"] = fixed

    return state