#!/usr/bin/env python3
"""
scripts/update_readmes.py

Automated documentation and statistics generator for the problem-solving repository.
Audits solution files across LeetCode and CodeChef, synchronizes problem metadata,
and updates Markdown tables and counts across:
  - /README.md
  - /LeetCode/README.md
  - /CodeChef/README.md

Designed to be idempotent, standard-library-only, and CI-safe.
"""

import os
import re
import sys
import json
import glob
from pathlib import Path
from collections import defaultdict


def get_repo_root():
    return Path(__file__).resolve().parent.parent


def slugify(title):
    """Generate a clean LeetCode problem URL slug from a title."""
    s = re.sub(r"^Q\d+\.\s*", "", title)
    s = s.lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s).strip("-")
    s = re.sub(r"-+", "-", s)
    return s


def load_metadata(metadata_path):
    if metadata_path.exists():
        with open(metadata_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"leetcode": {}, "leetcode_contests": {}, "codechef": {}}


def save_metadata(metadata_path, data):
    with open(metadata_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def scan_leetcode(repo_root, metadata):
    lc_dir = repo_root / "LeetCode"
    easy_dir = lc_dir / "EASY"
    medium_dir = lc_dir / "MEDIUM"
    hard_dir = lc_dir / "HARD"
    contest_dir = lc_dir / "Weekly Contest"

    easy_files = sorted(glob.glob(str(easy_dir / "*.py")))
    medium_files = sorted(glob.glob(str(medium_dir / "*.py")))
    hard_files = sorted(glob.glob(str(hard_dir / "*.py")))
    contest_files = sorted(glob.glob(str(contest_dir / "**" / "*.py"), recursive=True))

    lc_meta = metadata.get("leetcode", {})
    contest_meta = metadata.get("leetcode_contests", {})

    # Data structures to aggregate
    # easy_problems: id -> dict
    # medium_problems: id -> dict
    # hard_problems: id -> dict
    # contest_problems: list of dicts

    easy_problems = {}
    medium_problems = {}
    hard_problems = {}
    contest_problems = []

    # Map problem IDs to all solution file paths relative to LeetCode/
    problem_solutions = defaultdict(list)
    problem_info = {}

    def parse_problem_file(filepath, default_folder):
        p = Path(filepath)
        fname = p.name
        rel_path = p.relative_to(lc_dir).as_posix()

        # Regular problems: "0001 Two Sum.py", "287. Find the Duplicate Number.py"
        m = re.match(r"^(\d+)[.\s]+(.+?)\.py$", fname)
        if m:
            pid = int(m.group(1))
            raw_title = m.group(2).strip().rstrip(".")
            return pid, raw_title, rel_path, default_folder
        return None, fname, rel_path, default_folder

    # Process EASY folder
    for f in easy_files:
        pid, raw_title, rel_path, folder = parse_problem_file(f, "EASY")
        if pid is not None:
            problem_solutions[pid].append((rel_path, folder))
            if pid not in problem_info:
                problem_info[pid] = {
                    "id": pid,
                    "raw_title": raw_title,
                    "default_folder": folder,
                }

    # Process MEDIUM folder
    for f in medium_files:
        pid, raw_title, rel_path, folder = parse_problem_file(f, "MEDIUM")
        if pid is not None:
            problem_solutions[pid].append((rel_path, folder))
            if pid not in problem_info:
                problem_info[pid] = {
                    "id": pid,
                    "raw_title": raw_title,
                    "default_folder": folder,
                }

    # Process HARD folder
    for f in hard_files:
        pid, raw_title, rel_path, folder = parse_problem_file(f, "HARD")
        if pid is not None:
            problem_solutions[pid].append((rel_path, folder))
            if pid not in problem_info:
                problem_info[pid] = {
                    "id": pid,
                    "raw_title": raw_title,
                    "default_folder": folder,
                }

    # Process contest files
    for f in contest_files:
        p = Path(f)
        rel_path = p.relative_to(lc_dir).as_posix()
        repo_rel_path = p.relative_to(repo_root).as_posix()

        # Check contest metadata
        c_info = contest_meta.get(repo_rel_path, {})
        fname = p.name
        m_q = re.match(r"^Q(\d+)\.\s*(.+?)\s*\.py$", fname)

        if c_info:
            cid = c_info.get("id", 0)
            ctitle = c_info.get("title", fname)
            cdiff = c_info.get("difficulty", "Contest")
            curl = c_info.get("url", "")
        elif m_q:
            q_num = int(m_q.group(1))
            cid = 3902 + q_num
            ctitle = f"Q{q_num}. {m_q.group(2).strip()}"
            cdiff = "Contest"
            curl = f"https://leetcode.com/problems/{slugify(ctitle)}/"
        else:
            cid = 9999
            ctitle = fname.replace(".py", "")
            cdiff = "Contest"
            curl = ""

        contest_problems.append({
            "id": cid,
            "title": ctitle,
            "difficulty": cdiff,
            "url": curl,
            "solution_path": rel_path,
        })

    contest_problems.sort(key=lambda x: x["id"])

    # Organize regular problems by official difficulty
    for pid, info in problem_info.items():
        stored = lc_meta.get(str(pid), {})
        title = stored.get("title") or info["raw_title"]
        url = stored.get("url")
        if not url:
            url = f"https://leetcode.com/problems/{slugify(title)}/"

        # Official difficulty check: problem 128 is officially Medium
        if pid == 128:
            difficulty = "Medium"
        else:
            difficulty = info["default_folder"].capitalize()

        sols = problem_solutions[pid]

        prob_entry = {
            "id": pid,
            "title": title,
            "difficulty": difficulty,
            "url": url,
            "solutions": sols,
        }

        if difficulty == "Easy":
            easy_problems[pid] = prob_entry
        elif difficulty == "Medium":
            medium_problems[pid] = prob_entry
        elif difficulty == "Hard":
            hard_problems[pid] = prob_entry

    # Counts
    unique_easy = len(easy_problems)
    unique_med = len(medium_problems)
    unique_hard = len(hard_problems)
    unique_contest = len(contest_problems)
    unique_total = unique_easy + unique_med + unique_hard + unique_contest

    file_count_easy = len(easy_files)
    file_count_med = len(medium_files)
    file_count_hard = len(hard_files)
    file_count_contest = len(contest_files)
    file_count_total = file_count_easy + file_count_med + file_count_hard + file_count_contest

    return {
        "easy_problems": [easy_problems[k] for k in sorted(easy_problems.keys())],
        "medium_problems": [medium_problems[k] for k in sorted(medium_problems.keys())],
        "hard_problems": [hard_problems[k] for k in sorted(hard_problems.keys())],
        "contest_problems": contest_problems,
        "counts": {
            "unique_easy": unique_easy,
            "unique_medium": unique_med,
            "unique_hard": unique_hard,
            "unique_contest": unique_contest,
            "unique_total": unique_total,
            "files_easy": file_count_easy,
            "files_medium": file_count_med,
            "files_hard": file_count_hard,
            "files_contest": file_count_contest,
            "files_total": file_count_total,
        },
    }


def scan_codechef(repo_root, metadata):
    cc_dir = repo_root / "CodeChef"
    cc_meta = metadata.get("codechef", {})

    # Discover difficulty ranges
    range_dirs = []
    if cc_dir.exists():
        for d in sorted(cc_dir.iterdir()):
            if d.is_dir() and re.match(r"^\d{4}-\d{4}$", d.name):
                range_dirs.append(d)

    range_counts = {}
    problems = []

    for r_dir in range_dirs:
        r_name = r_dir.name.replace("-", "–")
        py_files = sorted(glob.glob(str(r_dir / "*.py")))
        range_counts[r_name] = {
            "folder": r_dir.name,
            "count": len(py_files),
        }

        for f in py_files:
            p = Path(f)
            rel_path = p.relative_to(cc_dir).as_posix()
            repo_rel_path = p.relative_to(repo_root).as_posix()

            m_stored = cc_meta.get(repo_rel_path, {})
            fname = p.name

            # Parse filename e.g. "001 SEARCHINARR.py", "002 Find maximum in an Array.py"
            m_fn = re.match(r"^(\d+)\s+(.+?)\.py$", fname)
            if m_fn:
                local_id = int(m_fn.group(1))
                name_part = m_fn.group(2).strip()
            else:
                local_id = len(problems) + 1
                name_part = fname.replace(".py", "")

            prob_name = m_stored.get("problem_name", name_part)
            prob_code = m_stored.get("problem_code", "")
            prob_url = m_stored.get("url", "")
            diff_range = m_stored.get("difficulty_range", r_name)

            problems.append({
                "local_id": local_id,
                "problem_name": prob_name,
                "problem_code": prob_code,
                "difficulty_range": diff_range,
                "url": prob_url,
                "solution_path": rel_path,
            })

    problems.sort(key=lambda x: x["local_id"])
    total_problems = len(problems)

    return {
        "range_counts": range_counts,
        "problems": problems,
        "total_problems": total_problems,
    }


def format_solution_link(solutions, default_label="Solution"):
    """
    Format solution link(s) for Markdown table.
    Handles multiple solutions (e.g. for duplicate #128).
    """
    if not solutions:
        return "—"
    if len(solutions) == 1:
        rel_path, _ = solutions[0]
        return f"[{default_label}](<{rel_path}>)"

    # Multiple solutions
    links = []
    for rel_path, folder in solutions:
        if folder == "EASY":
            links.append(f"[Alt (EASY)](<{rel_path}>)")
        elif folder == "MEDIUM":
            links.append(f"[Solution](<{rel_path}>)")
        else:
            links.append(f"[Solution ({folder})](<{rel_path}>)")
    return " · ".join(links)


def generate_main_readme_sections(lc_data, cc_data):
    lc_c = lc_data["counts"]
    cc_total = cc_data["total_problems"]
    total_unique = lc_c["unique_total"] + cc_total
    total_files = lc_c["files_total"] + cc_total

    # Overall Stats Section
    stats_md = (
        f"| Metric | Total Count |\n"
        f"| :--- | :---: |\n"
        f"| 🎯 **Total Unique Problems Documented** | **{total_unique}** |\n"
        f"| 💻 **LeetCode Unique Problems** | **{lc_c['unique_total']}** |\n"
        f"| 👨‍🍳 **CodeChef Unique Problems** | **{cc_total}** |\n"
        f"| 📂 **Total Solution Files Tracked** | **{total_files}** |"
    )

    # Platform Overview Table
    overview_md = (
        f"| Platform | Problems | Organization | Explore |\n"
        f"| :--- | :--- | :--- | :--- |\n"
        f"| **LeetCode** | {lc_c['unique_total']} unique ({lc_c['files_total']} solutions) | Easy / Medium / Hard / Contests | [View Solutions](LeetCode/README.md) |\n"
        f"| **CodeChef** | {cc_total} unique ({cc_total} solutions) | Difficulty Rating / Contests | [View Solutions](CodeChef/README.md) |\n"
        f"| **Total** | **{total_unique} unique** ({total_files} solutions) | — | — |"
    )

    return stats_md, overview_md


def generate_leetcode_readme_sections(lc_data):
    c = lc_data["counts"]

    # Progress Summary Section
    progress_md = (
        f"| Category | Unique Problems | Solution Files | Status |\n"
        f"| :--- | :---: | :---: | :---: |\n"
        f"| 🟢 Easy | {c['unique_easy']} | {c['files_easy']} | Active |\n"
        f"| 🟡 Medium | {c['unique_medium']} | {c['files_medium']} | Active |\n"
        f"| 🔴 Hard | {c['unique_hard']} | {c['files_hard']} | In Progress ([Details](HARD/000why.md)) |\n"
        f"| 🏁 Weekly Contest | {c['unique_contest']} | {c['files_contest']} | Active |\n"
        f"| **Total** | **{c['unique_total']}** | **{c['files_total']}** | — |\n\n"
        f"> **Note on Solved Totals:** Unique problems reflect distinct LeetCode challenges solved. "
        f"Problem #128 (*Longest Consecutive Sequence*) is officially classified as Medium; "
        f"an alternative solution is preserved in `EASY/`, resulting in 153 solution files across 152 distinct problems."
    )

    # Tables Section
    tables_parts = []

    # 1. Easy Table
    tables_parts.append(f"### 🟢 Easy Problems ({c['unique_easy']})\n")
    tables_parts.append("<details open>\n<summary><b>Click to expand / collapse Easy Problems table</b></summary>\n<br>\n")
    tables_parts.append("| # | Problem | Difficulty | Problem Link | Solution |\n| :---: | :--- | :---: | :---: | :--- |")
    for p in lc_data["easy_problems"]:
        link_str = f"[Link]({p['url']})" if p["url"] else "—"
        sol_str = format_solution_link(p["solutions"])
        tables_parts.append(f"| {p['id']} | {p['title']} | 🟢 Easy | {link_str} | {sol_str} |")
    tables_parts.append("\n</details>\n")

    # 2. Medium Table
    tables_parts.append(f"### 🟡 Medium Problems ({c['unique_medium']})\n")
    tables_parts.append("<details open>\n<summary><b>Click to expand / collapse Medium Problems table</b></summary>\n<br>\n")
    tables_parts.append("| # | Problem | Difficulty | Problem Link | Solution |\n| :---: | :--- | :---: | :---: | :--- |")
    for p in lc_data["medium_problems"]:
        link_str = f"[Link]({p['url']})" if p["url"] else "—"
        sol_str = format_solution_link(p["solutions"])
        tables_parts.append(f"| {p['id']} | {p['title']} | 🟡 Medium | {link_str} | {sol_str} |")
    tables_parts.append("\n</details>\n")

    # 3. Hard Section
    tables_parts.append("### 🔴 Hard Problems (0)\n")
    tables_parts.append("<details>\n<summary><b>Click to expand / collapse Hard Problems roadmap</b></summary>\n<br>\n")
    tables_parts.append(
        "*No Python solutions published yet. Advanced algorithmic challenges are currently under study. "
        "See [HARD/000why.md](HARD/000why.md) for curriculum notes and key concepts.*\n"
    )
    tables_parts.append("</details>\n")

    # 4. Contest Table
    tables_parts.append(f"### 🏁 Weekly Contest Problems ({c['unique_contest']})\n")
    tables_parts.append("<details open>\n<summary><b>Click to expand / collapse Weekly Contest table</b></summary>\n<br>\n")
    tables_parts.append("| # | Problem | Difficulty | Problem Link | Solution |\n| :---: | :--- | :---: | :---: | :--- |")
    for p in lc_data["contest_problems"]:
        link_str = f"[Link]({p['url']})" if p["url"] else "—"
        sol_str = f"[Solution](<{p['solution_path']}>)"
        diff_str = f"🏁 Contest ({p['difficulty']})" if p["difficulty"] != "Contest" else "🏁 Contest"
        tables_parts.append(f"| {p['id']} | {p['title']} | {diff_str} | {link_str} | {sol_str} |")
    tables_parts.append("\n</details>")

    return progress_md, "\n".join(tables_parts)


def generate_codechef_readme_sections(cc_data):
    total = cc_data["total_problems"]
    range_counts = cc_data["range_counts"]

    populated_ranges = {k: v for k, v in range_counts.items() if v["count"] > 0}

    # Progress Summary
    progress_lines = [
        "| Metric | Count |",
        "| :--- | :---: |",
        f"| 🎯 **Total CodeChef Problems Documented** | **{total}** |",
    ]
    for r_label, r_info in populated_ranges.items():
        progress_lines.append(f"| 📊 **{r_label} Range Solutions** | **{r_info['count']}** |")
    progress_lines.append("| 🏁 **Contest Solutions** | **0** (Planned) |")
    progress_md = "\n".join(progress_lines)

    # Difficulty Overview
    overview_lines = [
        "| Difficulty Range | Problems | Status | Solutions |",
        "| :--- | :---: | :---: | :--- |",
    ]
    standard_ranges = [
        ("0000–0999", "0000-0999"),
        ("1000–1399", "1000-1399"),
        ("1400–1599", "1400-1599"),
        ("1600+ (Higher Ranges)", "1600+"),
    ]

    for label, folder in standard_ranges:
        cnt = 0
        if label in range_counts:
            cnt = range_counts[label]["count"]
        elif folder in range_counts:
            cnt = range_counts[folder]["count"]

        if cnt > 0:
            overview_lines.append(f"| **{label}** | {cnt} | Populated | [Browse]({folder}/) |")
        else:
            overview_lines.append(f"| **{label}** | 0 | Planned | — |")

    overview_md = "\n".join(overview_lines)

    # Problem Table
    table_lines = [
        "| # | Problem Name | Problem Code | Difficulty Range | Problem Link | Solution |",
        "| :---: | :--- | :---: | :---: | :---: | :--- |",
    ]
    for p in cc_data["problems"]:
        code_str = f"`{p['problem_code']}`" if p["problem_code"] else "—"
        link_str = f"[{p['problem_code']}]({p['url']})" if (p["url"] and p["problem_code"]) else (f"[Link]({p['url']})" if p["url"] else "—")
        sol_str = f"[Solution](<{p['solution_path']}>)"
        table_lines.append(
            f"| {p['local_id']} | {p['problem_name']} | {code_str} | {p['difficulty_range']} | {link_str} | {sol_str} |"
        )
    table_md = "\n".join(table_lines)

    return progress_md, overview_md, table_md


def replace_marker_content(file_path, marker_name, new_content):
    if not file_path.exists():
        return False

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    start_tag = f"<!-- START_{marker_name} -->"
    end_tag = f"<!-- END_{marker_name} -->"

    pattern = re.compile(
        rf"({re.escape(start_tag)})(?:.*?)({re.escape(end_tag)})",
        re.DOTALL
    )

    if not pattern.search(content):
        # Marker not found
        return False

    updated_content = pattern.sub(rf"\g<1>\n{new_content}\n\g<2>", content)

    if updated_content != content:
        with open(file_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(updated_content)
        return True
    return False


def main():
    check_mode = "--check" in sys.argv
    repo_root = get_repo_root()
    metadata_path = repo_root / "scripts" / "problem_metadata.json"

    metadata = load_metadata(metadata_path)

    lc_data = scan_leetcode(repo_root, metadata)
    cc_data = scan_codechef(repo_root, metadata)

    # Generate sections
    main_stats, main_overview = generate_main_readme_sections(lc_data, cc_data)
    lc_progress, lc_tables = generate_leetcode_readme_sections(lc_data)
    cc_progress, cc_overview, cc_table = generate_codechef_readme_sections(cc_data)

    main_readme = repo_root / "README.md"
    lc_readme = repo_root / "LeetCode" / "README.md"
    cc_readme = repo_root / "CodeChef" / "README.md"

    changed = False

    # Main README
    if replace_marker_content(main_readme, "OVERALL_STATS", main_stats):
        changed = True
    if replace_marker_content(main_readme, "PLATFORM_OVERVIEW", main_overview):
        changed = True

    # LeetCode README
    if replace_marker_content(lc_readme, "LEETCODE_PROGRESS", lc_progress):
        changed = True
    if replace_marker_content(lc_readme, "LEETCODE_TABLES", lc_tables):
        changed = True

    # CodeChef README
    if replace_marker_content(cc_readme, "CODECHEF_PROGRESS", cc_progress):
        changed = True
    if replace_marker_content(cc_readme, "CODECHEF_OVERVIEW", cc_overview):
        changed = True
    if replace_marker_content(cc_readme, "CODECHEF_TABLE", cc_table):
        changed = True

    lc_counts = lc_data["counts"]
    print("========================================")
    print("Documentation Audit and Sync Summary:")
    print(f"LeetCode Unique Problems: {lc_counts['unique_total']} (Files: {lc_counts['files_total']})")
    print(f"  - Easy:    {lc_counts['unique_easy']} unique ({lc_counts['files_easy']} files)")
    print(f"  - Medium:  {lc_counts['unique_medium']} unique ({lc_counts['files_medium']} files)")
    print(f"  - Hard:    {lc_counts['unique_hard']} unique ({lc_counts['files_hard']} files)")
    print(f"  - Contest: {lc_counts['unique_contest']} unique ({lc_counts['files_contest']} files)")
    print(f"CodeChef Unique Problems: {cc_data['total_problems']} (Files: {cc_data['total_problems']})")
    print(f"Total Unique Problems:    {lc_counts['unique_total'] + cc_data['total_problems']}")
    print(f"Total Solution Files:     {lc_counts['files_total'] + cc_data['total_problems']}")
    print("========================================")

    if check_mode:
        if changed:
            print("[CHECK] Changes were required. README files are not in sync.")
            sys.exit(1)
        else:
            print("[CHECK] All README files are up to date.")
            sys.exit(0)
    else:
        if changed:
            print("[SUCCESS] README files updated successfully.")
        else:
            print("[IDEMPOTENT] README files were already completely up to date.")


if __name__ == "__main__":
    main()
