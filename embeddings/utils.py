from dotenv import load_dotenv
from pymongo import MongoClient
from bson.objectid import ObjectId
import os
import logging

load_dotenv(dotenv_path="jobSearcherAgent\.env")
logging.basicConfig(level=logging.INFO)


MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

try:
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    logging.info("✅ MongoDB connection established successfully.")
except Exception as e:
    logging.error(f"❌ Failed to connect to MongoDB: {e}")
    collection = None

def get_all_job_listings():
    if collection is None:
        return []
    try:
        documents = list(collection.find({},
                                            {"_id":1, 
                                             "job_title": 1}))
        return documents
    except:
        logging.error(f"❌ Failed to fetch job listings: {e}")
        return []
    

def get_job_listings_by_ids(ids: list, COLLECTION_NAME):
    collection = db[COLLECTION_NAME]
    required_keys = ['job_title', 'company', 'location', 'apply_url']
    for id in ids:
        try:
            object_id = ObjectId(id)
            posting = collection.find_one({"_id": object_id})
            if not posting:
                continue
            missing_keys = [key for key in required_keys if key not in posting]

            if missing_keys:
                continue 
            print(f"Job Title: {posting['job_title']}")
            print(f"Company: {posting['company']}")
            print(f"Location: {posting['location']}")
            print(f"Apply At: {posting['apply_url']}")
            print("*"*60)
        except Exception as e:
            continue

if __name__ == "__main__":
    docs = get_all_job_listings()
    print(len(docs))