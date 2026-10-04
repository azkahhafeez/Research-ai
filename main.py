from crew import create_crew


def main():
    topic = input("What would you like me to research? ")

    # We will connect your LLM here in the next step.
    llm = None

    crew = create_crew(llm, topic)

    result = crew.kickoff()

    print("\n===== RESEARCH RESULT =====\n")
    print(result)


if __name__ == "__main__":
    main()
