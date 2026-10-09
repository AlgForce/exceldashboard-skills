# ExcelDashboard AI Skills

Official agent skills for analyzing Excel/CSV data and generating visual analytical reports with [ExcelDashboard AI](https://www.exceldashboard.ai/?utm_source=github&utm_medium=referral&utm_campaign=skills_launch&utm_content=readme).

Your agent reads the data, verifies calculations, and prepares an analytical outline. The ExcelDashboard AI MCP server creates the visual report and returns a live browser preview. This repository contains the skill instructions and reproducible examples, maintained in the AlgForce GitHub organization.

[Website](https://www.exceldashboard.ai/?utm_source=github&utm_medium=referral&utm_campaign=skills_launch&utm_content=website) · [MCP setup](https://www.exceldashboard.ai/mcp?utm_source=github&utm_medium=referral&utm_campaign=skills_launch&utm_content=setup) · [Installation guide](docs/installation.md) · [Examples](examples/README.md)

## See the reporting workflow

**Excel or CSV → agent analysis → verified outline → MCP report generation → live preview**

Use the [agency reporting walkthrough](https://www.exceldashboard.ai/mcp/examples/agency-report?utm_source=github&utm_medium=referral&utm_campaign=skills_launch&utm_content=agency_example) for the website example, or inspect the [local agency example](examples/agency-report/README.md), including its synthetic CSV and complete outline.

The repository examples are source data and expected outlines, not screenshots of completed MCP jobs. Their calculations can be reproduced locally without an account. Generating a hosted report requires an authorized account and may consume service credits.

## Quick start

1. Install [exceldashboard-report](skills/exceldashboard-report/SKILL.md) from this repository, preserving its `references/` directory. See the [installation guide](docs/installation.md).
2. Configure your client's remote MCP connection to `https://api.exceldashboard.ai/mcp` using Streamable HTTP.
3. Complete browser OAuth and select a workspace. Confirm that this connection discovers `create_report` and `get_report`.
4. Attach one of the example CSVs and use its prompt to request a report. The agent analyzes the file, submits an outline, and returns the preview link.

Skill installation, MCP configuration, and OAuth are separate steps. Reading this README does not complete them.

## Install and connect

| Setting | Value |
|---|---|
| Repository | https://github.com/AlgForce/exceldashboard-skills |
| Skill directory | `skills/exceldashboard-report` |
| MCP endpoint | `https://api.exceldashboard.ai/mcp` |
| Transport | Streamable HTTP |
| Authentication | Browser OAuth and workspace selection |
| Setup guide | https://www.exceldashboard.ai/mcp |
| Agent documentation | https://www.exceldashboard.ai/mcp.md |

Use your client's supported GitHub skill installer, or copy the complete skill directory into its documented skill location. Client-specific configuration and verification steps are in the [installation guide](docs/installation.md). Compatibility is only claimed when a dated end-to-end result is recorded there.

## Reproducible report examples

All three examples use **synthetic data**, not real customer records or product performance claims.

| Example | Business question | Included material |
|---|---|---|
| [Sales performance](examples/sales-report/README.md) | How did sales change, and which product contributed most? | CSV, prompt, definitions, four-page outline |
| [Agency client report](examples/agency-report/README.md) | How did attributed ROAS and cost per conversion change? | CSV, prompt, definitions, four-page outline |
| [Executive business review](examples/business-review/README.md) | Did revenue meet target, and what was the contribution margin? | CSV, prompt, definitions, four-page outline |

Recalculate the example metrics with Python 3 (standard library only):

```bash
python3 scripts/verify_examples.py
```

## Skill and MCP tools

The [report skill](skills/exceldashboard-report/SKILL.md) covers analysis, submission, progress tracking, and failures. The [outline reference](skills/exceldashboard-report/references/outline-format.md) defines the required page syntax and layouts.

| Tool | Input | Purpose |
|---|---|---|
| `create_report` | Required `outline`; optional `locale` | Start a new visual report from a Markdown outline |
| `get_report` | Required `job_id` | Retrieve progress, final status, and the report URL |

Use `locale: "en"` for English output; the documented default is `zh-CN`. Calls do not require a workspace ID or an idempotency key. Each `create_report` call creates a new job, so uncertain submissions should not be retried automatically.

## Frequently asked questions

### Can the skill analyze Excel and CSV files?

Yes, when the agent can read and calculate from those files. The agent submits a verified outline and aggregated chart data. These MCP tools do not upload raw files.

### Is this an open-source reporting service?

The repository's instructions, documentation, and synthetic examples are available under the MIT License. Hosted ExcelDashboard AI access requires an account and is governed by the service's terms, limits, and pricing.

### Does it work with every agent?

The client must support the skill-loading workflow, remote Streamable HTTP MCP, and the server's OAuth flow. See the [verification status](docs/installation.md#client-verification-status); an untested client is not a confirmed integration.

### Where does the report appear?

The tools return a `report_url`. Open it in a browser to view the report. Automatic opening inside an agent depends on that client's available browser tools. A returned link does not prove generation is complete; the final status must be `completed`.

### Can MCP edit an existing report?

The connector exposes creation and status tools. Use the preview's Edit button for frontend editing with the appropriate signed-in permissions.

### How does GitHub installation relate to SkillHub?

This repository uses the directory name `exceldashboard-report`. Existing website documentation also references the SkillHub identifier `@org-9c0xwtir/algforce-report-v1`. They are separate distribution channels; do not assume their versions match. Use one installation source and compare its instructions when switching.

## Documentation and support

- [Client setup and troubleshooting](https://www.exceldashboard.ai/mcp/guides)
- [Agent documentation](https://www.exceldashboard.ai/mcp.md)
- [Contributing](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)
- [Report an instruction or installation issue](https://github.com/AlgForce/exceldashboard-skills/issues)

Use repository Issues for reproducible documentation or skill problems. For account and hosted-service support, use the contact options on the [website](https://www.exceldashboard.ai/).

## License

[MIT](LICENSE) applies to the files in this repository. It does not grant access to the hosted service or change the service's terms.
