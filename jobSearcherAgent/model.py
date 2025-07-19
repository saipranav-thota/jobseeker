import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

llm = LLM(
    model="gemini/gemini-2.5-pro",
    api_key=api_key,
    temperature=0.3
)

if __name__ == "__main__":
    if llm:
        print("Connections Sucessfull")
        print(api_key)
    else:
        print("Connection Unsucessfull")