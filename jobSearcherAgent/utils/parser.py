import json
import logging
import re

def parse_to_json(response):
    logging.info("Started Parsing")

    code_blocks = re.findall(r"```(?:json)?\s*(.*?)\s*```", response, re.DOTALL)

    if code_blocks:
        logging.info("🧹 Found and extracted code block from response")
        content = code_blocks[0]
    else:
        logging.warning("⚠️ No code block found, attempting to parse full response")
        content = response

    try:
        return json.loads(content)
    except json.JSONDecodeError as e:
        logging.error(f"❌ Failed to parse JSON: {e}")
        return None


if __name__ == "__main__":
    text = """
        
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
    """
    print(parse_to_json(text))
