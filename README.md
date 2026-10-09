# ExcelDashboard AI Skills

Official agent skills for ExcelDashboard AI.

## Report Skill

The report skill guides an agent through data analysis, outline
preparation, report creation, progress tracking, and report presentation.

Skill: [exceldashboard-report](skills/exceldashboard-report/SKILL.md)

Outline reference:
[outline-format.md](skills/exceldashboard-report/references/outline-format.md)

## MCP Connection

- Website and documentation: https://www.exceldashboard.ai/mcp
- MCP server: https://api.exceldashboard.ai/mcp
- Transport: Streamable HTTP
- Authorization: OAuth; users sign in and select a workspace
- Tools: create_report and get_report

Installing this skill does not configure the MCP connection or complete
OAuth authorization. Connect and authorize the MCP server separately.

## License

The skill instructions and reference files in this repository are
licensed under the MIT License. See LICENSE.

The hosted ExcelDashboard AI service is governed by its own terms
and account limits.
