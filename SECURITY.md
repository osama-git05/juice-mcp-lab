# Security and credential handling

## Existing exposure

The reviewed revision contained a non-empty API key in .env and a key visible in the API-authentication screenshot. Treat both credentials as exposed.

Revoke the old key in Unsloth Settings → API and issue a replacement. Store it only in a private environment file or approved secret store. This documentation change removes .env and the confirmed exposed screenshot from the current tree. Git history still contains the old objects.

After revocation, the owner can follow GitHub's sensitive-data removal process. Coordinate any history rewrite with collaborators and forks. This change does not rewrite history.

## Local operation

Bind inference and Juice Shop to loopback where practical. Keep external providers, web search and execution tools disabled when evaluating local-only inference. A local configured URL alone does not establish zero external traffic.

The current tests.py accepts TARGET_URL from the environment and Requests follows redirects by default. No hardcoded scope or approval gate is implemented. A later MCP release must enforce scope and redirect restrictions independently of the model.

## Evidence

Keep raw originals private and publish reviewed copies with tokens, cookies, keys, passwords and personal details removed. Screenshots show displayed observations, not complete request/response validation.

- [GitHub sensitive-data removal](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
- [Unsloth API keys](https://unsloth.ai/docs/basics/api.md)
