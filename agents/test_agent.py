from llm import llm

def test_agent(state):

    code = state.get("code")

    prompt = f"Write unit tests for this code:\n{code}"

    tests = llm.invoke(prompt)

    state["tests"] = tests

    return state
