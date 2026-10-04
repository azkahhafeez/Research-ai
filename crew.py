from crewai import Crew

from agents.researcher import create_researcher
from agents.analyst import create_analyst
from agents.fact_checker import create_fact_checker

from tasks.research_task import create_research_task
from tasks.analysis_task import create_analysis_task
from tasks.fact_check_task import create_fact_check_task


def create_crew(llm, topic):
    researcher = create_researcher(llm)
    analyst = create_analyst(llm)
    fact_checker = create_fact_checker(llm)

    research_task = create_research_task(researcher, topic)
    analysis_task = create_analysis_task(analyst, research_task)
    fact_check_task = create_fact_check_task(fact_checker, research_task)

    return Crew(
        agents=[researcher, analyst, fact_checker],
        tasks=[research_task, analysis_task, fact_check_task],
        verbose=True,
    )
