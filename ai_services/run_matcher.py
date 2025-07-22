# main script
import os
import logging
import datetime
from pypdf import PdfReader
from bson import ObjectId


from extract_resume import extract_text_from_doc, extract_text_from_pdf
from resume_parser import parse_resume
from mongo import load_data, update_data
from embedder import get_vector_embeddings

logging.basicConfig(level=logging.INFO)


def load_resume(path):

    filename = os.path.basename(path)
    size = os.path.getsize(path)
    now = datetime.datetime.utcnow()

    resume_raw_text = extract_text_from_doc(path)
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
    embedding = get_vector_embeddings(doc_id)
    update_data(
        doc_id,
        {"embedding": embedding.tolist()}
    )
