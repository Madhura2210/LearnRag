from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("RagLearningGeminiToken"),
    temperature=0.1
)
prompt = PromptTemplate(
    template = "Write a summary for the following Document -\n{document}",input_variables=['document']
)
parser = StrOutputParser()
loader = TextLoader(r"C:\Users\Madhura\Desktop\rag_run.txt", encoding = 'utf-8')

docs = loader.load()
print(type(docs))

print(len(docs))

print(type(docs[0]))
print(docs[0]) #page_content + metadata
chain = prompt|model|parser

print(chain.invoke({'document':docs[0].page_content}))   