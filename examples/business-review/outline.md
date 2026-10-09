# Executive Business Review

> Synthetic demonstration data for July–September 2026; not a real customer report.

<!-- meta
goal: Close the revenue target gap while verifying contribution economics
skill: executive-business-review
style: default
lang: business
pages: 4
audience: Executive operating team
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
  | Revenue | USD 330,000 | Quarterly revenue against USD 350,000 target |
  | Revenue target attainment | 94.29% | USD 330,000 / USD 350,000; gap USD -20,000 |
  | Contribution margin | 31.82% | USD 105,000 contribution / USD 330,000 revenue |
  Evidence: Quarterly revenue was USD 330,000 versus USD 350,000 target; August and September each missed by USD 10,000.
  Attribution: Rising revenue alone did not meet the target trajectory; these aggregates do not identify the cause of the gap.
  Recommendation: Review pipeline and cost coverage before agreeing on a recovery plan.

---

## Data definitions
`layout: Specification Sheet`
`layout_intent: Make the source, grain, units, formulas, and limitations explicit.`
`layout_slots: spec-body`

- [slot: spec-body] Measurement scope [smart_layout]
  | Definition | Value |
  |---|---|
  | Source and grain | Synthetic data.csv; one row per calendar month |
  | Scope and units | July–September 2026; all monetary values in USD |
  | Attainment and gap | Total revenue / total target; gap = revenue - target |
  | Contribution | Revenue minus supplied operating costs; margin = contribution / revenue |
  | Limitations | Cost scope is illustrative; contribution is not audited net profit |
  Footnote: Figures are synthetic and rounded for display. Aggregate observations do not establish causes or predict future performance.

---

## Revenue rose while the quarterly target gap reached USD 20,000
`layout: Single-Chart Insight`
`layout_intent: Show the monthly trend supporting the main analytical finding.`
`layout_slots: main-chart`

- [slot: main-chart] Monthly trend [chart: line]
  | Month | Revenue (USD) |
  |---|---|
  | 2026-07 | 100,000 USD |
  | 2026-08 | 110,000 USD |
  | 2026-09 | 120,000 USD |
  - [hint: Monthly targets were USD 100,000, USD 120,000, and USD 130,000 respectively.]
  Evidence: Quarterly revenue was USD 330,000 versus USD 350,000 target; August and September each missed by USD 10,000.
  Attribution: Rising revenue alone did not meet the target trajectory; these aggregates do not identify the cause of the gap.
  Recommendation: Review pipeline and cost coverage before agreeing on a recovery plan.

---

## Validate the findings before committing resources
`layout: Closing Statement`
`layout_intent: Connect measured findings to practical actions with named owners.`
`layout_slots: takeaways`

- [slot: takeaways] Findings and next steps [smart_layout]
  Findings:
  01. Revenue attainment was 94.29%, with a signed gap of USD -20,000 (-5.71% of target).
  02. Supplied operating costs totaled USD 225,000; contribution was USD 105,000 at a 31.82% margin.
  03. Revenue rose 20.00% from July to September, but August and September remained below target.
  Actions:
  P1. Sales lead: inspect pipeline timing and identify opportunities addressing the gap.
  P2. Finance lead: confirm cost coverage before using contribution for investment decisions.
  P3. Operating lead: assign owners and review recovery progress next month.
  Goal: Close the revenue target gap while verifying contribution economics
