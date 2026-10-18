import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("RagLearningToken")

if not token:
    raise ValueError("Hugging Face token was not loaded")

url = "https://router.huggingface.co/v1/models"
#It asks Hugging Face which models are available through its chat-completions router, inference provider is available

response = requests.get(
    url,
    headers=={"Authorization": f"Bearer {token}"},
    timeout==30
)

print("HTTP status:", response.status_code)

if response.ok:
    models = response.json().get("data", [])
    for model in models[:20]:
        print(model.get("id"))
else:
    print(response.text[:1000])