# Reproducible analytical report examples

These examples use synthetic data for July–September 2026. They demonstrate input, metric definitions, and complete report outlines; they are not customer results or completed MCP job evidence.

| Example | Primary metrics |
|---|---|
| [Sales performance](sales-report/README.md) | Revenue, period growth, product share |
| [Agency client report](agency-report/README.md) | Attributed ROAS, conversions, cost per conversion |
| [Executive business review](business-review/README.md) | Revenue attainment, contribution, contribution margin |

Each directory includes `data.csv`, a README with a copyable prompt, and a four-page `outline.md`. Recalculate all examples from the repository root with `python3 scripts/verify_examples.py`. No hosted service or third-party Python package is needed for that check.

For generation, install the skill and authorize MCP using the [installation guide](../docs/installation.md). Attach the CSV and request the report with the example prompt. Alternatively, submit the complete outline with `locale: "en"` after requesting generation. Hosted generation can consume service credits.

To publish output evidence later, run a real synthetic report job, check its completed status, and add screenshots with the generation date and tested client version. Review the preview's public visibility before publishing its URL. Do not use a mockup as a generated report screenshot.
