import os
os.environ["OTEL_SDK_DISABLED"] = "true"  
from crewai import Crew, Task, Process
from agent.JobScout_agent import JobScout
from task.JobScout_task import JobScout_task
from agent.investigator_agent import investigator
import logging
import time
from dotenv import load_dotenv
from utils.parser import parse_to_json
from utils.mongo import load_data, get_data, update_data


load_dotenv()
logging.basicConfig(level=logging.INFO)


print("GEMINI_API_KEY: ", os.getenv("GEMINI_API_KEY"))

if __name__ == "__main__":

    job_crew = Crew(
    agents=[JobScout],
    tasks=[JobScout_task],
    verbose=True
    )
    scout_result = job_crew.kickoff()
    output_text = scout_result.raw
    print("Successfully extracted job urls")
    job_urls = [url.strip() for url in output_text.split('\n') if url.strip()]

    time.sleep(90)

    for i, url in enumerate(job_urls):
        print(f"Extracting Jobs from link {i+1}")

        try:
            task_description = (
                f"Read and meticulously extract details from the job description at: {url}\n"
                "Extract the following: job title, company, location, and the url from where you can apply for the job."
                f"If a field is not explicitly found, leave it as an empty list or None as per the schema."
                f"Get at max 30 job postings. Once you have hit that number, stop agent execution."
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

            # Run CrewAI process
            results_crew_output = job_crew.kickoff()

            # Parse and load results
            load_data(parse_to_json(results_crew_output.raw))

        except Exception as e:
            # Log the error and skip this URL
            print(f"❌ Error while processing link {i+1}: {url}")
            print(f"   Reason: {e}")
            print("⚠️ Skipping to next job link...\n")
            continue  # Move to the next URL

        # Sleep logic (only if no exception)
        sleep_time = 90
        print(f"⏳ Sleeping for {sleep_time} seconds to avoid API rate limits...")
        time.sleep(sleep_time)
        print(f"Next up: Extracting jobs from link: {i+2}")
