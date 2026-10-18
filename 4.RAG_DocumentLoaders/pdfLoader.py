from langchain_community.document_loaders import PyPDFLoader

import os
from dotenv import load_dotenv
load_dotenv()
loader = PyPDFLoader(r"C:\Users\Madhura\Downloads\MonteCarlo.pdf")
docs = loader.load()
print(len(docs))#len of pages, each list item contains a dictionary with 2 keys:page content and metadata
#print(docs[0].page_content)
print(docs[9])#page_content+metadata of last page
#docs[<number>] every page is indexed with a number, for 10 pages we will have indices from 0-9