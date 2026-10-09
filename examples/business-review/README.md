# Executive Business Review

Synthetic example for July–September 2026. No real customer data is included.

## Files and prompt

- [data.csv](data.csv): source aggregates for the agent to analyze.
- [outline.md](outline.md): complete four-page example outline for `create_report`.

Attach `data.csv` to your agent and send:

> Analyze the attached synthetic business CSV and create a four-page English executive business review with ExcelDashboard AI. Include a data overview, definitions, a monthly revenue chart, and closing actions. Calculate quarterly revenue target attainment, the dollar target gap, and contribution margin from totals. Define contribution as revenue minus the supplied operating costs; do not describe it as net profit.

Install the skill and authorize MCP using the [installation guide](../../docs/installation.md). Generating a hosted report may consume credits. Supply the complete outline with `locale: "en"` if submitting it directly; do not pass a local filename as the outline string.

## Expected calculations

| Metric | Expected value | Calculation or scope |
|---|---|---|
| Revenue | USD 330,000 | Quarterly revenue against USD 350,000 target |
| Revenue target attainment | 94.29% | USD 330,000 / USD 350,000; gap USD -20,000 |
| Contribution margin | 31.82% | USD 105,000 contribution / USD 330,000 revenue |

Run `python3 scripts/verify_examples.py` from the repository root to reproduce these calculations.

## Definitions and limitations

- **Source and grain:** Synthetic data.csv; one row per calendar month.
- **Scope and units:** July–September 2026; all monetary values in USD.
- **Attainment and gap:** Total revenue / total target; gap = revenue - target.
- **Contribution:** Revenue minus supplied operating costs; margin = contribution / revenue.
- **Limitations:** Cost scope is illustrative; contribution is not audited net profit.

Percentages are calculated before rounding and displayed to two decimal places. These observations do not establish causes or forecast future performance.

## Report output

The outline contains an overview, definitions, one monthly analysis chart, and closing actions. A hosted report and screenshot have not been generated as part of this repository example. After a real run completes, use the returned `report_url` to inspect the output; do not infer completion from the existence of a link.

[Explore ExcelDashboard AI reporting](https://www.exceldashboard.ai/mcp?utm_source=github&utm_medium=referral&utm_campaign=skills_launch&utm_content=business-review) · [All examples](../README.md)
