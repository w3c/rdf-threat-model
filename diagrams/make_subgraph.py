import re
import sys

def fail(msg: str, code: int):
    print(msg, file=sys.stderr)
    exit(code)

if len(sys.argv) != 2:
    fail(f"usage: {sys.argv[0]} <filename_or_number>", 1)

m = re.search(r'[0-9]+(?=(\.[a-zA-Z0-9]+)?$)', sys.argv[1])
if m is None:
    fail("filename must end with a number, possibly followed by a single extension", 2)
N = m.group()

for line in sys.stdin:
    ex = re.search(r'# except(\s+[0-9]+)+\s*$', line)
    if ex and re.search(rf'\b{N}\b', ex.group()):
        print(f"# {line}", end="")
    else:
        print(line, end="")
