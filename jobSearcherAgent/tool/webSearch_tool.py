import os
from tavily import TavilyClient
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class TavilySearchToolInput(BaseModel):
    query: str = Field(..., description="The search query to find job postings on the web.")

class TavilySearchTool(BaseTool):
    name: str = "Tavily Job URL Search"
    description: str = (
        "A tool that uses the Tavily Search API to find and return a list of URLs "
        "based on a search query. It is ideal for finding the web addresses of "
        "job postings. The output is a newline-separated list of URLs."
    )
    args_schema: Type[BaseModel] = TavilySearchToolInput

    def _run(self, query: str) -> str:
        try:
            api_key = os.getenv("TAVILY_API_KEY")
            if not api_key:
                return "Error: TAVILY_API_KEY environment variable not set."

            client = TavilyClient(api_key=api_key)
            response = client.search(query=query, search_depth="basic", max_results=7)

            if not response.get('results'):
                return f"No results found for the query: '{query}'"

            urls = [result.get('url') for result in response['results'] if result.get('url')]
            if not urls:
                return f"No URLs found in the results for the query: '{query}'"

            return "\n".join(urls)
        except Exception as e:
            return f"An error occurred during the search: {e}"

    def _arun(self, query: str):
        raise NotImplementedError("Asynchronous version of this tool is not available.")
