"""Tests for collate_job_evaluations helpers."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import collate_job_evaluations as cj  # noqa: E402


def test_group_key_for_report_standard() -> None:
    assert cj.group_key_for_report(Path("UX Designer, Riot Games.eval.md")) == "UX Designer, Riot Games"
    assert cj.group_key_for_report(Path("UX Designer, Riot Games.eval - 2026-04-16.md")) == "UX Designer, Riot Games"
    assert cj.group_key_for_report(Path("UX Designer, Riot Games.eval - 2026-04-16 - 2.md")) == "UX Designer, Riot Games"


def test_group_key_for_report_malformed() -> None:
    assert cj.group_key_for_report(Path("not_an_eval_report.md")) is None
    assert cj.group_key_for_report(Path("weird.evalX.md")) is None


def test_choose_latest_per_group_by_mtime(tmp_path: Path) -> None:
    import os
    import time

    base = "Role A"
    older = tmp_path / f"{base}.eval - 2020-01-01.md"
    newer = tmp_path / f"{base}.eval.md"
    older.write_text("# old\n", encoding="utf-8")
    newer.write_text("# new\n", encoding="utf-8")

    t = time.time()
    os.utime(older, (t - 100, t - 100))
    os.utime(newer, (t, t))

    chosen = cj.choose_latest_per_group([older, newer])
    assert chosen[base] == newer


def test_verdict_line_to_table_cell_strips_labels() -> None:
    assert (
        cj.verdict_line_to_table_cell("- **Fit on paper**: High", "Fit on Paper") == "High"
    )
    assert (
        cj.verdict_line_to_table_cell(
            "- **Actual capability (inferred)**: Medium-High", "Capability"
        )
        == "Medium–High"
    )
    assert (
        cj.verdict_line_to_table_cell(
            "- **Likelihood of recruiter screen**: Low", "Recruiter Screen"
        )
        == "Low"
    )


def test_rating_only_for_summary_drops_tail_prose() -> None:
    assert cj.rating_only_for_summary("High") == "High"
    assert cj.rating_only_for_summary("Medium–High (notes here)") == "Medium–High"
    assert cj.rating_only_for_summary("High for senior game UX work") == "High"
    assert cj.rating_only_for_summary("Medium-High. More text.") == "Medium–High"


def test_rating_only_for_summary_picks_highest_of_multiple() -> None:
    s = (
        "Medium–High for game UX leadership; Medium for mobile CoD-specific execution."
    )
    assert cj.rating_only_for_summary(s) == "Medium–High"
    assert cj.rating_only_for_summary("Medium for A; High for B") == "High"
    assert cj.rating_only_for_summary("Unknown (x); Medium (y)") == "Medium"


def test_verdict_line_long_bullet_is_rating_only() -> None:
    line = (
        "- **Fit on paper:** **Medium–High** (strong years + portfolio; weaker on mobile)."
    )
    assert cj.verdict_line_to_table_cell(line, "Fit on Paper") == "Medium–High"


def test_extract_part5_and_verdicts() -> None:
    text = """# x

### PART 5 — Combined verdict

- **Fit on paper**: Good.
- **Actual capability**: OK.
- **Likelihood of recruiter screen**: Maybe.
- **Likelihood of hiring manager screen**: Fine.
- **Likelihood of panel loop survival**: Low.

#### 3 strongest reasons

### PART 6 — Rubric
"""
    part5 = cj.extract_part5_section(text)
    assert "Fit on paper" in part5
    assert "PART 6" not in part5
    verdicts = cj.extract_verdict_lines(part5)
    assert len(verdicts) == 5
    assert "Fit on Paper" in verdicts


def test_extract_verdict_lines_bold_paragraphs_without_list_markers() -> None:
    """Some eval reports use bold paragraphs for PART 5 verdicts instead of markdown list bullets."""
    part5 = """
## PART 5 — Combined verdict

**Fit on paper:** **High** (notes)

**Actual capability (inferred):** **Medium–High** (notes)

**Likelihood of recruiter screen:** **Low**

**Likelihood of hiring manager screen:** **Fine**

**Likelihood of panel loop survival:** **Medium**

#### Three strongest reasons
"""
    verdicts = cj.extract_verdict_lines(part5)
    assert len(verdicts) == 5
    assert "Fit on Paper" in verdicts
    assert verdicts["Fit on Paper"].startswith("**Fit on paper:**")


def test_snapshot_and_mutation(tmp_path: Path) -> None:
    jd = "Test Role"
    r = tmp_path / f"{jd}.eval.md"
    r.write_text("x", encoding="utf-8")
    before = cj.snapshot_reports_for_jd(tmp_path, jd)
    r.write_text("updated", encoding="utf-8")
    after = cj.snapshot_reports_for_jd(tmp_path, jd)
    assert cj.report_mutation_detected(before, after) is True


def test_snapshot_new_file(tmp_path: Path) -> None:
    jd = "Another"
    before = cj.snapshot_reports_for_jd(tmp_path, jd)
    p = tmp_path / f"{jd}.eval.md"
    p.write_text("new", encoding="utf-8")
    after = cj.snapshot_reports_for_jd(tmp_path, jd)
    assert cj.report_mutation_detected(before, after) is True


def test_any_eval_report_exists_for_jd(tmp_path: Path) -> None:
    jd = "X"
    assert cj.any_eval_report_exists_for_jd(tmp_path, jd) is False
    (tmp_path / f"{jd}.eval - 2026-01-02.md").write_text("a", encoding="utf-8")
    assert cj.any_eval_report_exists_for_jd(tmp_path, jd) is True


def test_allocate_overview_path_unique(tmp_path: Path) -> None:
    p1 = cj.allocate_overview_path(tmp_path, 3)
    assert p1.name.startswith("_OVERVIEW-")
    assert p1.name.endswith("(3).md")
    p1.write_text("x", encoding="utf-8")
    p2 = cj.allocate_overview_path(tmp_path, 3)
    assert p1 != p2
    assert p2.name.endswith("(3)-1.md")


def test_allocate_overview_path_singular_record(tmp_path: Path) -> None:
    p = cj.allocate_overview_path(tmp_path, 1)
    assert p.name.endswith("(1).md")


def test_tier_cell_to_numeric() -> None:
    assert cj.tier_cell_to_numeric("High") == 99.0
    assert cj.tier_cell_to_numeric("Medium–High") == 98.0
    assert cj.tier_cell_to_numeric("Medium") == 97.0
    assert cj.tier_cell_to_numeric("Unknown") == 95.0
    assert cj.tier_cell_to_numeric("TBD") == 93.0
    assert cj.tier_cell_to_numeric("") is None
    assert cj.tier_cell_to_numeric("Good") is None


def test_build_collated_rows_one_report(tmp_path: Path) -> None:
    jd = "Role X"
    (tmp_path / f"{jd}.eval.md").write_text(
        """# Header metadata
- `job`: Test Job

### PART 5 — Combined verdict

- **Fit on paper:** **High**
- **Actual capability (inferred):** **Medium**
- **Likelihood of recruiter screen:** **Low**
- **Likelihood of hiring manager screen:** **Medium**
- **Likelihood of panel loop survival:** **High**

### PART 6 — x
""",
        encoding="utf-8",
    )
    rows = cj.build_collated_rows(tmp_path, tmp_path)
    assert len(rows) == 1
    assert rows[0].jd_key == jd


def test_warn_unparsed_eval_markdown(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    (tmp_path / "bad.eval.extra.md").write_text("x", encoding="utf-8")
    cj.warn_unparsed_eval_markdown(tmp_path)
    err = capsys.readouterr().err
    assert "unparsed" in err
    assert "bad.eval.extra.md" in err


def test_write_overview_chart_html_smoke(tmp_path: Path) -> None:
    pytest.importorskip("plotly")
    jd = "Role Viz"
    (tmp_path / f"{jd}.eval.md").write_text(
        """### PART 5 — Combined verdict
- **Fit on paper:** **High**
- **Actual capability (inferred):** **Medium**
- **Likelihood of recruiter screen:** **Medium**
- **Likelihood of hiring manager screen:** **Medium**
- **Likelihood of panel loop survival:** **Medium**
### PART 6
""",
        encoding="utf-8",
    )
    rows = cj.build_collated_rows(tmp_path, tmp_path)
    import job_eval_overview_html as viz

    out = tmp_path / "dash.html"
    viz.write_overview_chart_html(out, rows, tmp_path, "job-evaluation-reports/test.md")
    text = out.read_text(encoding="utf-8")
    assert "plotly" in text.lower()
    assert "Heatmap" in text
