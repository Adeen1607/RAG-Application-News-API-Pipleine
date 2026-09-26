"""Validate and normalize news metadata before indexing."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = ["title", "author"]


def validate_news(path: Path, output: Path | None = None) -> dict[str, int | float]:
    frame = pd.read_csv(path)
    missing_columns = sorted(set(REQUIRED_COLUMNS) - set(frame.columns))
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    selected = frame[REQUIRED_COLUMNS].copy()
    selected["title"] = selected["title"].astype("string").str.strip()
    selected["author"] = selected["author"].astype("string").str.strip()

    input_rows = len(selected)
    incomplete = selected[REQUIRED_COLUMNS].isna().any(axis=1) | (
        selected[REQUIRED_COLUMNS] == ""
    ).any(axis=1)
    incomplete_rows = int(incomplete.sum())

    valid = selected.loc[~incomplete].copy()
    duplicate_rows = int(valid.duplicated(subset=["title", "author"]).sum())
    valid = valid.drop_duplicates(subset=["title", "author"]).reset_index(drop=True)

    report: dict[str, int | float] = {
        "input_rows": input_rows,
        "incomplete_rows_removed": incomplete_rows,
        "duplicate_rows_removed": duplicate_rows,
        "valid_rows": len(valid),
        "valid_row_rate": round(len(valid) / input_rows, 4) if input_rows else 0.0,
        "unique_authors": int(valid["author"].nunique()),
    }

    if output is not None:
        output.parent.mkdir(parents=True, exist_ok=True)
        valid.to_csv(output, index=False)

    print(json.dumps(report, indent=2))
    return report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate news metadata for indexing.")
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


if __name__ == "__main__":
    arguments = parse_args()
    validate_news(arguments.data, arguments.output)
