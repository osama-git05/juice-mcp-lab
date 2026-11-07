# Penetration Testing Assessment Report: OWASP Juice Shop
**Project:** Local-LLM Powered MCP Security Evaluation  
**Target:** OWASP Juice Shop (`http://10.0.2.15:3000`)  
**Runner Architecture:** Python FastAPI / Unsloth Qwen2.5-Coder-7B-Instruct via SSH Reverse Tunnel  

---

## 1. Executive Summary
This report summarizes the automated security assessment performed against an isolated instance of OWASP Juice Shop. Utilizing a local Large Language Model (`Qwen2.5-Coder-7B-Instruct`) hosted on Windows hardware and bridged via a secure SSH reverse tunnel to a Kali Linux testing environment, a Model Context Protocol (MCP) runner executed ten distinct vulnerability checks (T01–T10) mapping directly to the OWASP Top 10.

## 2. Lab Topology & Architecture
- **Host Infrastructure:** Windows 10/11 with RTX 2080 GPU running Unsloth Studio local LLM inference server on port `8888`.
- **Guest Testing Environment:** Kali Linux Virtual Machine (VirtualBox NAT with SSH reverse port forwarding to `127.0.0.1:2222`).
- **Target Application:** OWASP Juice Shop containerized deployment on Docker (`http://10.0.2.15:3000`).

## 3. Summary of Test Cases (T01 - T10)

| ID | Vulnerability / Test Case | OWASP Category | Target Endpoint | Status / Finding |
|----|---------------------------|----------------|-----------------|------------------|
| **T01** | SQL Injection (Login Bypass) | A03:2021-Injection | `/rest/user/login` | Verified Vulnerable |
| **T02** | Cross-Site Scripting (XSS) in Search | A03:2021-Injection | `/#/search?q=...` | Verified Vulnerable |
| **T03** | Broken Object Level Authorization (BASKET) | A01:2021-Broken Access Control | `/rest/basket/1` | Verified Vulnerable |
| **T04** | Sensitive Data Exposure (Config File) | A05:2021-Security Misconfiguration | `/ftp/package.json.bak` | Verified Vulnerable |
| **T05** | Forced Browsing (Admin Dashboard) | A01:2021-Broken Access Control | `/#/administration` | Verified Vulnerable |
| **T06** | Security Misconfiguration (Swagger Docs) | A05:2021-Security Misconfiguration | `/api-docs/` | Verified Vulnerable |
| **T07** | Weak Authentication (Password Reset) | A07:2021-Identification Failures | `/rest/user/reset-password` | Verified Vulnerable |
| **T08** | Input Validation & Search Vector | A03:2021-Injection | `/rest/products/search` | Verified Vulnerable |
| **T09** | Unvalidated Redirects | A01:2021-Broken Access Control | `/redirect?to=...` | Verified Vulnerable |
| **T10** | Mass Assignment / Privilege Escalation | A01:2021-Broken Access Control | `/api/Users` | Verified Vulnerable |

## 4. Conclusion & Recommendations
The automated MCP runner successfully verified all targeted vulnerability vectors without reliance on external cloud APIs, ensuring complete data privacy and local execution integrity. Remediation efforts should focus on input sanitization, strict object-level authorization checks, and proper administrative route guarding.
