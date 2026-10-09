# Sales Performance Review

> Synthetic demonstration data for July–September 2026; not a real customer report.

<!-- meta
goal: Review revenue growth and decide which product segments to investigate
skill: sales-performance-review
style: default
lang: business
pages: 4
audience: Sales lead
date_range: 2026-07-01 to 2026-09-30
generated: 2026-10-09
-->

---

## Data overview
`layout: KPI Ledger`
`layout_intent: Summarize verified quarterly metrics before reviewing scope and definitions.`
`layout_slots: kpi-summary`

- [slot: kpi-summary] Quarterly performance [smart_layout]
  | Metric | Current value | Description |
  |---|---|---|
  | Revenue | USD 36,000 | Sum of all monthly product revenue |
  | July-to-September growth | 40.00% | (14,000 - 10,000) / 10,000; not quarter-over-quarter |
  | Pro revenue share | 66.67% | USD 24,000 / USD 36,000 |
  Evidence: Revenue rose from USD 10,000 in July to USD 14,000 in September; Pro revenue increased by USD 4,000 while Standard stayed at USD 4,000 each month.
  Attribution: The increase is arithmetically concentrated in Pro; these data do not explain demand, acquisition, or profitability.
  Recommendation: Inspect customer and cost breakdowns before expanding Pro investment.

---

## Data definitions
`layout: Specification Sheet`
`layout_intent: Make the source, grain, units, formulas, and limitations explicit.`
`layout_slots: spec-body`

- [slot: spec-body] Measurement scope [smart_layout]
  | Definition | Value |
  |---|---|
  | Source and grain | Synthetic data.csv; one row per month and product |
  | Scope and units | July–September 2026; USD revenue and units sold |
  | Revenue | Revenue supplied in the CSV; sum across months/products |
  | Growth and share | Growth uses July baseline; Pro share uses quarterly total |
  | Limitations | No costs, customer detail, refunds, or earlier quarter baseline |
  Footnote: Figures are synthetic and rounded for display. Aggregate observations do not establish causes or predict future performance.

---

## Monthly revenue rose 40% from July to September
`layout: Single-Chart Insight`
`layout_intent: Show the monthly trend supporting the main analytical finding.`
`layout_slots: main-chart`

- [slot: main-chart] Monthly trend [chart: line]
  | Month | Revenue (USD) |
  |---|---|
  | 2026-07 | 10,000 USD |
  | 2026-08 | 12,000 USD |
  | 2026-09 | 14,000 USD |
  - [hint: September revenue was USD 14,000 versus USD 10,000 in July.]
  Evidence: Revenue rose from USD 10,000 in July to USD 14,000 in September; Pro revenue increased by USD 4,000 while Standard stayed at USD 4,000 each month.
  Attribution: The increase is arithmetically concentrated in Pro; these data do not explain demand, acquisition, or profitability.
  Recommendation: Inspect customer and cost breakdowns before expanding Pro investment.

---

## Validate the findings before committing resources
`layout: Closing Statement`
`layout_intent: Connect measured findings to practical actions with named owners.`
`layout_slots: takeaways`

- [slot: takeaways] Findings and next steps [smart_layout]
  Findings:
  01. Quarterly revenue totaled USD 36,000 across 360 units sold.
  02. Pro contributed USD 24,000 (66.67%) of quarterly revenue and all USD 4,000 of the July-to-September increase.
  03. The 40.00% growth figure compares July with September, not two quarters.
  Actions:
  P1. Sales lead: review Pro customer segments and repeat purchases.
  P2. Finance lead: validate costs and refunds before assessing profitability.
  P3. Analyst: obtain prior-quarter data for a comparable quarterly baseline.
  Goal: Review revenue growth and decide which product segments to investigate
