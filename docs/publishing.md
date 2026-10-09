# GitHub publication and website integration

## Repository settings

Recommended About description:

> Official ExcelDashboard AI agent skills for analyzing Excel/CSV data and generating visual reports through MCP.

Website: `https://www.exceldashboard.ai/mcp`

Suggested topics: `agent-skills`, `mcp`, `excel`, `csv`, `data-analysis`, `ai-reporting`.

These settings improve project presentation and GitHub discovery; they do not guarantee search ranking or AI citations.

## Release preparation

- Review the files and Git history for unpublished material before changing visibility.
- Run `python3 scripts/verify_examples.py` and check documentation links.
- Verify GitHub installation and a synthetic MCP report on a named client version; record the result in the installation guide.
- Resolve the product naming and distribution-version mapping with the website/SkillHub documentation.
- Move the relevant changelog entries into the chosen version section, then publish that tag and Release. Do not reuse a SkillHub version number without confirming equivalent package contents.

Suggested release title: `ExcelDashboard AI Skills — GitHub reporting examples`.

Suggested release body:

> Official ExcelDashboard AI report skill with installation guidance and three reproducible synthetic examples: sales performance, agency client reporting, and executive business review. Agents verify the data and prepare an outline; the MCP server creates the visual report and returns a live preview.
>
> Skill installation and MCP OAuth are separate steps. Hosted report creation requires an account and is governed by service limits and terms. See the installation guide for verification status.

## Website integration

The website changes below are a handoff for its source repository; this document does not change the deployed site.

| Existing surface | Recommended change |
|---|---|
| Homepage MCP & Skills section | Add the official GitHub repository alongside the existing setup and SkillHub links |
| `/mcp` | Add a GitHub installation section with the repository URL, skill path, and separate OAuth steps |
| `/mcp/guides` | Link to the GitHub installation guide and report client verification status consistently |
| `/mcp.md` | State the GitHub source/path and distinguish its revision from the existing SkillHub package |
| `/mcp/examples/agency-report` | Link to the matching CSV and outline; reconcile any differing figures explicitly |

Keep existing SkillHub installations usable while introducing the GitHub channel. Preserve its identifier as a distribution identifier, and explain the product name consistently. Avoid implying that both channels contain identical revisions until verified.

Suggested website link labels: “Official GitHub skills”, “Install from GitHub”, and “Download the synthetic example”.

For search discoverability, keep explanatory content visible in HTML, link from the MCP hub to tutorials and cases, and verify indexing, sitemap, canonical URLs, and crawler access. Machine-readable documentation supplements the public pages.

## Attribution and follow-up

README promotional links use `utm_source=github`, `utm_medium=referral`, and `utm_campaign=skills_launch`. Agent endpoint URLs and operational configuration links stay unchanged.

Record a prelaunch baseline, then compare at 30, 60, and 90 days: indexed documentation pages, search impressions/clicks, GitHub referral sessions, successful MCP connections, and first completed reports. If measuring AI citations, keep a fixed question set and record the platform, date, response, cited URL, and accuracy; results vary by query and session.

Submit actual tutorials or usable examples to relevant maintained directories and communities according to their rules. Do not create duplicate repositories or low-value pages solely to manufacture links.
