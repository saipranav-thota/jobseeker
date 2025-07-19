from crewai import Crew
from agent.JobScout_agent import JobScout
from task.JobScout_task import JobScout_task
from dotenv import load_dotenv

load_dotenv()


if __name__ == "__main__":
#Checking the JobScout agent
    job_crew = Crew(
    agents=[JobScout],
    tasks=[JobScout_task],
    verbose=True
    )

    result = job_crew.kickoff()

    print("\n\n########################")
    print("## Job Search Results:")
    print("########################\n")
    print(result)