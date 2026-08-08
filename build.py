#!/usr/bin/env python3
"""
Build the Coconut AI analysis site.

data/competitors.json is the single source of truth. This script validates it,
writes a CSV export, and injects the JSON inline into competitors.html so the
published page makes zero external requests.

Idempotent: safe to run repeatedly. Re-injection replaces any previously
injected payload.
"""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
DATA = ROOT / "data" / "competitors.json"
PAGE = ROOT / "competitors.html"
CSV_OUT = ROOT / "data" / "competitors.csv"

MARKER = "__COMPETITORS_JSON__"
SCRIPT_RE = re.compile(
    r'(<script id="cdata" type="application/json">)(.*?)(</script>)',
    re.DOTALL,
)

REQUIRED = ["id", "name", "tier", "category", "what", "funding_display",
            "confidence", "threat", "relationship"]
VALID_CONFIDENCE = {"verified", "reported", "thin"}
VALID_THREAT = {"existential", "high", "medium", "low"}


def fail(msg: str) -> None:
    print(f"  FAIL  {msg}", file=sys.stderr)


def validate(db: dict) -> list[str]:
    errors: list[str] = []
    companies = db.get("companies", [])
    tiers = db.get("meta", {}).get("tiers", {})

    if not companies:
        errors.append("no companies in dataset")
    if not tiers:
        errors.append("meta.tiers missing")

    seen_ids: set[str] = set()
    for i, c in enumerate(companies):
        label = c.get("name") or c.get("id") or f"index {i}"

        for field in REQUIRED:
            # Explicit None/"" check: tier 0 is a valid value and must not read as missing.
            val = c.get(field)
            if val is None or (isinstance(val, str) and not val.strip()):
                errors.append(f"{label}: missing required field '{field}'")

        cid = c.get("id", "")
        if cid in seen_ids:
            errors.append(f"{label}: duplicate id '{cid}'")
        seen_ids.add(cid)
        if cid and not re.fullmatch(r"[a-z0-9-]+", cid):
            errors.append(f"{label}: id '{cid}' must be lowercase kebab-case")

        if str(c.get("tier")) not in tiers:
            errors.append(f"{label}: tier {c.get('tier')!r} not defined in meta.tiers")

        if c.get("confidence") not in VALID_CONFIDENCE:
            errors.append(f"{label}: confidence {c.get('confidence')!r} not in {sorted(VALID_CONFIDENCE)}")

        if c.get("threat") not in VALID_THREAT:
            errors.append(f"{label}: threat {c.get('threat')!r} not in {sorted(VALID_THREAT)}")

        f = c.get("funding_usd_m")
        if f is None:
            errors.append(f"{label}: missing funding_usd_m (use 0 for open source)")
        elif not isinstance(f, (int, float)) or f < 0:
            errors.append(f"{label}: funding_usd_m must be a non-negative number, got {f!r}")

        url = c.get("url", "")
        if url and not url.startswith("http"):
            errors.append(f"{label}: url must be absolute, got {url!r}")

    return errors


def write_csv(db: dict) -> int:
    cols = ["id", "name", "tier", "tier_name", "category", "funding_display",
            "funding_usd_m", "status", "owner", "founders", "confidence",
            "threat", "url", "what", "relationship", "coconut_answer"]
    tiers = db["meta"]["tiers"]
    rows = sorted(db["companies"], key=lambda c: (c["tier"], -(c.get("funding_usd_m") or 0)))

    with CSV_OUT.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for c in rows:
            row = dict(c)
            row["tier_name"] = tiers[str(c["tier"])].split(" — ")[0]
            w.writerow(row)
    return len(rows)


def inject(db: dict) -> bool:
    html = PAGE.read_text(encoding="utf-8")
    payload = json.dumps(db, separators=(",", ":"), ensure_ascii=False)

    # Prevent the JSON from terminating its own <script> block.
    payload = payload.replace("</", "<\\/")

    if MARKER not in html and not SCRIPT_RE.search(html):
        fail("could not find the data <script id=\"cdata\"> block in competitors.html")
        return False

    new_html, n = SCRIPT_RE.subn(
        lambda m: m.group(1) + payload + m.group(3), html, count=1
    )
    if n != 1:
        fail("data script block did not match exactly once")
        return False

    if new_html == html:
        print("  ok    competitors.html already current")
        return True

    PAGE.write_text(new_html, encoding="utf-8")
    return True


def main() -> int:
    if not DATA.exists():
        fail(f"{DATA} not found")
        return 1
    if not PAGE.exists():
        fail(f"{PAGE} not found")
        return 1

    db = json.loads(DATA.read_text(encoding="utf-8"))

    errors = validate(db)
    if errors:
        print(f"\nValidation failed with {len(errors)} error(s):\n", file=sys.stderr)
        for e in errors:
            fail(e)
        return 1

    companies = db["companies"]
    print(f"  ok    {len(companies)} companies validated")

    by_tier: dict[str, int] = {}
    by_conf: dict[str, int] = {}
    for c in companies:
        key = db["meta"]["tiers"][str(c["tier"])].split(" — ")[0]
        by_tier[key] = by_tier.get(key, 0) + 1
        by_conf[c["confidence"]] = by_conf.get(c["confidence"], 0) + 1

    for k, v in by_tier.items():
        print(f"        {v:>3}  {k}")
    print("  ok    confidence: " + ", ".join(f"{k}={v}" for k, v in sorted(by_conf.items())))

    n = write_csv(db)
    print(f"  ok    wrote {CSV_OUT.relative_to(ROOT)} ({n} rows)")

    if not inject(db):
        return 1
    size_kb = PAGE.stat().st_size / 1024
    print(f"  ok    injected data into {PAGE.relative_to(ROOT)} ({size_kb:.0f} KB)")
    print("\nBuild complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
