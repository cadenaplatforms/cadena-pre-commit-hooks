"""Ensures that all dependencies in requirements files have an exact version number."""

from __future__ import annotations

import argparse
from typing import Sequence

import requirements


PASS = 0
FAIL = 1


def pin_requirements(file_path) -> int:
    """Check if all dependencies in the given requirements file have an exact version number."""

    def verify_spec(spec):
        return spec[0] == "==" and "*" not in spec[1] or spec[0] == "==="

    rv = PASS
    with open(file_path, encoding="utf-8") as file:
        for req in requirements.parse(file):
            if not any(verify_spec(spec) for spec in req.specs):
                print(
                    f"{file_path} dependency '{req.name}' does not have an exact version number: {req.line}.",
                )
                rv = FAIL

    return rv


def main(argv: Sequence[str] | None = None) -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to check.")
    args = parser.parse_args(argv)

    retv = PASS

    for filename in args.filenames:
        if pin_requirements(filename) == FAIL:
            retv = FAIL

    return retv


if __name__ == "__main__":
    raise SystemExit(main())
