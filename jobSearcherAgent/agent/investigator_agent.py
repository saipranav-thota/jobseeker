from model import llm
from crewai import Agent


investigator = Agent(
    role="Lead Investigator & Data Extractor",
    goal="To visit each provided URL, scrape its content, and extract the raw, unstructured job details like title, company name, location, and the full job description.",
    backstory=(
        """You are a meticulous investigator who can cut through the noise of website 
            layouts, ads, and boilerplate text. You are equipped with tools to parse HTML 
            and precisely pull out the specific pieces of information you've been tasked 
            to find, no matter how deeply they are buried in the code"""
    ),
    verbose=2,
    tools=[],
    llm=llm
)