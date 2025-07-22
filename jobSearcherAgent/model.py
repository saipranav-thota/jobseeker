import os
from dotenv import load_dotenv
from crewai import LLM
load_dotenv()

if not os.getenv("GEMINI_API_KEY"):
    raise ValueError("GEMINI_API_KEY environment variable is not set")

llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.7
)

if __name__ == "__main__":
    try:
        print("Testing LLM configuration...")
        print(f"Model: {llm.model}")
        print("✅ LLM Configuration Successful")
    except Exception as e:
        print(f"❌ LLM Configuration Failed: {str(e)}")