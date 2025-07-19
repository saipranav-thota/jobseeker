from crewai import Task
from jobSearcherAgent.agent.investigator_agent import investigator

investigator_task = Task(
    description=(
        """For each URL provided, visit the page and extract the job title, 
            company name, location, and the full job description text."""
    ),
    expected_output=(
        """A list of JSON objects, with each object containing the raw, 
            unformatted data for one job listing"""
    ),
    context="This task will use output of JobScout_task as input",
    agent=investigator
)