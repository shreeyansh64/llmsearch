from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from tavily import TavilyClient

load_dotenv()
tavily = TavilyClient()


@tool
def search(query : str) -> str:
    """
    Tool that searches over internet
    Args:
        query: The query to search for
    Returns:
        The search result
    """
    print(f"Searching for {query}")
    return tavily.search(query=query)

llm = ChatOllama(temperature=0, model="gpt-oss:20b")
tools = [search]
agent = create_agent(model=llm,tools=tools)

def main():
    print("Hello")
    result = agent.invoke({"messages": HumanMessage(content="What is the weather in tokyo")})
    print(result)
    


if __name__ == "__main__":
    main()
