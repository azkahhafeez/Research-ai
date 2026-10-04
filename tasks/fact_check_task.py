from crewai import Task


def create_fact_check_task(agent, research_output):
    return Task(
        description=f"""
        Fact-check the research below:

        {research_output}

        Verify the important claims using reliable sources.
        Look for incorrect, unsupported, outdated, or conflicting information.
        """,
        expected_output="""
        A fact-checking report containing:
        - Verified claims
        - Claims that need correction
        - Conflicting information
        - Reliable sources
        """,
        agent=agent,
    )
