from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuild import create_react_agent
from dotenv import load_dotenv

load_dotenv()

def main():
    # Initialize the LLM
    model = ChatOpenAI(model="gpt-4", temperature=0)

    # Create a REACT agent
    tools = []
    agent_executor = create_react_agent(model, tools)
    
    print("SOMETHING")
    
    while True:
        user_input = input("\nYou: ").strip()

        if user_input == "quit":
            break
        
        print("\nAssistant: ", end="")
    