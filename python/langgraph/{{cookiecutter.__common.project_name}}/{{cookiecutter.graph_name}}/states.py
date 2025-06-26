"""States for the LangGraph agent."""

from typing import TypedDict

from langchain_core.messages import HumanMessage
from langgraph.graph import MessagesState


class InputState(MessagesState):
    """State for the input node. MUST only contain the messages of the thread."""
    example: str
    pass

class State(InputState):
    """This is the state that is both exposed to the input and is passed along to other nodes for the most part."""
    pass

class HiddenState(TypedDict):
    """This is the state that is hidden and can be passed along to other nodes for the most part."""
    input_message: list[HumanMessage]
    hidden_state: str

class OutputState(MessagesState):
    """This is the output state that is returned by the agent."""
    output: str
