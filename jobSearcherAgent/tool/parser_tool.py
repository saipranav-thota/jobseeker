import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type

# --- Instructions ---
# This script requires the 'selenium' and 'webdriver-manager' packages.
# Install them from your terminal:
# pip install selenium webdriver-manager

# 1. Define the Input Schema for the Tool
class WebScrapingInput(BaseModel):
    """Input for the Selenium Scraping Tool."""
    website_url: str = Field(..., description="The URL of the website to scrape.")

# 2. Define the Custom Tool
class WebScrapingTool(BaseTool):
    """
    A tool that uses Selenium to scrape the full HTML content of a webpage,
    including content loaded with JavaScript. It's more robust for modern,
    dynamic websites.
    """
    name: str = "Selenium Web Scraper"
    description: str = "Uses a headless Chrome browser to scrape the full HTML of a given URL."
    args_schema: Type[BaseModel] = WebScrapingInput

    def _run(self, website_url: str) -> str:
        """Use the tool to scrape a website."""
        # Set up Selenium WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
        
        driver = None
        try:
            # Initialize the driver
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            
            # Navigate to the URL
            driver.get(website_url)
            
            # Wait for dynamic content to load
            time.sleep(5)
            
            # Get the page source
            html_content = driver.page_source
            
            return html_content if html_content else "Failed to retrieve HTML content."

        except Exception as e:
            return f"An error occurred during scraping: {e}"
        
        finally:
            # Ensure the browser is closed
            if driver:
                driver.quit()

    def _arun(self, website_url: str):
        """Asynchronous version is not implemented."""
        raise NotImplementedError("This tool does not support asynchronous execution.")

# 3. Test Block to run the tool directly
if __name__ == '__main__':
    # Define the target URL
    test_url = "https://www.naukri.com/devops-engineer-jobs-in-india"
    
    # Instantiate the tool
    scraper_tool = WebScrapingTool()
    
    # Prepare the input
    tool_input = {"website_url": test_url}
    
    print(f"--- Scraping content from: {test_url} ---")
    
    # Run the tool
    results = scraper_tool.run(tool_input)
    
    print("\n\n###################################")
    print("##          HTML Content         ##")
    print("###################################\n")
    print(results[:3000]) 
    print("\n\n--- Scraping complete. ---")
