from crewai import Task


def create_analysis_task(agent, research_output):
    return Task(
        description=f"""
        Analyze the research provided below:

        {research_output}

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
    )
