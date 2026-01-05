from langchain_classic import hub
from langchain_classic.agents import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_tavily import TavilySearch

load_dotenv()


tools = [TavilySearch()]
llm = ChatOllama(model="qwen2.5:7b")
react_prompt = hub.pull("hwchase17/react")
agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=react_prompt
)

agent_executor = AgentExecutor(agent=agent,tools=tools,verbose=True)


def main():
    result = agent_executor.invoke(
        input={
            "input":"search for 3 job posting for an ai engineer using langchain in delhi on linkedin and list their details"
        }
    )
    print(result)


if __name__ == "__main__":
    main()
