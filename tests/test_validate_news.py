"""News metadata validation must preserve the source CSV."""

import pandas as pd
import pytest

from src.validate_news import validate_news


def test_rejects_overwriting_source_file(tmp_path):
    source = tmp_path / "news.csv"
    source.write_text("title,author,url\nHeadline,Writer,https://example.com\n")
    original = source.read_bytes()
    with pytest.raises(ValueError, match="output path must differ"):
        validate_news(source, source)
    assert source.read_bytes() == original


def test_deduplicates_trimmed_records_and_exports_only_valid_metadata(tmp_path):
    source = tmp_path / "news.csv"
    source.write_text("title,author\n Headline ,A\nHeadline,A\n ,B\nOther,C\n")
    output = tmp_path / "processed" / "news.csv"
    report = validate_news(source, output)
    assert report == {
        "input_rows": 4,
        "incomplete_rows_removed": 1,
        "duplicate_rows_removed": 1,
        "valid_rows": 2,
        "valid_row_rate": 0.5,
        "unique_authors": 2,
    }
    assert pd.read_csv(output).to_dict("records") == [
        {"title": "Headline", "author": "A"},
        {"title": "Other", "author": "C"},
    ]


def test_missing_required_columns_raise_explicit_error(tmp_path):
    source = tmp_path / "news.csv"
    source.write_text("title\nHeadline\n")
    with pytest.raises(ValueError, match="Missing required columns"):
        validate_news(source)
