# Agency Client Performance Review

> Synthetic demonstration data for July–September 2026; not a real customer report.

<!-- meta
goal: Validate campaign efficiency before testing a budget change
skill: agency-client-review
style: default
lang: business
pages: 4
audience: Client marketing lead
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
  | Ad spend | USD 30,000 | Total July–September media spend |
  | Attributed ROAS | 3.50x | USD 105,000 attributed revenue / USD 30,000 spend |
  | Cost per conversion | USD 40.00 | USD 30,000 spend / 750 conversions |
  Evidence: Attributed revenue rose from USD 30,000 to USD 40,000 at unchanged monthly spend; monthly CPA fell from USD 50.00 to USD 33.33.
  Attribution: Aggregate attributed results do not isolate channel drivers or establish incremental revenue.
  Recommendation: Validate attribution and channel breakdowns before a controlled budget test.

---

## Data definitions
`layout: Specification Sheet`
`layout_intent: Make the source, grain, units, formulas, and limitations explicit.`
`layout_slots: spec-body`

- [slot: spec-body] Measurement scope [smart_layout]
  | Definition | Value |
  |---|---|
  | Source and grain | Synthetic data.csv; one row per calendar month |
  | Scope and units | July–September 2026; USD and conversion counts |
  | Attribution | Fixed 7-day click window assumed for this demonstration |
  | Formulas | ROAS = attributed revenue / spend; CPA = spend / conversions |
  | Limitations | Agency fees, organic revenue, refunds, and incremental lift excluded |
  Footnote: Figures are synthetic and rounded for display. Aggregate observations do not establish causes or predict future performance.

---

## Attributed ROAS increased from 3.00x to 4.00x
`layout: Single-Chart Insight`
`layout_intent: Show the monthly trend supporting the main analytical finding.`
`layout_slots: main-chart`

- [slot: main-chart] Monthly trend [chart: line]
  | Month | Attributed ROAS (x) |
  |---|---|
  | 2026-07 | 3.00x |
  | 2026-08 | 3.50x |
  | 2026-09 | 4.00x |
  - [hint: Monthly spend remained USD 10,000; quarterly ROAS was 3.50x.]
  Evidence: Attributed revenue rose from USD 30,000 to USD 40,000 at unchanged monthly spend; monthly CPA fell from USD 50.00 to USD 33.33.
  Attribution: Aggregate attributed results do not isolate channel drivers or establish incremental revenue.
  Recommendation: Validate attribution and channel breakdowns before a controlled budget test.

---

## Validate the findings before committing resources
`layout: Closing Statement`
`layout_intent: Connect measured findings to practical actions with named owners.`
`layout_slots: takeaways`

- [slot: takeaways] Findings and next steps [smart_layout]
  Findings:
  01. Quarterly attributed revenue was USD 105,000 on USD 30,000 spend, yielding 3.50x ROAS.
  02. Quarterly conversions totaled 750, giving USD 40.00 cost per conversion.
  03. July-to-September attributed revenue increased 33.33%; the cause and incremental lift remain unverified.
  Actions:
  P1. Marketing lead: check attribution windows, refunds, and conversion definitions.
  P2. Agency analyst: compare channel and campaign results under consistent definitions.
  P3. Account lead: agree on a controlled budget test after validation.
  Goal: Validate campaign efficiency before testing a budget change
