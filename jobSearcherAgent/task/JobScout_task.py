from crewai import Task
from agent.JobScout_agent import JobScout

JobScout_task = Task(
    description=(
       
        "You must generate a comprehensive list of search URLs. All job postings should be from India only. Create a search query for every possible combination of the following inputs:\n"
        "'roles': ['SDE', 'Data Science', 'Software Engineer', 'DevOps Engineer']"
        "'websites': ['linkedin.com', 'naukri.com', 'glassdoor.co.in', 'Shine.com']"
        "For example, one query should be for 'SDE jobs in Bangalore on linkedin.com', another for 'Data Analyst jobs in Hyderabad on indeed.com', and so on, all fields are covered atleast once.\n"
        "Your final output must be a complete list of all these generated search page URLs, separated by newlines."
    ),
    expected_output=(
        "A list of at max 9 unique URLs pointing directly to job description pages"
    ),
    agent=JobScout
)