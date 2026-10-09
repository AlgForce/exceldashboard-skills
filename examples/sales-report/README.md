# Sales Performance Review

Synthetic example for July–September 2026. No real customer data is included.

## Files and prompt

- [data.csv](data.csv): source aggregates for the agent to analyze.
- [outline.md](outline.md): complete four-page example outline for `create_report`.

Attach `data.csv` to your agent and send:

> Analyze the attached synthetic sales CSV and create a four-page English sales performance report with ExcelDashboard AI. Include a data overview, definitions, a monthly revenue chart, and closing actions. Calculate quarterly revenue, July-to-September growth, and each product’s revenue share. State that these aggregates do not establish the causes of growth.

Install the skill and authorize MCP using the [installation guide](../../docs/installation.md). Generating a hosted report may consume credits. Supply the complete outline with `locale: "en"` if submitting it directly; do not pass a local filename as the outline string.

## Expected calculations

| Metric | Expected value | Calculation or scope |
|---|---|---|
| Revenue | USD 36,000 | Sum of all monthly product revenue |
| July-to-September growth | 40.00% | (14,000 - 10,000) / 10,000; not quarter-over-quarter |
| Pro revenue share | 66.67% | USD 24,000 / USD 36,000 |

Run `python3 scripts/verify_examples.py` from the repository root to reproduce these calculations.

## Definitions and limitations

- **Source and grain:** Synthetic data.csv; one row per month and product.
- **Scope and units:** July–September 2026; USD revenue and units sold.
- **Revenue:** Revenue supplied in the CSV; sum across months/products.
- **Growth and share:** Growth uses July baseline; Pro share uses quarterly total.
- **Limitations:** No costs, customer detail, refunds, or earlier quarter baseline.

Percentages are calculated before rounding and displayed to two decimal places. These observations do not establish causes or forecast future performance.

## Report output

The outline contains an overview, definitions, one monthly analysis chart, and closing actions. A hosted report and screenshot have not been generated as part of this repository example. After a real run completes, use the returned `report_url` to inspect the output; do not infer completion from the existence of a link.

[Explore ExcelDashboard AI reporting](https://www.exceldashboard.ai/mcp?utm_source=github&utm_medium=referral&utm_campaign=skills_launch&utm_content=sales-report) · [All examples](../README.md)
