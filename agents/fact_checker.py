from crewai import Agent
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()


def create_fact_checker(llm):
    return Agent(
        role="Fact Checker",
        goal="Verify important claims and identify unreliable or conflicting information.",
        backstory="You are a careful fact checker who verifies claims using reliable sources.",
        tools=[search_tool],
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )
