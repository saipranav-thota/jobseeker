import chromadb
import os
from embeddings.utils import get_all_job_listings, get_job_listings_by_ids

PERSIST_DIRECTORY = "./chroma_db_job_postings"
os.makedirs(PERSIST_DIRECTORY, exist_ok=True)
client = chromadb.PersistentClient(path=PERSIST_DIRECTORY)

collection_name = "job_postings"
collection = client.get_or_create_collection(name=collection_name)

print(f"Collection '{collection_name}' created or retrieved.")

def load_and_upsert_job_data():
    job_data_from_mongo = get_all_job_listings()
    ids = []
    documents = []

    for item in job_data_from_mongo:
        ids.append(str(item['_id']))
        documents.append(item['job_title'])


    collection.upsert(
        documents=documents,
        ids=ids
    )

    print(f"\nUpserted {len(ids)} documents into the collection.")
    print(f"Current total documents in collection: {collection.count()}")


def get_job_embeddings(queries, k):
    ids = []
    for query_text in queries:
        results = collection.query(
            query_texts=[query_text],
            n_results=k,
        )
        if results['documents'][0]:
            for i in range(len(results['documents'][0])):
                ids.append(results['ids'][0][i])
    return ids

if __name__ == "__main__":
    load_and_upsert_job_data()
    query_text = ['Experienced software developer roles', 'AI', 'Deep Learning']
    ids = get_job_embeddings(query_text, 2)
    get_job_listings_by_ids(ids)