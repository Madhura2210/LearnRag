from langchain_community.document_loaders import TextLoader, DirectoryLoader
import os 
from pathlib import Path

directory = Path(r"C:\Users\Madhura\Documents\test_folder_rag")

selected_files = [
    "rag_run.txt"
]

docs = []

for filename in selected_files:
    loader = TextLoader(str(directory / filename))
    docs.extend(loader.load())

print(f"Loaded {len(docs)} documents")

for doc in docs:
    print(doc.metadata)

    #lazy_load incase you want to import eventually for larger docs, which are not easily available all at once