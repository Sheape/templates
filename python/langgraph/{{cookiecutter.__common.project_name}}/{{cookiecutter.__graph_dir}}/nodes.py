"""Nodes for the LangGraph agent."""

from .states import InputState

def example_node(input: InputState):
    print(input.example)
    pass
