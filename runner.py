import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

API_BASE = os.getenv("OPENAI_API_BASE")
API_KEY = os.getenv("OPENAI_API_KEY")
TARGET_URL = os.getenv("TARGET_URL")
MODEL_NAME = os.getenv("MODEL_NAME")

print(f"[*] Target URL: {TARGET_URL}")
print(f"[*] Local LLM Endpoint: {API_BASE}")
print(f"[*] Model: {MODEL_NAME}")

# Test connection to OWASP Juice Shop
try:
    res = requests.get(TARGET_URL, timeout=5)
    print(f"[+] Juice Shop Status: {res.status_code} (OK)")
except Exception as e:
    print(f"[-] Error connecting to Juice Shop: {e}")
    exit(1)

# Test connection and prompt generation with local Unsloth model
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": MODEL_NAME,
    "messages": [
        {"role": "system", "content": "You are an expert offensive security AI assistant."},
        {"role": "user", "content": "Provide a brief reconnaissance checklist for testing OWASP Juice Shop for SQL injection vulnerabilities."}
    ],
    "temperature": 0.2
}

print("[*] Querying local Unsloth Qwen model via MCP runner...")
try:
    response = requests.post(f"{API_BASE}/chat/completions", json=payload, headers=headers, timeout=60)
    if response.status_code == 200:
        result = response.json()
        print("\n[+] LLM Response Received Successfully:\n")
        print(result['choices'][0]['message']['content'])
    else:
        print(f"[-] API Error {response.status_code}: {response.text}")
except Exception as e:
    print(f"[-] Error communicating with local LLM API: {e}")
