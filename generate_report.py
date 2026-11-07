import json
import os

report = {
    "project": "OWASP Juice Shop MCP Automated Assessment",
    "target": os.getenv("TARGET_URL", "http://10.0.2.15:3000"),
    "runner_model": os.getenv("MODEL_NAME", "Qwen2.5-Coder-7B-Instruct"),
    "summary": {
        "total_tests": 10,
        "status": "Completed",
        "scope": "T01 - T10 Vulnerability Verification"
    },
    "test_results": [
        {"id": "T01", "name": "SQL Injection (Login Bypass)", "category": "A03:2021-Injection"},
        {"id": "T02", "name": "Cross-Site Scripting (XSS) in Search", "category": "A03:2021-Injection"},
        {"id": "T03", "name": "Broken Object Level Authorization", "category": "A01:2021-Broken Access Control"},
        {"id": "T04", "name": "Sensitive Data Exposure (Config File)", "category": "A05:2021-Security Misconfiguration"},
        {"id": "T05", "name": "Forced Browsing (Admin Dashboard)", "category": "A01:2021-Broken Access Control"},
        {"id": "T06", "name": "Security Misconfiguration (Swagger Docs)", "category": "A05:2021-Security Misconfiguration"},
        {"id": "T07", "name": "Weak Authentication (Password Reset)", "category": "A07:2021-Identification & Auth Failures"},
        {"id": "T08", "name": "Input Validation & Search Vector", "category": "A03:2021-Injection"},
        {"id": "T09", "name": "Unvalidated Redirects", "category": "A01:2021-Broken Access Control"},
        {"id": "T10", "name": "Mass Assignment / Privilege Escalation", "category": "A01:2021-Broken Access Control"}
    ]
}

with open("docs/report_summary.json", "w") as f:
    json.dump(report, f, indent=4)

print("[+] Report generated successfully at docs/report_summary.json")
