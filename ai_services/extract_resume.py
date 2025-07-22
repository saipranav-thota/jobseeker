#Extract text when resume is given
from docx import Document
from pypdf import PdfReader

def extract_text_from_doc(doc_path):
    doc = Document(doc_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def extract_text_from_pdf(doc_path):
    reader = PdfReader(doc_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text


if __name__ == "__main__":
    print(extract_text_from_doc("resume.docx"))
    print(extract_text_from_pdf("resume.pdf"))