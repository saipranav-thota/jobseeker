# Job Searcher Agent

A CrewAI-based job search aggregator that finds job search URLs across major job boards for various tech roles in India.

## Features

- Searches multiple job boards: LinkedIn, Indeed, Naukri, Glassdoor, Dice, Shine, and Wellfound
- Covers various tech roles: SDE, Data Science, Software Engineer, DevOps Engineer
- Uses Tavily Search API for web search capabilities
- Generates comprehensive lists of job search URLs

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   Create a `.env` file in the root directory with:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

3. **Run the application:**
   ```bash
   python main.py
   ```

## Project Structure

```
jobSearcherAgent/
├── agent/
│   ├── JobScout_agent.py      # Main job search agent
│   ├── dataAnalyst_agent.py   # Data analysis agent
│   └── investigator_agent.py  # Investigation agent
├── task/
│   ├── JobScout_task.py       # Job search task
│   ├── dataAnalyst_task.py    # Data analysis task
│   └── investigator_task.py   # Investigation task
├── tool/
│   └── webSearch_tool.py      # Tavily search tool
├── model.py                   # LLM configuration
├── main.py                    # Main execution file
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## How it Works

The JobScout agent uses the Tavily Search API to find job search URLs across major job boards. It systematically searches for different combinations of roles and websites to generate a comprehensive list of job search pages.

## Output

The agent generates a list of URLs pointing to job search result pages on various job boards, covering different tech roles and locations in India.

## Dependencies

- crewai: Multi-agent framework
- langchain-openai: OpenAI integration
- tavily-python: Web search API
- python-dotenv: Environment variable management
- pydantic: Data validation 