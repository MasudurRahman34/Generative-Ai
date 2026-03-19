import os
from typing import TypedDict, List, Union
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


class AgentState(TypedDict):
    messages: List[Union[HumanMessage, AIMessage]]


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


def process(state: AgentState) -> AgentState:
    response = llm.invoke(state["messages"])

    state["messages"].append(AIMessage(content=response.content))
    print(f"\nAi:{response.content}")
    print("Current state: ", state["messages"])
    return state


graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)

agent = graph.compile()

conversation_history = []
user_input = input("You :")

while user_input != "exit":
    conversation_history.append(HumanMessage(content=user_input))
    result = agent.invoke({"messages": conversation_history})
    conversation_history = result["messages"]
    user_input = input("You: ")

with open("logging.txt", "w") as file:
    file.write("Your conversation Log:\n")

    for messages in conversation_history:
        if isinstance(messages, HumanMessage):
            file.write(f"You:{messages.content}\n")
        elif isinstance(messages, AIMessage):
            file.write(f"Ai: {messages.content}\n\n")
    file.write("End of the converstation")

print("Conversation save to the logging.txt")
