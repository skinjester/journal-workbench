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
        == "Medium-High"
    )
    assert (
        cj.verdict_line_to_table_cell(
            "- **Signal strength: Recruiter**: Low", "Signal Strength (Recruiter)"
        )
        == "Low"
    )
    assert (
        cj.verdict_line_to_table_cell(
            "- **Likelihood of recruiter screen**: Low", "Signal Strength (Recruiter)"
        )
        == "Low"
    )


def test_rating_only_for_summary_drops_tail_prose() -> None:
    assert cj.rating_only_for_summary("High") == "High"
    assert cj.rating_only_for_summary("Medium-High (notes here)") == "Medium-High"
    assert cj.rating_only_for_summary("High for senior game UX work") == "High"
    assert cj.rating_only_for_summary("Medium-High. More text.") == "Medium-High"


def test_rating_only_for_summary_takes_first_tier_not_max() -> None:
    s = (
        "Medium-High for game UX leadership; Medium for mobile CoD-specific execution."
    )
    assert cj.rating_only_for_summary(s) == "Medium-High"
    assert cj.rating_only_for_summary("Medium for A; High for B") == "Medium"
    assert cj.rating_only_for_summary("Medium — although craft on the site is High") == "Medium"
    assert cj.rating_only_for_summary("Unknown (x); Medium (y)") == "Unknown"


def test_verdict_line_long_bullet_is_rating_only() -> None:
    line = (
        "- **Fit on paper:** **Medium-High** (strong years + portfolio; weaker on mobile)."
    )
    assert cj.verdict_line_to_table_cell(line, "Fit on Paper") == "Medium-High"


def test_verdict_line_narrative_coherence_column() -> None:
    line = "- **Narrative coherence (for this JD):** **Low** (scattershot proof)."
    assert cj.verdict_line_to_table_cell(line, "Narrative Coherence") == "Low"
    line2 = "- **Narrative coherence:** **High**"
    assert cj.verdict_line_to_table_cell(line2, "Narrative Coherence") == "High"


def test_extract_part5_and_verdicts() -> None:
    text = """# x

### PART 5 — Combined verdict

- **Fit on paper**: High.
- **Actual capability (inferred)**: Medium.
- **Narrative coherence (for this JD)**: Medium.
- **Signal strength: Recruiter**: Low.
- **Signal strength: HM**: High.

#### 3 strongest reasons

### PART 6 — Rubric
"""
    part5 = cj.extract_part5_section(text)
    assert "Fit on paper" in part5
    assert "PART 6" not in part5
    verdicts = cj.extract_verdict_lines(part5)
    assert len(verdicts) == 5
    assert "Fit on Paper" in verdicts
    assert "Narrative Coherence" in verdicts


def test_extract_verdict_lines_bold_paragraphs_without_list_markers() -> None:
    """Some eval reports use bold paragraphs for PART 5 verdicts instead of markdown list bullets."""
    part5 = """
## PART 5 — Combined verdict

**Fit on paper:** **High** (notes)

**Actual capability (inferred):** **Medium-High** (notes)

**Narrative coherence (for this JD):** **Medium**

**Signal strength: Recruiter:** **Low**

**Signal strength: HM:** **Fine**

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
    assert cj.tier_cell_to_numeric("Medium-High") == 98.0
    assert cj.tier_cell_to_numeric("Medium") == 97.0
    assert cj.tier_cell_to_numeric("Medium-Low") == 96.0
    assert cj.tier_cell_to_numeric("Very Low") == 94.0
    assert cj.tier_cell_to_numeric("Unknown") == 93.0
    assert cj.tier_cell_to_numeric("TBD") == 91.0
    assert cj.tier_cell_to_numeric("") is None
    assert cj.tier_cell_to_numeric("Good") is None


def test_tier_cell_to_chart_numeric_uniform_spacing() -> None:
    vals = [
        cj.tier_cell_to_chart_numeric(label) for label in cj.SEVEN_STEP_ORDINALS
    ]
    assert None not in vals
    assert vals == sorted(vals)
    deltas = [round(vals[i + 1] - vals[i], 6) for i in range(len(vals) - 1)]
    assert all(abs(d - deltas[0]) < 1e-6 for d in deltas), f"deltas not uniform: {deltas}"
    assert cj.tier_cell_to_chart_numeric("Very High") == 92.0
    assert cj.tier_cell_to_chart_numeric("Very Low") == 8.0
    assert cj.tier_cell_to_chart_numeric("Unknown") is not None
    assert cj.tier_cell_to_chart_numeric("Unknown") < cj.tier_cell_to_chart_numeric("Very Low")


def test_normalize_seven_point_tiers() -> None:
    assert cj.rating_only_for_summary("medium low (x)") == "Medium-Low"
    assert cj.rating_only_for_summary("Very Low") == "Very Low"
    assert cj.rating_only_for_summary("Medium–High (legacy en dash)") == "Medium-High"


def test_seven_step_ordinals_constant() -> None:
    assert cj.SEVEN_STEP_ORDINALS == (
        "Very Low",
        "Low",
        "Medium-Low",
        "Medium",
        "Medium-High",
        "High",
        "Very High",
    )


def test_build_collated_rows_one_report(tmp_path: Path) -> None:
    jd = "Role X"
    (tmp_path / f"{jd}.eval.md").write_text(
        """# Header metadata
- `job`: Test Job

### PART 5 — Combined verdict

- **Fit on paper:** **High**
- **Actual capability (inferred):** **Medium**
- **Narrative coherence (for this JD):** **Medium**
- **Signal strength: Recruiter:** **Low**
- **Signal strength: HM:** **Medium**

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
- **Narrative coherence (for this JD):** **Medium**
- **Signal strength: Recruiter:** **Medium**
- **Signal strength: HM:** **Medium**
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
    assert "Dot matrix" in text
    assert "Radar" in text


def test_combined_chart_columns_order() -> None:
    assert len(cj.COMBINED_CHART_COLUMNS) == len(cj.VERDICT_TABLE_COLUMNS) + len(cj.RUBRIC_TABLE_COLUMNS)
    assert cj.COMBINED_CHART_COLUMNS[: len(cj.VERDICT_TABLE_COLUMNS)] == cj.VERDICT_TABLE_COLUMNS


def test_chart_score_columns_omits_ats_and_risk_factors() -> None:
    assert "ATS / recruiter hygiene" not in cj.CHART_SCORE_COLUMNS
    assert "Risk Factors" not in cj.CHART_SCORE_COLUMNS
    assert len(cj.CHART_SCORE_COLUMNS) == len(cj.COMBINED_CHART_COLUMNS) - 2


def test_tier_cell_pass_fail_chart_numeric() -> None:
    assert cj.tier_cell_to_chart_numeric("Pass") == 92.0
    assert cj.tier_cell_to_chart_numeric("Fail") == 8.0


def test_extract_model_used_header() -> None:
    text = """# Header metadata
- `template_version`: v1.14.0
- `model_used`: `GPT-5.4 Mini`
- `job`: Role
"""
    assert cj.extract_model_used(text) == "GPT-5.4 Mini"


def test_extract_model_used_missing() -> None:
    assert cj.extract_model_used("# no metadata\nbody") == ""


def test_is_mini_family_model_heuristic() -> None:
    assert cj._is_mini_family_model("GPT-5.4 Mini") is True
    assert cj._is_mini_family_model("Cursor / GPT-5.4 Mini") is True
    assert cj._is_mini_family_model("gpt-5.4-medium") is False
    assert cj._is_mini_family_model("Cursor GPT-5.4") is False
    assert cj._is_mini_family_model("") is False


def test_build_collated_rows_captures_model_used(tmp_path: Path) -> None:
    jd = "Role With Model"
    (tmp_path / f"{jd}.eval.md").write_text(
        """# Header metadata
- `model_used`: `GPT-5.4 Mini`

### PART 5 — Combined verdict

- **Fit on paper:** **High**
- **Actual capability (inferred):** **Medium**
- **Narrative coherence (for this JD):** **Medium**
- **Signal strength: Recruiter:** **Medium**
- **Signal strength: HM:** **Medium**

### PART 6 — x
""",
        encoding="utf-8",
    )
    rows = cj.build_collated_rows(tmp_path, tmp_path)
    assert rows[0].model_used == "GPT-5.4 Mini"


def test_extract_rubric_subsection_and_lines() -> None:
    part6 = """
#### Rubric

- **Problem Match (25%):** High
- **Relevant Proof (20%):** Medium
- **Recency (15%):** Low
- **Role Readability (15%):** Medium
- **Differentiation (10%):** High
- **Risk Factors (10%):** Medium
- **Narrative Coherence (5%):** High
- **ATS / recruiter hygiene:** Pass

#### Weighted synthesis

- **Q:** A
"""
    block = cj.extract_rubric_subsection(part6)
    assert "Weighted synthesis" not in block
    rubric = cj.extract_rubric_lines(block)
    assert rubric["Problem Match"].startswith("- **Problem Match")
    assert cj.rubric_line_to_table_cell(rubric["ATS / recruiter hygiene"], "ATS / recruiter hygiene") == "Pass"
    assert cj.rubric_line_to_table_cell(rubric["Narrative Coherence (rubric)"], "Narrative Coherence (rubric)") == "High"


def test_build_collated_rows_parses_part6_rubric(tmp_path: Path) -> None:
    jd = "Rubric Co"
    (tmp_path / f"{jd}.eval.md").write_text(
        """### PART 5 — Combined verdict
- **Fit on paper:** **High**
- **Actual capability (inferred):** **Medium**
- **Narrative coherence (for this JD):** **Medium**
- **Signal strength: Recruiter:** **Medium**
- **Signal strength: HM:** **Medium**

### PART 6 — Rubric scoring

#### Rubric

- **Problem Match (25%):** Low
- **ATS / recruiter hygiene:** Fail

#### Weighted synthesis
x
""",
        encoding="utf-8",
    )
    rows = cj.build_collated_rows(tmp_path, tmp_path)
    assert len(rows) == 1
    assert rows[0].rubric.get("Problem Match", "").startswith("- **Problem Match")
    assert cj.rubric_line_to_table_cell(rows[0].rubric["ATS / recruiter hygiene"], "ATS / recruiter hygiene") == "Fail"
