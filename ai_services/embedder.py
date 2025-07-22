#convert text into vector embeddings
# using sentence transfrmer
import json
from sentence_transformers import SentenceTransformer
from resume_parser import extract_text_from_doc
from mongo import get_data

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def get_vector_embeddings(id):
    data = get_data(id)
    skills = data.get("skills", [])
    job_domains = data.get("domains", [])
    summary = data.get("summary")  

    # Build full text blob
    text = "\n".join([
        summary or "",
        "Skills: " + ", ".join(skills or []),
        "Domains: " + ", ".join(job_domains or []),
    ])

      
    embeddings = model.encode(text)
    
    return embeddings

if __name__ == "__main__":
    print(get_vector_embeddings("686a52a60e625f62932b113e"))
