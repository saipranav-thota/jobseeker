from ai_services.run_matcher import load_resume
from ai_services.mongo import get_data
from embeddings.vectordb import get_job_embeddings, load_and_upsert_job_data
from embeddings.utils import get_job_listings_by_ids
import os 
from dotenv import load_dotenv
import logging
from pymongo import MongoClient



load_dotenv(dotenv_path="jobSearcherAgent\.env")
logging.basicConfig(level=logging.INFO)


MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

try:
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db['user_data']
    logging.info("✅ MongoDB connection established successfully.")
except Exception as e:
    logging.error(f"❌ Failed to connect to MongoDB: {e}")
    collection = None

doc_id = load_resume("resume.docx")
document = get_data(doc_id)
domains = document['domains']
print(domains)

ids = get_job_embeddings(domains, 5)
collection = 'job_data'
get_job_listings_by_ids(ids, collection)
