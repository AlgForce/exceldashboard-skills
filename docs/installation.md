# Install the ExcelDashboard AI report skill

## Install from GitHub

Repository: https://github.com/AlgForce/exceldashboard-skills

Skill directory: `skills/exceldashboard-report`

If your agent provides a GitHub skill installer, give it both values and follow its supported workflow. If it supports local skill directories, you can clone the repository:

```bash
git clone https://github.com/AlgForce/exceldashboard-skills.git
```

Copy the complete `skills/exceldashboard-report` directory into the skill location documented by your client. Keep `SKILL.md` and `references/outline-format.md` together. Reload skills or restart the client if required. Do not copy only the entrypoint file.

For versioned installation, use a published GitHub Release/tag once available. The current checkout's changelog does not prove that a Release exists.

## Configure MCP and authorize

1. Open the client's supported remote MCP configuration interface.
2. Add `https://api.exceldashboard.ai/mcp` as a Streamable HTTP server.
3. Complete the server's browser OAuth flow and select the workspace for report creation.
4. Confirm that the authorized connection discovers `create_report` and `get_report`.
5. Ask the agent to load the report skill. Tool discovery alone does not prove the skill was installed.

Use the current [official client guides](https://www.exceldashboard.ai/mcp/guides) for exact configuration fields. Do not paste access tokens into chat or repository Issues.

Suggested setup prompt:

> Install the ExcelDashboard AI report skill from https://github.com/AlgForce/exceldashboard-skills, directory skills/exceldashboard-report, using this client's supported skill installation workflow. Configure remote MCP at https://api.exceldashboard.ai/mcp with Streamable HTTP, guide me through browser OAuth and workspace selection, and verify create_report and get_report are discovered on that connection. Do not create a report during setup. Explain any unsupported steps and do not claim persistent installation or connection merely from reading documentation.

If your client can load instructions only for the current conversation, it may follow the complete Skill and outline reference for that session; that is not persistent installation. If it cannot support remote MCP or the OAuth flow, use a supported client before attempting tool calls.

## Client verification status

Reviewed on 2026-10-09. This table describes available evidence, not certification.

| Client | Evidence | Status |
|---|---|---|
| WorkBuddy | Website `mcp.md`, reviewed 2026-10-07, reports connection and generation verified in existing tests; exact client version was not recorded | Reported by product documentation; not rerun for this GitHub package |
| Other agent clients | No versioned end-to-end result is included in this repository | Unverified |

A confirmed result should record the client version, OS, skill source/revision, connection method, test date, tool discovery, and a completed synthetic report job. Do not publish tokens or private report URLs as evidence.

## Try a synthetic example

Choose an [example](../examples/README.md), attach its `data.csv`, and send its prompt. This requests a hosted report and may consume credits. Alternatively, inspect `outline.md` and reproduce the numbers locally:

```bash
python3 scripts/verify_examples.py
```

Run that command from the repository root. Submit the complete outline as `create_report.outline` with `locale: "en"` only when report generation is requested. Save the returned job ID, open the returned report URL, and follow the polling interval until `completed` or `failed`.

## Troubleshooting

| Symptom | Check or action |
|---|---|
| Skill is not discovered | Confirm the client's skill directory, complete folder structure, and reload requirements |
| MCP tools are absent | Confirm the endpoint, remote transport support, OAuth completion, and server-specific tool discovery |
| Authorization fails | Reconnect in the client and select the intended workspace |
| `INVALID_ARGUMENT` | Check the complete outline against the [format reference](../skills/exceldashboard-report/references/outline-format.md) |
| Creation times out | Query the known job ID; if none was returned, resolve the uncertain submission before creating another job |
| Preview link appears while generation is running | Continue tracking; only `completed` proves success |
| No internal preview opens | Open the returned link manually; automatic internal opening requires client browser tools |
