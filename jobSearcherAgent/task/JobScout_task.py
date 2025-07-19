from crewai import Task
from jobSearcherAgent.agent.JobScout_agent import JobScout

JobScout_task = Task(
    description=(
        "Search the web for 10 recent job listings for a {job_role} in {location}"
    ),
    expected_output=(
        "A list of unique URLs pointing directly to job description pages"
    ),
    agent=JobScout
)