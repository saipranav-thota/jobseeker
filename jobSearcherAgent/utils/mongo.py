import logging
import re
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.objectid import ObjectId
from utils.parser import parse_to_json


load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

logging.basicConfig(level=logging.INFO)

try:
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    logging.info("✅ MongoDB connection established successfully.")
except Exception as e:
    logging.error(f"❌ Failed to connect to MongoDB: {e}")
    collection = None

def load_data(job_data):
    try:
        # If job_data is a list, use it directly
        if isinstance(job_data, list):
            postings = job_data
        elif isinstance(job_data, dict):
            postings = job_data.get("job_postings", [])
        else:
            logging.error("❌ Invalid job data format. Must be dict or list.")
            return []

        if not postings:
            logging.warning("⚠️ No job postings found to insert.")
            return []

        inserted_ids = []
        for post in postings:
            result = collection.insert_one(post)
            inserted_ids.append(str(result.inserted_id))
            logging.info(f"✅ Inserted job posting with _id: {result.inserted_id}")

        # return inserted_ids

    except Exception as e:
        logging.error(f"❌ Failed to insert job postings into MongoDB: {e}")
        return []


def get_data(doc_id: str):
    try:
        if collection is None:
            raise Exception("MongoDB collection is not initialized.")

        result = collection.find_one({"_id": ObjectId(doc_id)})
        logging.info(f"✅ Fetched document with _id: {doc_id}")
        return result
    except Exception as e:
        logging.error(f"❌ Failed to fetch document {doc_id}: {e}")
        return None

def update_data(doc_id: str, update_dict: dict):
    try:
        if collection is None:
            raise Exception("MongoDB collection is not initialized.")

        result = collection.update_one(
            {"_id": ObjectId(doc_id)},
            {"$set": update_dict}
        )
        if result.modified_count > 0:
            logging.info(f"✅ Updated document {doc_id}")
        else:
            logging.warning(f"⚠️ No changes made to document {doc_id}")
    except Exception as e:
        logging.error(f"❌ Failed to update document {doc_id}: {e}")



if __name__ == "__main__":
    text = """
            ```            
                {
                    "job_postings": [
                        {
                            "job_title": "Data scientist",
                            "company": "CAPGEMINI TECHNOLOGY SERVICES INDIA LIMITED",
                            "location": [
                                "Bangalore",
                                "Hyderabad",
                                "Pune"
                            ],
                            "apply_url": "https://www.shine.com/jobs/data-scientist/capgemini-technology-services-india-limited/17401743"
                        },
                        {
                            "job_title": "ML Ops/ Data Science Specialist",
                            "company": "CAPGEMINI TECHNOLOGY SERVICES INDIA LIMITED",
                            "location": [
                                "Bangalore",
                                "Noida",
                                "Chennai",
                                "Hyderabad",
                                "Kolkata",
                                "Gurugram",
                                "Pune",
                                "Mumbai City",
                                "Delhi"
                            ],
                            "apply_url": "https://www.shine.com/jobs/ml-ops-data-science-specialist/capgemini-technology-services-india-limited/17214865"
                        },
                        {
                            "job_title": "ML Ops/ Data Science Specialist",
                            "company": "CAPGEMINI TECHNOLOGY SERVICES INDIA LIMITED",
                            "location": [
                                "Bangalore",
                                "Noida",
                                "Chennai",
                                "Hyderabad",
                                "Gurugram",
                                "Kolkata",
                                "Pune",
                                "Mumbai City",
                                "Delhi"
                            ],
                            "apply_url": "https://www.shine.com/jobs/ml-ops-data-science-specialist/capgemini-technology-services-india-limited/17214866"
                        },
                        {
                            "job_title": "Agentic AI Data Scientist",
                            "company": "CAPGEMINI TECHNOLOGY SERVICES INDIA LIMITED",
                            "location": [
                                "Bangalore",
                                "Hyderabad",
                                "Pune"
                            ],
                            "apply_url": "https://www.shine.com/jobs/agentic-ai-data-scientist/capgemini-technology-services-india-limited/17434951"
                        },
                        {
                            "job_title": "Data Scientist for Education Industry, Mumbai",
                            "company": "Talent Leads HR Solutions Pvt Ltd",
                            "location": [
                                "Mumbai City"
                            ],
                            "apply_url": "https://www.shine.com/jobs/data-scientist-for-education-industry-mumbai/talent-leads-hr-solutions-pvt-ltd/17484335"
                        },
                        {
                            "job_title": "Healthcare Data Scientist",
                            "company": "CLIN BIOSCIENCES",
                            "location": [
                                "Bangalore",
                                "Hyderabad",
                                "Pune",
                                "Mumbai City",
                                "Delhi"
                            ],
                            "apply_url": "https://www.shine.com/jobs/healthcare-data-scientist/clin-biosciences/17484347"      
                        },
                        {
                            "job_title": "Data Scientist",
                            "company": "HARJAI COMPUTERS PRIVATE LIMITED",
                            "location": [
                                "Mumbai City"
                            ],
                            "apply_url": "https://www.shine.com/jobs/data-scientist/harjai-computers-private-limited/17471835" 
                        },
                        {
                            "job_title": "Senior Data Scientist",
                            "company": "Ara Resources Private Limited",
                            "location": [
                                "Bangalore"
                            ],
                            "apply_url": "https://www.shine.com/jobs/senior-data-scientist/ara-resources-private-limited/17402654"
                        },
                        {
                            "job_title": "Data Scientist",
                            "company": "Wroots Global Private Limited",
                            "location": [
                                "Gurugram"
                            ],
                            "apply_url": "https://www.shine.com/jobs/data-scientist/wroots-global-private-limited/17249900"    
                        },
                        {
                            "job_title": "Data Scientist",
                            "company": "CLIN BIOSCIENCES",
                            "location": [
                                "Bangalore",
                                "Hyderabad",
                                "Pune",
                                "Mumbai City",
                                "Delhi"
                            ],
                            "apply_url": "https://www.shine.com/jobs/data-scientist/clin-biosciences/17325301"
                        },
                        {
                            "job_title": "Data Scientist",
                            "company": "ACTION X OUTSOURCE (OPC) PRIVATE LIMITED",
                            "location": [
                                "Hyderabad"
                            ],
                            "apply_url": "https://www.shine.com/jobs/data-scientist/action-x-outsource-opc-private-limited/17346628"
                        },
                        {
                            "job_title": "SENIOR DATA SCIENTIST, GLOBAL DATA SCIENCE (167669)",
                            "company": "Colgate-Palmolive",
                            "location": [
                                "Maharashtra"
                            ],
                            "apply_url": "https://www.shine.com/jobs/senior-data-scientist-global-data-science/colgate-palmolive/17485519"
                        },
                        {
                            "job_title": "SENIOR DATA SCIENTIST, GLOBAL DATA SCIENCE (167666)",
                            "company": "Colgate-Palmolive",
                            "location": [
                                "Maharashtra"
                            ],
                            "apply_url": "https://www.shine.com/jobs/senior-data-scientist-global-data-science/colgate-palmolive/17479473"
                        },
                        {
                            "job_title": "Data Science Trainee / Junior Data Scientist",
                            "company": "Bloom Infotech",
                            "location": [
                                "Punjab"
                            ],
                            "apply_url": "https://www.shine.com/jobs/data-science-trainee-junior-data-scientist/bloom-infotech/17505906"
                        },
                        {
                            "job_title": "Growth Data Scientist",
                            "company": "Moniepoint Group",
                            "location": [
                                "All India"
                            ],
                            "apply_url": "https://www.shine.com/jobs/growth-data-scientist/moniepoint-group/17490655"
                        },
                        {
                            "job_title": "SENIOR DATA SCIENTIST, GLOBAL DATA SCIENCE",
                            "company": "Colgate-Palmolive",
                            "location": [
                                "Maharashtra"
                            ],
                            "apply_url": "https://www.shine.com/jobs/senior-data-scientist-global-data-science/colgate-palmolive/17327837"
                        },
                        {
                            "job_title": "Data Scientist & Gen AI Consultant",
                            "company": "SAP",
                            "location": [
                                "Haryana"
                            ],
                            "apply_url": "https://www.shine.com/jobs/data-scientist-gen-ai-consultant/sap/17422142"
                        },
                        {
                            "job_title": "Junior Data Scientist",
                            "company": "Beckman Coulter Life Sciences",
                            "location": [
                                "Karnataka"
                            ],
                            "apply_url": "https://www.shine.com/jobs/junior-data-scientist/beckman-coulter-life-sciences/17388174"
                        },
                        {
                            "job_title": "Lead Data Scientist",
                            "company": "Beckman Coulter Life Sciences",
                            "location": [
                                "Karnataka"
                            ],
                            "apply_url": "https://www.shine.com/jobs/lead-data-scientist/beckman-coulter-life-sciences/17410504"
                        },
                        {
                            "job_title": "Director, Data Science, Visa Consulting & Analytics, India and South Asia",
                            "company": "Visa",
                            "location": [
                                "All India"
                            ],
                            "apply_url": "https://www.shine.com/jobs/director-data-science-visa-consulting-analytics-india-and-south-asia/visa/17477925"
                        }
                    ]
                }
    ```
    """
    doc_id = load_data(parse_to_json(text))
    print(doc_id)