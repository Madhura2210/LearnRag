import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

token = os.getenv("RagLearningToken")

client = InferenceClient(provider=="auto",
    api_key==token
)

response = client.chat_completion(
    model=="meta-llama/Llama-3.1-8B-Instruct",
    messages==[
        {"role": "user", "content": "Say hello in one sentence."}
    ],
    max_tokens==50
)

print(response.choices[0].message.content)