# Architecture

## Implemented data flow

The current source uses direct HTTP calls through Requests. The model returns a checklist. The probe loop does not use that response to choose its next action.

![Current architecture](architecture/current-architecture.png)

```mermaid
flowchart TD
    U["Operator in Kali"] --> R["runner.py"]
    R --> T["Target HTTP check"]
    R --> S["SSH reverse tunnel"]
    S --> L["Unsloth inference"]
    L --> O["Printed checklist"]
    U --> P["tests.py fixed GET probes"]
    P --> J["Juice Shop"]
    J --> H["Printed HTTP statuses"]
    U --> G["generate_report.py"]
    G --> B["Reviewed baseline JSON"]
```

There is no FastAPI application, MCP client/server, retrieval index, tool-calling loop, hardcoded target allowlist or approval interceptor in the reviewed source.

## Network roles

| Endpoint | Role |
|---|---|
| Windows loopback 8888 | Model listener |
| Kali loopback 8888 | Reverse-forwarded model API |
| Windows loopback 2222, if configured | NAT forwarding to Kali SSH 22 |
| Kali loopback 3000 | Recommended local application binding |
| 10.0.2.15:3000 | Address printed in the recorded runner and probe evidence |

The screenshots demonstrate a working inference response but do not independently establish all adapter or SSH settings.

## Planned MCP increment

![Planned workflow](architecture/planned-mcp-workflow.png)

```mermaid
flowchart TD
    M["Model proposes action"] --> V["Validate target and action"]
    V --> D{"Approval needed"}
    D -->|Yes| A["Operator review"]
    D -->|No| C["MCP invocation"]
    A -->|Approve| C
    A -->|Reject| E["Record rejection"]
    C --> T["Authorised target"]
    T --> R["Capture full evidence"]
    R --> F["Review and draft finding"]
```

Start with one fixed check, preserve its full result and show a real MCP tools/list and tools/call exchange. Add adaptive selection after that path is demonstrated. Editable draw.io files, Graphviz sources and PNG exports are in docs/architecture. Open either .drawio file in diagrams.net to edit it.
