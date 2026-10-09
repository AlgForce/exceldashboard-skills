# Contributing

Contributions that improve reproducible installation, reporting instructions, examples, and error handling are welcome.

Before opening a pull request:

1. Explain the user problem and the resulting behavior.
2. Keep MCP instructions consistent with the current [official documentation](https://www.exceldashboard.ai/mcp.md). Preserve the separation between skill installation, MCP configuration, and OAuth.
3. Use synthetic or explicitly publishable data. State grain, date range, units, definitions, and limitations. Include source CSVs and complete outlines for new examples.
4. Run `python3 scripts/verify_examples.py` when changing examples. Check relative links and the [outline format](skills/exceldashboard-report/references/outline-format.md).
5. Record client compatibility with a version, date, and end-to-end result. Clearly distinguish observed behavior from assumptions.

Instruction changes must retain job tracking, avoid automatic retries of uncertain creation calls, and avoid claiming completion before `status: completed`. The connector exposes only `create_report` and `get_report`.

Do not include tokens, private customer data, workspace credentials, or private report links in Issues or pull requests. For hosted-account support, use the website's support contact.
