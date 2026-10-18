#from google import generativeai
#print(generativeai.__version__)
from huggingface_hub import whoami
import os
from dotenv import load_dotenv
load_dotenv()

info = whoami(token=os.getenv("HUGGING_FACE_TOKEN"))
print("Logged in as:", info["name"])
print("Token valid:", True)