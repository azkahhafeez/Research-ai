from crewai import Agent
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()


def create_analyst(llm):
    return Agent(
        role="Research Analyst",
        goal="Analyze research findings and identify patterns, disagreements, and gaps.",
        backstory="You are a careful research analyst who turns raw research into structured findings.",
        tools=[search_tool],
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )
