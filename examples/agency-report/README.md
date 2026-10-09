# Agency Client Performance Review

Synthetic example for July–September 2026. No real customer data is included.

## Files and prompt

- [data.csv](data.csv): source aggregates for the agent to analyze.
- [outline.md](outline.md): complete four-page example outline for `create_report`.

Attach `data.csv` to your agent and send:

> Analyze the attached synthetic campaign CSV and create a four-page English agency client report with ExcelDashboard AI. Include a data overview, definitions, a monthly ROAS chart, and closing actions. Calculate quarterly ROAS and cost per conversion using totals, not unweighted monthly ratio averages. Use a fixed 7-day click attribution assumption, and explain that attributed revenue does not prove incremental lift.

Install the skill and authorize MCP using the [installation guide](../../docs/installation.md). Generating a hosted report may consume credits. Supply the complete outline with `locale: "en"` if submitting it directly; do not pass a local filename as the outline string.

## Expected calculations

| Metric | Expected value | Calculation or scope |
|---|---|---|
| Ad spend | USD 30,000 | Total July–September media spend |
| Attributed ROAS | 3.50x | USD 105,000 attributed revenue / USD 30,000 spend |
| Cost per conversion | USD 40.00 | USD 30,000 spend / 750 conversions |

Run `python3 scripts/verify_examples.py` from the repository root to reproduce these calculations.

## Definitions and limitations

- **Source and grain:** Synthetic data.csv; one row per calendar month.
- **Scope and units:** July–September 2026; USD and conversion counts.
- **Attribution:** Fixed 7-day click window assumed for this demonstration.
- **Formulas:** ROAS = attributed revenue / spend; CPA = spend / conversions.
- **Limitations:** Agency fees, organic revenue, refunds, and incremental lift excluded.

Percentages are calculated before rounding and displayed to two decimal places. These observations do not establish causes or forecast future performance.

## Report output

The outline contains an overview, definitions, one monthly analysis chart, and closing actions. A hosted report and screenshot have not been generated as part of this repository example. After a real run completes, use the returned `report_url` to inspect the output; do not infer completion from the existence of a link.

[Explore ExcelDashboard AI reporting](https://www.exceldashboard.ai/mcp?utm_source=github&utm_medium=referral&utm_campaign=skills_launch&utm_content=agency-report) · [All examples](../README.md)
