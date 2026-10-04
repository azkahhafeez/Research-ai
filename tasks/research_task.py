from crewai import Task


def create_research_task(agent, topic):
    return Task(
        description=f"""
        Research the following topic thoroughly:

        {topic}

        Find reliable information, identify the key facts,
        and provide useful sources for the final analysis.
        """,
        expected_output="""
        A detailed research report containing:
        - Key findings
        - Important facts
        - Reliable sources
        - Any conflicting or uncertain information
        """,
        agent=agent,
    )
