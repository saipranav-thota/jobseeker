from crewai import Task
from agent.JobScout_agent import JobScout

JobScout_task = Task(
    description=(
       
        "You must generate a comprehensive list of search URLs. All job postings should be from India only. Create a search query for every possible combination of the following inputs:\n"
        '"roles": ["Software Engineer", "Data Scientist", "Machine Learning Engineer", "Full Stack Developer", "DevOps Engineer"]'
        '"websites": ["https://www.linkedin.com/jobs","https://www.indeed.com","https://www.glassdoor.com/Job","https://www.monster.com/jobs","https://www.naukri.com"]'
        "For example, one query should be for 'SDE jobs in Bangalore on linkedin.com', another for 'Data Analyst jobs in Hyderabad on indeed.com', and so on, all fields are covered atleast once.\n"
        "Your final output must be a complete list of all these generated search page URLs, separated by newlines."
        "Get a maximum of only 20 links"
    ),
    expected_output=(
        "A list of at max 20 unique URLs pointing directly to job description pages"
    ),
    agent=JobScout
)