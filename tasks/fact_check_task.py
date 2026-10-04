from crewai import Task


def create_fact_check_task(agent, research_task):
    return Task(
        description="""
        Fact-check the research produced by the researcher.

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
        context=[research_task],
    )
