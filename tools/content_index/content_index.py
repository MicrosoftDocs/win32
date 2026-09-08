#!/usr/bin/env python3
"""Build, search, and audit conceptual documentation indexes."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable

DEFAULT_CONFIG = ".github/content-index-config.json"
WORD_RE = re.compile(r"[a-z0-9][a-z0-9.+#-]*")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$")
LINK_RE = re.compile(r"!?\[([^\]]*)\]\([^)]+\)")
HTML_RE = re.compile(r"<[^>]+>")
CODE_RE = re.compile(r"`[^`]+`")
WHITESPACE_RE = re.compile(r"\s+")
STOP_WORDS = {
    "a", "about", "after", "all", "also", "an", "and", "any", "are", "as",
    "at", "be", "because", "before", "between", "by", "can", "configure",
    "create", "do", "does", "for", "from", "get", "how", "if", "in", "into",
    "is", "it", "its", "learn", "more", "not", "of", "on", "or", "other",
    "page", "set", "that", "the", "their", "this", "to", "use", "using",
    "was", "what", "when", "where", "which", "will", "with", "you", "your",
}


def load_config(repo_root: Path, config_path: str) -> dict:
    path = repo_root / config_path
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        return {}, text
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return {}, text

    metadata: dict[str, str] = {}
    for line in lines[1:end]:
        if line.startswith((" ", "\t", "-")) or ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip().lower()] = value.strip().strip("\"'")
    return metadata, "\n".join(lines[end + 1 :])


def strip_markdown(text: str) -> str:
    output: list[str] = []
    in_fence = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence or stripped.startswith(("[!", ":::")):
            continue
        line = LINK_RE.sub(r"\1", line)
        line = CODE_RE.sub(" ", line)
        line = HTML_RE.sub(" ", line)
        line = re.sub(r"^[#>*+\-\d.\s]+", "", line)
        output.append(line)
    return WHITESPACE_RE.sub(" ", " ".join(output)).strip()


def extract_headings(text: str) -> list[str]:
    headings: list[str] = []
    in_fence = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if not in_fence and (match := HEADING_RE.match(stripped)):
            headings.append(clean_heading(match.group(1)))
    return headings


def clean_heading(value: str) -> str:
    value = LINK_RE.sub(r"\1", value)
    value = CODE_RE.sub(" ", value)
    return WHITESPACE_RE.sub(" ", HTML_RE.sub(" ", value)).strip()


def normalize_token(token: str) -> str:
    if len(token) > 4 and token.endswith("ies"):
        return f"{token[:-3]}y"
    if (
        len(token) > 3
        and token.endswith("s")
        and not token.endswith(("is", "ss", "us"))
    ):
        return token[:-1]
    return token


def tokenize(value: str) -> list[str]:
    return [
        normalize_token(token)
        for token in WORD_RE.findall(value.lower())
        if len(token) > 1 and token not in STOP_WORDS and not token.isdigit()
    ]


def important_terms(text: str, max_terms: int) -> list[str]:
    counts = Counter(tokenize(text))
    return [
        term
        for term, _ in sorted(
            counts.items(), key=lambda item: (-item[1], item[0])
        )[:max_terms]
    ]


def published_url(url_prefix: str, relative_path: Path) -> str:
    path = relative_path.as_posix()
    if path.lower().endswith(".md"):
        path = path[:-3]
    if path.lower().endswith("/index"):
        path = path[:-6]
    elif path.lower() == "index":
        path = ""
    return f"{url_prefix.rstrip('/')}/{path.lstrip('/')}".rstrip("/")


def excluded(path: Path, config: dict) -> bool:
    excluded_parts = {part.lower() for part in config["exclude_path_parts"]}
    if any(part.lower() in excluded_parts for part in path.parts):
        return True
    return path.name.lower() in {
        name.lower() for name in config["exclude_filenames"]
    }


def generated_api_reference(metadata: dict[str, str], body: str) -> bool:
    if metadata.get("ms.topic", "").strip().lower() != "reference":
        return False
    has_definition = re.search(r"^## Definition\s*$", body, re.MULTILINE)
    has_namespace = re.search(r"^Namespace:\s", body, re.MULTILINE)
    has_member_section = re.search(
        r"^## (Parameters|Properties|Methods|Fields|Events|Constructors|Returns)\s*$",
        body,
        re.MULTILINE,
    )
    return bool(has_definition and has_namespace and has_member_section)


def record_for_file(
    repo_root: Path, docset: dict, path: Path, config: dict
) -> dict | None:
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    metadata, body = parse_front_matter(text)
    topic = metadata.get("ms.topic", "").strip().lower()
    if topic in {item.lower() for item in config["exclude_topics"]}:
        return None
    if any(
        key.lower() in metadata for key in config.get("exclude_metadata_keys", [])
    ):
        return None
    if config.get("exclude_generated_api_reference") and generated_api_reference(
        metadata, body
    ):
        return None

    headings = extract_headings(body)
    title = metadata.get("title") or (headings[0] if headings else path.stem)
    description = metadata.get("description", "")
    body_text = strip_markdown(body)
    normalized_tokens = tokenize(body_text)
    normalized = " ".join(normalized_tokens)
    relative_to_docset = path.relative_to(repo_root / docset["root"])
    relative_to_repo = path.relative_to(repo_root)
    term_source = " ".join([title, description, *headings, body_text])

    return {
        "schema_version": config["schema_version"],
        "repository": config["repository"],
        "docset": docset["name"],
        "status": docset["status"],
        "path": relative_to_repo.as_posix(),
        "url": published_url(docset["url_prefix"], relative_to_docset),
        "title": title,
        "description": description,
        "ms_topic": topic,
        "ms_service": metadata.get("ms.service", ""),
        "ms_subservice": metadata.get("ms.subservice", ""),
        "headings": headings[1:] if headings and headings[0] == title else headings,
        "terms": important_terms(term_source, config["max_terms"]),
        "word_count": len(normalized_tokens),
        "fingerprint": hashlib.sha256(normalized.encode("utf-8")).hexdigest(),
    }


def build_records(repo_root: Path, config: dict) -> list[dict]:
    records: list[dict] = []
    for docset in config["docsets"]:
        root = repo_root / docset["root"]
        if not root.exists():
            continue
        for path in sorted(root.rglob("*.md")):
            relative = path.relative_to(root)
            if excluded(relative, config):
                continue
            record = record_for_file(repo_root, docset, path, config)
            if record:
                records.append(record)
    return sorted(records, key=lambda item: (item["repository"], item["path"]))


def serialize(records: Iterable[dict]) -> str:
    return "".join(
        json.dumps(record, ensure_ascii=True, sort_keys=True, separators=(",", ":"))
        + "\n"
        for record in records
    )


def build_index(repo_root: Path, config: dict, check: bool) -> int:
    index_path = repo_root / config["index_path"]
    content = serialize(build_records(repo_root, config))
    if check:
        if index_path.exists():
            with index_path.open("r", encoding="utf-8", newline="") as stream:
                existing = stream.read()
        else:
            existing = ""
        if existing != content:
            print(
                f"{config['index_path']} is stale. Run "
                f"`python tools/content_index/content_index.py build`.",
                file=sys.stderr,
            )
            return 1
        print(f"{config['index_path']} is current.")
        return 0

    index_path.parent.mkdir(parents=True, exist_ok=True)
    with index_path.open("w", encoding="utf-8", newline="\n") as stream:
        stream.write(content)
    print(f"Wrote {len(content.splitlines())} records to {config['index_path']}.")
    return 0


def load_indexes(paths: Iterable[Path], schema_version: int) -> list[dict]:
    records: list[dict] = []
    required = {
        "schema_version",
        "repository",
        "docset",
        "status",
        "path",
        "url",
        "title",
        "description",
        "headings",
        "terms",
        "word_count",
        "fingerprint",
    }
    for path in paths:
        with path.open(encoding="utf-8") as stream:
            for line_number, line in enumerate(stream, 1):
                if line.strip():
                    try:
                        record = json.loads(line)
                    except json.JSONDecodeError as error:
                        raise ValueError(f"{path}:{line_number}: {error}") from error
                    missing = required - set(record)
                    if missing:
                        raise ValueError(
                            f"{path}:{line_number}: missing required fields: "
                            f"{', '.join(sorted(missing))}"
                        )
                    if record["schema_version"] != schema_version:
                        raise ValueError(
                            f"{path}:{line_number}: schema version "
                            f"{record['schema_version']} does not match {schema_version}"
                        )
                    records.append(record)
    return records


def field_tokens(record: dict, field: str) -> set[str]:
    value = record.get(field, "")
    if isinstance(value, list):
        value = " ".join(value)
    if field == "path":
        value = re.sub(r"[/_.-]+", " ", value)
    return set(tokenize(value))


def search(records: list[dict], query: str, limit: int) -> list[tuple[float, dict]]:
    query_tokens = set(tokenize(query))
    query_phrase = query.lower().strip()
    results: list[tuple[float, dict]] = []
    for record in records:
        title = field_tokens(record, "title")
        description = field_tokens(record, "description")
        headings = field_tokens(record, "headings")
        path = field_tokens(record, "path")
        terms = set(record.get("terms", []))
        score = (
            8 * len(query_tokens & title)
            + 4 * len(query_tokens & description)
            + 3 * len(query_tokens & headings)
            + 2 * len(query_tokens & path)
            + len(query_tokens & terms)
        )
        if query_phrase and query_phrase in record.get("title", "").lower():
            score += 12
        if score:
            if record.get("status") == "current":
                score += 0.25
            results.append((score, record))
    return sorted(
        results,
        key=lambda item: (-item[0], item[1].get("title", ""), item[1]["path"]),
    )[:limit]


def jaccard(left: set[str], right: set[str]) -> float:
    union = left | right
    return len(left & right) / len(union) if union else 0.0


def duplicate_score(left: dict, right: dict) -> tuple[float, str]:
    if left["fingerprint"] == right["fingerprint"]:
        return 1.0, "identical normalized content"
    title_score = jaccard(field_tokens(left, "title"), field_tokens(right, "title"))
    summary_score = jaccard(
        field_tokens(left, "title")
        | field_tokens(left, "description")
        | field_tokens(left, "headings"),
        field_tokens(right, "title")
        | field_tokens(right, "description")
        | field_tokens(right, "headings"),
    )
    term_score = jaccard(set(left.get("terms", [])), set(right.get("terms", [])))
    score = 0.5 * title_score + 0.3 * summary_score + 0.2 * term_score
    return score, "similar title, summary, headings, and terminology"


def audit(
    records: list[dict], threshold: float, limit: int, min_words: int
) -> list[dict]:
    term_to_records: dict[str, list[int]] = defaultdict(list)
    fingerprint_to_records: dict[str, list[int]] = defaultdict(list)
    for index, record in enumerate(records):
        fingerprint_to_records[record["fingerprint"]].append(index)
        candidate_terms = field_tokens(record, "title") | field_tokens(
            record, "description"
        )
        for term in candidate_terms:
            term_to_records[term].append(index)

    candidate_pairs: set[tuple[int, int]] = set()
    for indexes in fingerprint_to_records.values():
        for position, left in enumerate(indexes):
            for right in indexes[position + 1 :]:
                candidate_pairs.add((left, right))
    for indexes in term_to_records.values():
        if len(indexes) > 100:
            continue
        for position, left in enumerate(indexes):
            for right in indexes[position + 1 :]:
                candidate_pairs.add((min(left, right), max(left, right)))

    findings: list[dict] = []
    for left_index, right_index in candidate_pairs:
        left, right = records[left_index], records[right_index]
        if left["word_count"] < min_words or right["word_count"] < min_words:
            continue
        if left["path"] == right["path"] and left["repository"] == right["repository"]:
            continue
        score, reason = duplicate_score(left, right)
        if score >= threshold:
            findings.append(
                {
                    "score": round(score, 3),
                    "reason": reason,
                    "left": left,
                    "right": right,
                }
            )
    return sorted(findings, key=lambda item: -item["score"])[:limit]


def print_search(results: list[tuple[float, dict]]) -> None:
    if not results:
        print("No related content found.")
        return
    for score, record in results:
        print(
            f"{score:5.2f}  [{record['status']}] {record['title']}\n"
            f"       {record['repository']}:{record['path']}\n"
            f"       {record['url']}"
        )


def print_audit(findings: list[dict], output_format: str) -> None:
    if output_format == "json":
        print(json.dumps(findings, indent=2, sort_keys=True))
        return
    print("| Score | First topic | Second topic | Reason |")
    print("|---:|---|---|---|")
    for finding in findings:
        left, right = finding["left"], finding["right"]
        print(
            f"| {finding['score']:.3f} "
            f"| [{left['title']}]({left['url']})<br>`{left['repository']}:{left['path']}` "
            f"| [{right['title']}]({right['url']})<br>`{right['repository']}:{right['path']}` "
            f"| {finding['reason']} |"
        )


def index_paths(repo_root: Path, config: dict, supplied: list[str]) -> list[Path]:
    values = supplied or [config["index_path"]]
    return [Path(value) if Path(value).is_absolute() else repo_root / value for value in values]


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--repo-root", default=".", help="Repository root.")
    result.add_argument("--config", default=DEFAULT_CONFIG, help="Index configuration.")
    subcommands = result.add_subparsers(dest="command", required=True)
    subcommands.add_parser("build", help="Generate the configured index.")
    subcommands.add_parser("check", help="Fail if the configured index is stale.")

    search_parser = subcommands.add_parser("search", help="Search one or more indexes.")
    search_parser.add_argument("query")
    search_parser.add_argument("--index", action="append", default=[])
    search_parser.add_argument("--limit", type=int, default=10)

    audit_parser = subcommands.add_parser("audit", help="Find likely duplicate topics.")
    audit_parser.add_argument("--index", action="append", default=[])
    audit_parser.add_argument("--threshold", type=float, default=0.72)
    audit_parser.add_argument("--limit", type=int, default=100)
    audit_parser.add_argument(
        "--min-words",
        type=int,
        default=50,
        help="Exclude shorter navigation and stub pages from audit candidates.",
    )
    audit_parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    return result


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    repo_root = Path(args.repo_root).resolve()
    try:
        config = load_config(repo_root, args.config)
    except (OSError, json.JSONDecodeError) as error:
        print(error, file=sys.stderr)
        return 1
    if args.command in {"build", "check"}:
        return build_index(repo_root, config, args.command == "check")

    try:
        records = load_indexes(
            index_paths(repo_root, config, args.index), config["schema_version"]
        )
    except (OSError, ValueError) as error:
        print(error, file=sys.stderr)
        return 1
    if args.command == "search":
        print_search(search(records, args.query, args.limit))
    else:
        print_audit(
            audit(records, args.threshold, args.limit, args.min_words), args.format
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
