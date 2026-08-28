#!/usr/bin/env python3
"""
Diffs tokens.css against .design-sync-snapshot.css and prints the added /
changed / removed tokens as JSON, ready for Claude to push into Pencil
(pen.dev) via its GetVariables / SetVariables execute-tool functions.

This script does NOT talk to Pencil directly (its tools are only reachable
from Claude's own tool-calling session) - it just computes the diff.

Usage: python3 sync-tokens.py
"""
import json
import re
import sys
from pathlib import Path

TOKEN_RE = re.compile(r"^\s*(--[\w-]+)\s*:\s*(.+?)\s*;\s*$")

TYPE_PREFIXES = [
    ("--color-", "color"),
    ("--font-weight-", "string"),
    ("--font-", "string"),
    ("--text-", "number"),
    ("--tracking-", "number"),
    ("--leading-", "number"),
    ("--radius-", "number"),
    ("--space-", "number"),
]


def token_type(name):
    for prefix, kind in TYPE_PREFIXES:
        if name.startswith(prefix):
            return kind
    return "unknown"


def parse_tokens(path):
    tokens = {}
    if not path.exists():
        return tokens
    for line in path.read_text().splitlines():
        match = TOKEN_RE.match(line)
        if match:
            tokens[match.group(1)] = match.group(2)
    return tokens


def main():
    root = Path(__file__).parent
    current = parse_tokens(root / "tokens.css")
    snapshot = parse_tokens(root / ".design-sync-snapshot.css")

    added = [
        {"type": token_type(name), "name": name, "value": value}
        for name, value in current.items()
        if name not in snapshot
    ]
    changed = [
        {"name": name, "value": value}
        for name, value in current.items()
        if name in snapshot and snapshot[name] != value
    ]
    removed = [{"name": name, "delete": True} for name in snapshot if name not in current]

    result = {"added": added, "changed": changed, "removed": removed}

    if not added and not changed and not removed:
        print("No changes since last Pencil sync.")
    else:
        print(json.dumps(result, indent=2))

    return 0


if __name__ == "__main__":
    sys.exit(main())
