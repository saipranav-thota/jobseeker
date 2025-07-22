import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from model import llm
from crewai import Agent
from tool.parser_tool import WebScrapingTool
from dotenv import load_dotenv

load_dotenv()

parser_tool = WebScrapingTool()

investigator =  Agent(
    role='Job Description Extractor',
    goal='Accurately extract structured information from job description URLs.',
    backstory="""You are a highly precise AI assistant specialized in parsing web pages
                to extract specific data fields from job postings. Your output must always conform
                to the specified JSON schema.""",
    verbose=True, 
    allow_delegation=False,
    tools=[parser_tool],
    llm=llm
)