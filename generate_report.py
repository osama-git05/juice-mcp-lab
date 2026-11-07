"""Export reviewed historical probe observations, not a new scan verdict."""
import json
from pathlib import Path

OBSERVATIONS = [
    ("T01", "SQL injection login bypass", 500),
    ("T02", "Search XSS", 200),
    ("T03", "Basket access control", 401),
    ("T04", "Backup file exposure", 403),
    ("T05", "Administrative route access", 200),
    ("T06", "API documentation exposure", 200),
    ("T07", "Password reset weakness", 500),
    ("T08", "Search input validation", 200),
    ("T09", "Redirect handling", 406),
    ("T10", "Mass assignment", 401),
]

report = {
    "project": "Local LLM Security Assessment Lab",
    "provenance": {
        "source": "Committed screenshot; manually reviewed baseline",
        "evidence": "docs/screenshots/06-security-checks.png",
        "reviewed_revision": "b892b45beb5e54215cec0eac2a2729e2a1552504",
        "new_run_ingested": False,
        "target_shown": "http://10.0.2.15:3000",
    },
    "summary": {
        "catalogue_cases": 10,
        "displayed_http_observations": 10,
        "confirmed_vulnerabilities": 0,
        "unverified_cases": 10,
        "status": "Baseline evidence review; vulnerability validation pending",
    },
    "test_results": [
        {
            "id": test_id,
            "name": name,
            "observed_http_status": status,
            "vulnerability_classification": "unverified",
            "evidence": "docs/screenshots/06-security-checks.png",
            "confirmation_requirements": f"docs/TEST_MATRIX.md#{test_id.lower()}",
        }
        for test_id, name, status in OBSERVATIONS
    ],
}
output = Path(__file__).resolve().parent / "docs" / "report_summary.json"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(f"Reviewed baseline exported to {output}")
print("No new scan was run or ingested; all vulnerability cases remain unverified.")
