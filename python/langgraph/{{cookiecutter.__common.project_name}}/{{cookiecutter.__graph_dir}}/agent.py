"""Main LangGraph Agent"""

from .states import State
from .config import Settings
from .nodes import example_node

from langgraph.graph import END, START, StateGraph


builder = StateGraph(State, Settings)

builder.add_node("example", example_node)

builder.add_edge(START, "example")
builder.add_edge("example", END)

graph = builder.compile()
