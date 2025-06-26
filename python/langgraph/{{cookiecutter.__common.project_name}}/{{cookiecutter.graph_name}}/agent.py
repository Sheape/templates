"""Main LangGraph Agent"""

from {{cookiecutter.graph_name}}.states import State
from {{cookiecutter.graph_name}}.config import Settings
from {{cookiecutter.graph_name}}.nodes import example_node

from langgraph.graph import END, START, StateGraph


builder = StateGraph(State, Settings)

builder.add_node("example_node", example_node)

builder.add_edge(START, "example_node")
builder.add_edge("example_node", END)

graph = builder.compile()
