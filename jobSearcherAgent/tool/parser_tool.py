import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type



class WebScrapingInput(BaseModel):
    website_url: str = Field(..., description="The URL of the website to scrape.")

class WebScrapingTool(BaseTool):
    name: str = "Selenium Web Scraper"
    description: str = "Uses a headless Chrome browser to scrape the full HTML of a given URL."
    args_schema: Type[BaseModel] = WebScrapingInput

    def _run(self, website_url: str) -> str:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
        
        driver = None
        try:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            
            driver.get(website_url)
            
            time.sleep(5)
            
            html_content = driver.page_source
            
            return html_content if html_content else "Failed to retrieve HTML content."

        except Exception as e:
            return f"An error occurred during scraping: {e}"
        
        finally:
            if driver:
                driver.quit()

    def _arun(self, website_url: str):
        raise NotImplementedError("This tool does not support asynchronous execution.")

if __name__ == '__main__':
    test_url = "https://www.naukri.com/devops-engineer-jobs-in-india"
    
    scraper_tool = WebScrapingTool()
    
    tool_input = {"website_url": test_url}
    
    print(f"--- Scraping content from: {test_url} ---")
    
    results = scraper_tool.run(tool_input)
    
    print("\n\n###################################")
    print("##          HTML Content         ##")
    print("###################################\n")
    print(results[:3000]) 
    print("\n\n--- Scraping complete. ---")
