from crewai import Agent
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()


def create_researcher(llm):
    return Agent(
        role="Web Researcher",
        goal="Find reliable and relevant information about the research topic.",
        backstory="You are an expert web researcher who carefully searches for useful evidence.",
        tools=[search_tool],
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )
