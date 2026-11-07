# Test matrix and confirmation requirements

This matrix preserves the IDs used by the committed tests.py. The implementation sends GET requests to each URL. The vector strings are metadata and are not used to construct validation requests. The model helper evaluate_with_llm is defined but never called by the loop.

Observed statuses are transcribed from [the committed probe screenshot](screenshots/06-security-checks.png). They were not collected by a new run during documentation review.

| ID | Intended condition | Captured status | What can be concluded | Evidence needed to confirm a weakness |
|---|---|---|---|---|
| <a id="t01"></a>T01 | SQL injection login bypass | 500 | GET caused an error; bypass unverified | Correct login method, baseline and changed authentication behaviour tied to the test |
| <a id="t02"></a>T02 | Search XSS | 200 | Fragment was not transmitted; response does not test script execution | Browser execution evidence and affected DOM context |
| <a id="t03"></a>T03 | Basket access control | 401 | Request was denied for the tested context | Two controlled users and owner/non-owner resource comparison |
| <a id="t04"></a>T04 | Backup file exposure | 403 | Candidate file request denied | Actual unauthorised sensitive file content, if obtained by a separate authorised test |
| <a id="t05"></a>T05 | Administrative route access | 200 | Fragment was not transmitted; no admin access established | Browser and protected backend-function evidence under controlled user roles |
| <a id="t06"></a>T06 | Exposed API documentation | 200 | Route answered; returned content is not captured | Intended documentation body and a concrete sensitivity or policy assessment |
| <a id="t07"></a>T07 | Password reset weakness | 500 | GET caused an error; reset manipulation unverified | Correct workflow with a disposable account and expected/observed outcomes |
| <a id="t08"></a>T08 | Search input validation | 200 | Ordinary GET answered; no payload validation or RCE evidence | Specific input, baseline and relevant response behaviour |
| <a id="t09"></a>T09 | Redirect handling | 406 | Request rejected in captured run | Unfollowed response Location or controlled browser navigation demonstrating an unauthorised destination |
| <a id="t10"></a>T10 | Mass assignment | 401 | GET was denied; no write or role mutation attempted | Approved disposable-account request and independently verified effective role |

All ten vulnerability classifications are **unverified**. The 401/403/406 observations are useful negative responses for those exact probes, but they do not prove all bypasses are absent.

## Future record for each check

Record run ID, UTC timestamp, source commit, image digest, actual model ID and scope. For the individual check, store method, exact route, redacted request, status, relevant response headers and body, identity context, baseline/control, outcome and evidence path. Use confirmed, no issue observed, inconclusive or not run. Tie impact, severity and remediation to what was demonstrated.

For browser tests, preserve a redacted screenshot and the relevant network or DOM observation. An application challenge notification can corroborate evidence, but it should not replace the request, response or execution context.
