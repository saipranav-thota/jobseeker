# main script
import os
import logging
import datetime
from bson import ObjectId
from ai_services.extract_resume import extract_text_from_doc, extract_text_from_pdf
from ai_services.resume_parser import parse_resume
from ai_services.mongo import load_data

logging.basicConfig(level=logging.INFO)


def load_resume(path):

    filename = os.path.basename(path)
    size = os.path.getsize(path)
    now = datetime.datetime.utcnow()

    resume_raw_text = extract_text_from_doc(path) or extract_text_from_pdf(path)
    data = parse_resume(resume_raw_text)
    metadata = {
        "_id":ObjectId(),
        "info":{
            "filename":filename,
            "size":size,
            "created_at":now
        }
    }
    data = data

    document = {**metadata, **data}
    load_data(document)

    logging.info(f"✅ Loaded resume {filename} into database.")
    return str(metadata["_id"])


if __name__ == "__main__":
    doc_id = load_resume("resume.docx")