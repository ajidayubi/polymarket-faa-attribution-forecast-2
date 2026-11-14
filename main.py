"""Empirical horizon-quantile forecaster for Polymarket prices.

Reads one makefun/polymarket-case/v1 case per *.in file and writes a
five-quantile forecast for every market and every minute of the 240-minute
horizon. The median stays at the last price; the spread comes from the
empirical distribution of past h-step price changes over the trailing 48
hours of one-minute prices.
"""

import json
import os

LEVELS = (0.05, 0.25, 0.5, 0.75, 0.95)
HORIZON = 240
WINDOW = 2880
SCALE = 0.90


def _quantile(ordered, level):
    count = len(ordered)
    if count == 1:
        return ordered[0]
    spot = level * (count - 1)
    low = int(spot)
    high = low + 1
    if high >= count:
        return ordered[-1]
    part = spot - low
    return ordered[low] + part * (ordered[high] - ordered[low])


def _clip(value):
    if value < 0.0:
        return 0.0
    if value > 1.0:
        return 1.0
    return value


def forecast_market(prices):
    if len(prices) <= 1:
        raise ValueError("cannot forecast a market with fewer than two prices")
    last = prices[-1]
    window = prices[-WINDOW:]
    size = len(window)
    rows = []
    for step in range(1, HORIZON + 1):
        use = step if step < size else size - 1
        moves = sorted(window[t] - window[t - use] for t in range(use, size))
        shifts = [_quantile(moves, level) for level in LEVELS]
        middle = shifts[2]
        row = []
        for shift in shifts:
            row.append(round(_clip(last + SCALE * (shift - middle)), 6))
        row.sort()
        rows.append(row)
    return rows


def forecast_case(case):
    found = []
    for market in case["markets"]:
        found.append({"id": market["id"], "q": forecast_market(market["prices"])})
    return {"forecasts": found}


def main():
    in_dir = os.environ.get("MAKEFUN_INPUT_DIR", "/input")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    for name in sorted(os.listdir(in_dir)):
        if not name.endswith(".in"):
            continue
        with open(os.path.join(in_dir, name), "r", encoding="utf-8") as handle:
            case = json.load(handle)
        result = forecast_case(case)
        stem = name[:-3]
        path = os.path.join(out_dir, stem + ".out")
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(json.dumps(result, separators=(",", ":")))


if __name__ == "__main__":
    main()
