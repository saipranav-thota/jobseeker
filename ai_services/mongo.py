import os
import logging
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.objectid import ObjectId
import certifi

load_dotenv()

# Read environment or fallback values
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

# Connect to MongoDB with SSL for Atlas
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def load_data(document: dict):
    try:
        result = collection.insert_one(document)
        logging.info(f"Inserted document with _id: {result.inserted_id}")
        return str(result.inserted_id)
    except Exception as e:
        logging.error(f"❌ Failed to insert into MongoDB: {e}")
        return None

def get_data(doc_id : str):
    try:
        result = collection.find_one({"_id":ObjectId(doc_id)})
        return result
    except Exception as e:
        logging.error(f"❌ Failed to fetch document {doc_id}: {e}")
        return None
    
def update_data(doc_id: str, update_dict: dict):
    try:
        collection.update_one(
            {"_id": ObjectId(doc_id)},
            {"$set": update_dict}
        )
        logging.info(f"✅ Updated document {doc_id}")
    except Exception as e:
        logging.error(f"❌ Failed to update document {doc_id}: {e}")

if __name__ == "__main__":
    # data = {"name":"Pranav"}
    # load_data(data)
    print(get_data("686a52a60e625f62932b113e"))