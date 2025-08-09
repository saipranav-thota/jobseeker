import os
os.environ["OTEL_SDK_DISABLED"] = "true"  # Disable telemetry

from crewai import Agent, Task, Crew, Process
from model import llm

# --- 1. Create a test agent ---
test_agent = Agent(
    role="Test Agent",
    goal="Verify LLM is working in CrewAI",
    backstory="This is just a health check agent to confirm CrewAI + LLM setup works.",
    verbose=True,
    llm=llm
)

# --- 2. Define a simple task ---
test_task = Task(
    description="Just say 'Hello World' and nothing else.",
    agent=test_agent,
    expected_output="The phrase 'Hello World'"
)

# --- 3. Create a crew ---
test_crew = Crew(
    agents=[test_agent],
    tasks=[test_task],
    process=Process.sequential,
    verbose=True
)

# --- 4. Run the crew ---
if __name__ == "__main__":
    try:
        result = test_crew.kickoff()
        print("\n✅ CrewAI LLM Test Successful!")
        print("LLM Output:", result.raw if hasattr(result, 'raw') else result)
    except Exception as e:
        print("\n❌ CrewAI LLM Test Failed!")
        print("Error:", str(e))
