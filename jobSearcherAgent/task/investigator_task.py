from crewai import Task
from agent.investigator_agent import investigator

investigator_task = Task(
    description=(
        f"Read and meticulously extract details from the job description the job details\n"
        "Extract the following: job title, company, location, and the url from where you can apply for the job."
        f"If a field is not explicitly found, leave it as an empty list or None as per the schema."
        f"Get at max 30 job postings. Once you have hit that number, stop agnet execution."
        ),
    expected_output="A json type result of individual job postings found on the page.",
    agent=investigator
)