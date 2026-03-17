from langgraph.graph import StateGraph, END

from agents.code_agent import code_agent
from agents.debug_agent import debug_agent
from agents.test_agent import test_agent
from agents.docs_agent import docs_agent

# Create graph
workflow = StateGraph(dict)

# Add nodes
workflow.add_node("code", code_agent)
workflow.add_node("debug", debug_agent)
workflow.add_node("test", test_agent)
workflow.add_node("docs", docs_agent)

# Entry point
workflow.set_entry_point("code")

# Flow
workflow.add_edge("code", "debug")
workflow.add_edge("debug", "test")
workflow.add_edge("test", "docs")
workflow.add_edge("docs", END)

# Compile
app = workflow.compile()
