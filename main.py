from typing import List

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch
from pydantic import BaseModel, Field

load_dotenv()


class Source(BaseModel):
    """Schema for the source used by the agent"""

    url: str = Field(description="URL of the source")


class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""

    answer: str = Field(description="The agent's answer to to query")
    sources: List[Source] = Field(
        default_factory=list, description="List of sources used to generate the answer"
    )


llm = ChatOllama(model="gpt-oss:20b")
tools = [TavilySearch()]
agent = create_agent(
    model=llm,
    tools=tools,
    response_format=ToolStrategy(
        schema=AgentResponse,
        tool_message_content="Structured response generated successfully",
    ),
)


def main():
    print("Hello")
    result = agent.invoke(
        {"messages": [HumanMessage(content="What is the weather in tokyo")]}
    )
    print(result)


if __name__ == "__main__":
    main()
