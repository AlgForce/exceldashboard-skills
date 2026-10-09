#!/usr/bin/env python3
"""Recalculate synthetic example metrics using only the Python standard library."""

import csv
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MONTHS = {"2026-07", "2026-08", "2026-09"}


def load(slug, fields, grain):
    path = ROOT / "examples" / slug / "data.csv"
    with path.open(newline="", encoding="utf-8") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames != fields:
            raise ValueError(f"{path}: unexpected CSV columns")
        rows = list(reader)
    if not rows or {row["month"] for row in rows} != MONTHS:
        raise ValueError(f"{path}: expected all three example months")
    keys = [tuple(row[field] for field in grain) for row in rows]
    if len(keys) != len(set(keys)):
        raise ValueError(f"{path}: duplicate records at the documented grain")
    for row in rows:
        for field in fields:
            if field not in {"month", "product"}:
                value = Decimal(row[field])
                if not value.is_finite() or value < 0:
                    raise ValueError(f"{path}: invalid {field}")
                if field in {"units", "conversions"} and value != value.to_integral_value():
                    raise ValueError(f"{path}: {field} must be an integer count")
    return rows


def total(rows, field):
    return sum((Decimal(row[field]) for row in rows), Decimal(0))


def check(label, actual, expected):
    # Compare before display rounding so changes cannot silently alter the example.
    if actual != Decimal(expected):
        raise ValueError(f"{label}: expected {expected}, calculated {actual}")


def verify_sales():
    rows = load("sales-report", ["month", "product", "revenue_usd", "units"],
                ["month", "product"])
    if {row["product"] for row in rows} != {"Standard", "Pro"} or len(rows) != 6:
        raise ValueError("Sales example: expected two products in each month")
    revenue = total(rows, "revenue_usd")
    units = total(rows, "units")
    monthly = {month: total([r for r in rows if r["month"] == month], "revenue_usd")
               for month in sorted(MONTHS)}
    pro = total([row for row in rows if row["product"] == "Pro"], "revenue_usd")
    check("Sales revenue", revenue, "36000")
    check("Sales units", units, "360")
    check("Pro revenue", pro, "24000")
    for month, expected in zip(sorted(MONTHS), ["10000", "12000", "14000"]):
        check(f"Sales revenue {month}", monthly[month], expected)
    growth = (monthly["2026-09"] - monthly["2026-07"]) / monthly["2026-07"] * 100
    print(f"Sales: revenue USD {revenue:,.0f}; units {units}; "
          f"July–September growth {growth:.2f}%; Pro share {pro / revenue * 100:.2f}%")


def verify_agency():
    rows = load("agency-report", ["month", "ad_spend_usd", "attributed_revenue_usd", "conversions"],
                ["month"])
    spend = total(rows, "ad_spend_usd")
    revenue = total(rows, "attributed_revenue_usd")
    conversions = total(rows, "conversions")
    check("Agency spend", spend, "30000")
    check("Agency attributed revenue", revenue, "105000")
    check("Agency conversions", conversions, "750")
    monthly = {row["month"]: row for row in rows}
    for month, expected_revenue, expected_conversions in zip(
            sorted(MONTHS), ["30000", "35000", "40000"], ["200", "250", "300"]):
        row = monthly[month]
        check(f"Agency spend {month}", Decimal(row["ad_spend_usd"]), "10000")
        check(f"Agency revenue {month}", Decimal(row["attributed_revenue_usd"]), expected_revenue)
        check(f"Agency conversions {month}", Decimal(row["conversions"]), expected_conversions)
        roas = Decimal(row["attributed_revenue_usd"]) / Decimal(row["ad_spend_usd"])
        cpa = Decimal(row["ad_spend_usd"]) / Decimal(row["conversions"])
        print(f"Agency {month}: ROAS {roas:.2f}x; CPA USD {cpa:.2f}")
    print(f"Agency quarter: attributed revenue USD {revenue:,.0f}; "
          f"ROAS {revenue / spend:.2f}x; CPA USD {spend / conversions:.2f}")


def verify_business():
    rows = load("business-review", ["month", "revenue_usd", "revenue_target_usd", "operating_cost_usd"],
                ["month"])
    revenue = total(rows, "revenue_usd")
    target = total(rows, "revenue_target_usd")
    costs = total(rows, "operating_cost_usd")
    check("Business revenue", revenue, "330000")
    check("Business target", target, "350000")
    check("Business costs", costs, "225000")
    monthly = {row["month"]: row for row in rows}
    for month, values in zip(sorted(MONTHS), [
            ("100000", "100000", "70000"),
            ("110000", "120000", "75000"),
            ("120000", "130000", "80000")]):
        for field, expected in zip(["revenue_usd", "revenue_target_usd", "operating_cost_usd"], values):
            check(f"Business {field} {month}", Decimal(monthly[month][field]), expected)
    contribution = revenue - costs
    print(f"Business: attainment {revenue / target * 100:.2f}%; "
          f"gap USD {revenue - target:,.0f} ({(revenue - target) / target * 100:.2f}%); "
          f"contribution USD {contribution:,.0f}; margin {contribution / revenue * 100:.2f}%")


if __name__ == "__main__":
    verify_sales()
    verify_agency()
    verify_business()
    print("All synthetic example calculations verified.")
