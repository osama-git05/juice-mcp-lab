# Local-RAG & MCP Automated Penetration Testing Lab
A professional-grade Model Context Protocol (MCP) security assessment framework powered by a local Large Model (`Qwen2.5-Coder-7B-Instruct`), bridging a Windows host RTX GPU via an SSH reverse tunnel to a Kali Linux testing environment targeting OWASP Juice Shop.

## Architecture Overview
- **Host:** Windows 10/11 + RTX 2080 GPU (Unsloth Studio LLM Server on port `8888`)
- **Guest:** Kali Linux VM (Dockerized OWASP Juice Shop + Python MCP Runner)
- **Tunnel:** Secure SSH Reverse Port Forwarding (`127.0.0.1:2222 -> 8888`)

## Project Structure
- `runner.py`: Core MCP runner interface for local LLM test execution.
- `tests.py`: Automated OWASP Top 10 security test suite (T01–T10).
- `generate_report.py`: Aggregates scan telemetry into structured JSON.
- `docs/REPORT.md`: Comprehensive penetration testing report.
- `docs/screenshots/`: Evidence capture directory (`01` to `06`).
