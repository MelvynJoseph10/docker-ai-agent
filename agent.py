from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
import subprocess

SYSTEM_PROMPT = """
You are a Docker Expert. You can explain things in 1-2 lines max.
You don't overthink, hallucinate or keep reasoning in a loop.
You Reason and Act according to user prompt
these are the things you do:
1/ You tell about errors (What went wrong, etc)
2/ You tell about the root cause (What was the cause likely)
3/ You tell about the fix or solution in short
"""

@tool
def show_running_containers():
    """Shows all running Docker containers"""
    result = subprocess.run(["docker", "ps"], capture_output=True, text=True)
    return result.stdout

@tool
def show_container_logs(container_name: str):
    """Shows logs for a specific Docker container"""
    result = subprocess.run(["docker", "logs", container_name], capture_output=True, text=True)
    return result.stdout

llm = ChatOllama(model="gemma4", temperature=0.8)
tools = [show_running_containers, show_container_logs]

agent = create_react_agent(llm, tools, prompt=SYSTEM_PROMPT)

user_input = input("Enter your message:\n")
response = agent.invoke({"messages": [{"role": "user", "content": user_input}]})
print(response["messages"][-1].content)