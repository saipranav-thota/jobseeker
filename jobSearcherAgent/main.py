import os
from crewai import Crew, Task, Process
from agent.JobScout_agent import JobScout
from task.JobScout_task import JobScout_task
from agent.investigator_agent import investigator
import time
from dotenv import load_dotenv

load_dotenv()

print("GEMINI_API_KEY: ", os.getenv("GEMINI_API_KEY"))

if __name__ == "__main__":

    job_crew = Crew(
    agents=[JobScout],
    tasks=[JobScout_task],
    verbose=True
    )
    scout_result = job_crew.kickoff()
    output_text = scout_result.raw
    job_urls = [url.strip() for url in output_text.split('\n') if url.strip()]

    time.sleep(60)

    for i, url in enumerate(job_urls):
        print(f"Extracting Jobs from link{i+1}")
        task_description = (
            f"Read and meticulously extract details from the job description at: {url}\n"
            "Extract the following: job title, company, location, and the url from where you can apply for the job."
            f"If a field is not explicitly found, leave it as an empty list or None as per the schema."
            f"Get at max 30 job postings. Once you have hit that number, stop agnet execution."
        )
        job_analysis_tasks = Task(
            description=task_description,
            agent=investigator,
            expected_output="A detailed job description extracted in a structured JSON format",
        )

        job_crew = Crew(
        agents=[investigator], 
        tasks=[job_analysis_tasks],
        process=Process.sequential,
        verbose=True
        )

        results_crew_output = job_crew.kickoff()
        print(results_crew_output)

        sleep_time = min(60 * (i + 1) * (i + 1), 300)
        print(f"⏳ Sleeping for {sleep_time} seconds to avoid API rate limits...")
        time.sleep(sleep_time)
        print(f"Next up: Extracting jobs from link: {i+2}")