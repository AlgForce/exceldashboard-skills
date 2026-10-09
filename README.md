# ExcelDashboard AI Skills

Official agent skills for data analysis and visual report generation with [ExcelDashboard AI](<https://www.exceldashboard.ai>).

ExcelDashboard AI helps users turn business data into visual reports with charts, structured analysis, and browser-based report previews. This repository provides instructions that help AI agents prepare report outlines, create reports through MCP, and track report generation.

[Explore ExcelDashboard AI](<https://www.exceldashboard.ai>) · [MCP Setup Guide](<https://www.exceldashboard.ai/mcp>) · [Agent Documentation](<https://www.exceldashboard.ai/mcp.md>)

## What this skill helps you do

- Analyze user-provided data using your agent's available tools.
- Organize findings into a structured report outline.
- Create visual reports through the ExcelDashboard AI MCP server.
- Track report progress and share the report preview link.
- Produce sales reports, marketing performance reports, agency client reports, and business reviews.

The agent performs data analysis and prepares the outline. ExcelDashboard AI generates the visual report from that outline.

## Available skill

| Skill | Purpose |
|---|---|
| ExcelDashboard Report (skills/exceldashboard-report/SKILL.md) | Prepare analytical report outlines, create visual reports, and track generation through MCP. |

See the report outline format (skills/exceldashboard-report/references/outline-format.md) for the required structure and examples.

## Connect to the MCP server

| Setting | Value |
|---|---|
| Product | ExcelDashboard AI |
| Website | https://www.exceldashboard.ai |
| MCP endpoint | https://api.exceldashboard.ai/mcp |
| Transport | Streamable HTTP |
| Authentication | OAuth |
| Setup documentation | https://www.exceldashboard.ai/mcp |

Connect using a client that supports remote MCP and the server's OAuth flow. Sign in and select the workspace where reports should be created.

Installing this skill and connecting the MCP server are separate steps. Users complete authorization in the browser.

## Install the skill

Use your agent's supported GitHub skill installation method and select:

```
skills/exceldashboard-report
```

For agents that support local skill directories, copy the complete `exceldashboard-report` folder, including its `references` directory, into the location documented by your agent.

Then connect the MCP server and complete OAuth authorization.

Client support for skill installation and OAuth varies. Consult your client's documentation and the ExcelDashboard AI setup guide.

## Report workflow

1. Read the user's request and available data.
2. Calculate and verify the findings using the agent's tools.
3. Prepare an outline following the report outline format.
4. Call `create_report`.
5. Show the returned report preview link to the user.
6. Call `get_report` according to the returned polling interval.
7. Stop polling when the report completes or fails.

Keep the user informed of report progress and provide the report link with status updates.

## MCP tools

| Tool | Input | Purpose |
|---|---|---|
| `create_report` | Required `outline`; optional `locale` | Start report generation from a Markdown outline. |
| `get_report` | Required `job_id` | Retrieve report status, progress, and the report link. |

The outline must include a report title, page sections, and the verified information needed to render the report. Set `locale` to `en` for an English report.

The tools do not require users to enter a workspace ID or an idempotency key.

## Example requests

### Sales performance report

“Analyze this sales dataset and create a three-page report covering revenue trends, product performance, and recommended actions.”

### Agency client report

“Create a monthly client report from these campaign results. Include spend, conversions, return on advertising spend, and next month's recommendations.”

### Executive business review

“Turn these business metrics into a visual report with an executive summary, key findings, and supporting charts.”

Provide source data or verified metrics so the agent can prepare an accurate outline.

## Frequently asked questions

### Can I use Excel or CSV files?

Yes, when your agent can read those files. The agent analyzes the data and submits a structured outline. The MCP report tools do not accept raw file uploads.

### Do I need an ExcelDashboard AI account?

Yes. Report creation requires an authorized account and workspace. Hosted service access is subject to your account's limits and terms.

### Does reading this README install the skill?

No. The agent must use a supported skill installation method or load the skill instructions through its available capabilities.

### Does installing the skill automatically connect MCP?

No. MCP configuration and browser authorization are separate steps.

### Where can I view the report?

The MCP tools return a report preview link. Open that link to view the report in your browser.

## Documentation and support

- [ExcelDashboard AI website](<https://www.exceldashboard.ai>)
- [MCP connection and setup](<https://www.exceldashboard.ai/mcp>)
- [Documentation for agents](<https://www.exceldashboard.ai/mcp.md>)
- Skill instructions (skills/exceldashboard-report/SKILL.md)
- Report outline format (skills/exceldashboard-report/references/outline-format.md)

For issues with the skill instructions, use this repository's Issues tab.

## License

The skill files in this repository are available under the MIT License (LICENSE).

The license applies to the files in this repository. Access to the hosted ExcelDashboard AI service is governed by the service's terms.
