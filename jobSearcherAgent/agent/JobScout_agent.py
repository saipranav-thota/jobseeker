import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from dotenv import load_dotenv
from model import llm
from crewai import Agent
from tool.webSearch_tool import TavilySearchTool
load_dotenv()

search_tool = TavilySearchTool()



JobScout = Agent(
    role='Job Search Aggregator Scout',
    goal='Find URLs for job search result pages on major job boards for various tech roles across major Indian cities.',
    backstory=(
        "An expert web researcher who finds the main entry points for job searches "
        "on major platforms. You are given a list of roles and cities and must find "
        "search pages that cover these criteria."
    ),
    tools=[search_tool],
    verbose=True,
    allow_delegation=False,
    llm=llm
)