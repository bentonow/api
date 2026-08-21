#!/usr/bin/env python3
"""Compare bento-api.yaml operations to scripts/expected-endpoints.txt."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "bento-api.yaml"
EXPECTED = ROOT / "scripts" / "expected-endpoints.txt"
HTTP_METHODS = {"get", "post", "put", "patch", "delete", "head", "options"}


def expected_operations():
    operations = []
    for raw in EXPECTED.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        method, path = line.split(" ", 1)
        operations.append(f"{method.upper()} {path}")
    return operations


def spec_operations():
    operations = []
    current_path = None
    for raw in SPEC.read_text().splitlines():
        if raw.startswith("    /") and raw.rstrip().endswith(":"):
            current_path = raw.strip()[:-1]
            continue
        stripped = raw.strip()
        if current_path and stripped.endswith(":") and stripped[:-1] in HTTP_METHODS:
            operations.append(f"{stripped[:-1].upper()} {current_path}")
    return operations


def main():
    expected = expected_operations()
    actual = spec_operations()
    missing = [item for item in expected if item not in actual]
    extra = [item for item in actual if item not in expected]

    print(f"expected {len(expected)} operations, spec has {len(actual)}")
    if missing:
        print("missing from spec:")
        for item in missing:
            print(f"  {item}")
    if extra:
        print("in spec but not in expected inventory:")
        for item in extra:
            print(f"  {item}")
    if missing or extra:
        return 1
    print("coverage matches scripts/expected-endpoints.txt")
    return 0


if __name__ == "__main__":
    sys.exit(main())
