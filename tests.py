import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_BASE = os.getenv("OPENAI_API_BASE")
API_KEY = os.getenv("OPENAI_API_KEY")
TARGET_URL = os.getenv("TARGET_URL")
MODEL_NAME = os.getenv("MODEL_NAME")

# Define OWASP Juice Shop Test Cases T01 - T10
TEST_CASES = [
    {"id": "T01", "name": "SQL Injection (Login Bypass)", "endpoint": "/rest/user/login", "vector": "' OR 1=1--"},
    {"id": "T02", "name": "Cross-Site Scripting (XSS) in Search", "endpoint": "/#/search?q=<script>alert(1)</script>", "vector": "<script>alert(1)</script>"},
    {"id": "T03", "name": "Broken Object Level Authorization (BASKET)", "endpoint": "/rest/basket/1", "vector": "IDOR enumeration"},
    {"id": "T04", "name": "Sensitive Data Exposure (Config File)", "endpoint": "/ftp/package.json.bak", "vector": "Directory traversal / backup file retrieval"},
    {"id": "T05", "name": "Forced Browsing (Admin Dashboard)", "endpoint": "/#/administration", "vector": "Client-side routing restriction bypass"},
    {"id": "T06", "name": "Security Misconfiguration (Swagger API docs)", "endpoint": "/api-docs/", "vector": "Exposed API documentation endpoint"},
    {"id": "T07", "name": "Weak Authentication (Password Reset)", "endpoint": "/rest/user/reset-password", "vector": "Predictable security questions"},
    {"id": "T08", "name": "Remote Code Execution / Deserialization Vector", "endpoint": "/rest/products/search", "vector": "Malformed input payload"},
    {"id": "T09", "name": "Unvalidated Redirects", "endpoint": "/redirect?to=https://example.com", "vector": "External redirect parameter manipulation"},
    {"id": "T10", "name": "Mass Assignment / User Role Escalation", "endpoint": "/api/Users", "vector": "Privilege escalation via JSON payload injection"}
]

def evaluate_with_llm(test_case):
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You are an expert security assessment AI."},
            {"role": "user", "content": f"Analyze test case {test_case['id']}: {test_case['name']} targeting endpoint {test_case['endpoint']} with vector '{test_case['vector']}'. Provide a concise risk rating and validation strategy."}
        ],
        "temperature": 0.2
    }
    try:
        res = requests.post(f"{API_BASE}/chat/completions", json=payload, headers=headers, timeout=30)
        if res.status_code == 200:
            return res.json()['choices'][0]['message']['content'].strip()
    except Exception:
        pass
    return "LLM evaluation unavailable."

print("[*] Initializing OWASP Juice Shop Automated Test Suite (T01-T10)...")
for test in TEST_CASES:
    url = f"{TARGET_URL}{test['endpoint']}"
    try:
        response = requests.get(url, timeout=5)
        status = response.status_code
    except Exception:
        status = "Connection Error"

    print(f"[{test['id']}] {test['name']} -> Endpoint: {test['endpoint']} | Status: {status}")
