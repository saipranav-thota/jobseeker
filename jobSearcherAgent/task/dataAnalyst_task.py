from crewai import Task
from jobSearcherAgent.agent.dataAnalyst_agent import dataAnalyst

dataAnalyst_task = Task(
    description=(
        """ake the list of raw job details, clean them up, and format them 
        into a standardized schema. Standardize the location, infer the posting 
        date if possible, and extract 5-10 key skills or technologies from the 
        description. Finally, save each processed job listing"""
    ),
    expected_output=(
        """A success message confirming that the cleaned job listings 
            have been saved to the designated file (e.g., jobs.json)"""
    ),
    context="This task will take output of investigator_task as input",
    agent=dataAnalyst
)