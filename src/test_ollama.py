import requests

url = "http://localhost:11434/api/generate"

data = {
    "model": "llama3.2:1b",
    "prompt": "Explain artificial intelligence in 2 simple sentences.",
    "stream": False
}

response = requests.post(url, json=data, timeout=120)
response.raise_for_status()

result = response.json()

print("AI Response:")
print(result["response"])