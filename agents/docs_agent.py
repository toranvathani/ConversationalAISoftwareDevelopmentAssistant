from llm import llm

def docs_agent(state):

    code = state.get("code")

    prompt = f"Write documentation for this code:\n{code}"

    docs = llm.invoke(prompt)

    state["docs"] = docs

    return state