#!/usr/bin/env python3
"""LingoLink check_preserved.py (v1.0.3). Python 3 standard library only.
Checks that URLs, numbers and code spans in a source text appear unchanged in a translation.
Usage: python3 check_preserved.py SOURCE_FILE TRANSLATION_FILE   (exit 0 = all preserved, 1 = something missing)
Limits: it checks exact text only; it cannot judge meaning, and numbers written as words or with
localized separators (1.000 vs 1,000) are reported as missing so a human can look."""
import re, sys

VERSION = "1.0.3"  # keep equal to .cursor-plugin/plugin.json

URL = re.compile(r"https?://[^\s<>\"')\]]+")
CODE = re.compile(r"```.*?```|`[^`\n]+`", re.S)
NUM = re.compile(r"(?<![A-Za-z0-9_.])\d+(?:[.,:]\d+)*")

def items(text):
    codes = CODE.findall(text)
    rest = CODE.sub(" ", text)
    urls = [u.rstrip(".,;:") for u in URL.findall(rest)]
    rest = URL.sub(" ", rest)
    return {"url": urls, "code": codes, "number": NUM.findall(rest)}

def check(src, dst):
    missing = []
    for kind, vals in items(src).items():
        for v in vals:
            if src.count(v) > dst.count(v):
                missing.append((kind, v))
    return missing

def main(argv):
    if len(argv) == 2 and argv[1] == "--version":
        print(VERSION); return 0
    if len(argv) != 3:
        print(__doc__); return 2
    src = open(argv[1], encoding="utf-8").read()
    dst = open(argv[2], encoding="utf-8").read()
    found = items(src)
    miss = check(src, dst)
    for kind, vals in found.items():
        print(f"{kind}: {len(vals)} in source")
    if miss:
        for kind, v in miss:
            print(f"MISSING {kind}: {v}")
        return 1
    print("PASS: all URLs, numbers and code spans preserved")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
