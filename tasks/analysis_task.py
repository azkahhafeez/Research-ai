from crewai import Task


def create_analysis_task(agent, research_task):
    return Task(
        description="""
        Analyze the research produced by the researcher.

        Identify the most important findings, compare the information,
        and produce a clear, logical analysis.
        """,
        expected_output="""
        A structured analysis containing:
        - Main conclusions
        - Supporting evidence
        - Important comparisons
        - Remaining uncertainties
        """,
        agent=agent,
        context=[research_task],
    )
