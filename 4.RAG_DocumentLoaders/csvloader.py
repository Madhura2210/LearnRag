from langchain_community.document_loaders import CSVLoader
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
    template = "Write a summary based on this csv file -\n{document}",input_variables=['document']
)
parser = StrOutputParser()



loader = CSVLoader(r"C:\Users\Madhura\Downloads\train.csv\train.csv")
document = loader.load()

chain = prompt | model | parser
print(chain.invoke({'document':document[0].page_content}))   
