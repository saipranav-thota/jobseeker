# parse resume text 
import os
import json
import logging
from dotenv import load_dotenv 
from model import llm
from langchain_core.prompts import PromptTemplate
from extract_resume import extract_text_from_doc

# ✅ Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

load_dotenv()
logging.info("🔐 Loaded environment variables")

# Confirm LLM loaded
if llm:
    logging.info("✅ LLM loaded successfully")
else:
    logging.warning("⚠️ LLM is not loaded")

# Prompt definition
prompt = PromptTemplate(
    input_variables=["text"],
    template="""
    Extract this structured JSON from the resume text. Follow these rules strictly:
    - Output ONLY valid JSON.
    - If a field is missing in the resume, assign it an empty value like an empty string.
    - DO NOT include any explanation or text outside the JSON.
      "name": String,
      "summary": String,
      "skills": [String],
      "domains": [String],
      "education": [
        {{
          "degree": String
        }}
      ],
      "experience": [
        {{
          "company": String,
          "role": String,
          "duration": Number
        }}
      ],
      "languages": [String],
      "years_of_work_experience": Number
    }}
    Resume:
    {text}
    """
)

parse_resume_chain = prompt | llm

def parse_resume(text):
    logging.info("📄 Starting resume parsing")
    try:
        response = parse_resume_chain.invoke({"text": text}).content
        logging.info("✅ LLM response received")

        if response.startswith("```") and response.endswith("```"):
            logging.info("🧹 Stripping markdown code block from LLM response")
            response = "\n".join(response.split("\n")[1:-1])

        return json.loads(response)
    except json.JSONDecodeError:
        logging.error("❌ LLM returned non-JSON content:")
        logging.error(response)
        return None
    except Exception as e:
        logging.exception("❌ Unexpected error during parsing")
        return None


if __name__ == "__main__":
    logging.info("🚀 Resume parser started")

    resume_path = "resume.docx"
    if not os.path.exists(resume_path):
        logging.error(f"❌ Resume file not found at {resume_path}")
        exit(1)

    logging.info(f"📂 Extracting text from: {resume_path}")
    resume = extract_text_from_doc(resume_path)

    logging.info("🧠 Invoking resume parsing chain")
    parsed = parse_resume(resume)

    if parsed:
        logging.info("✅ Parsed Resume Output:")
        print(json.dumps(parsed, indent=2))
    else:
        logging.error("⚠️ Failed to parse resume")

    logging.info("🏁 Done.")
