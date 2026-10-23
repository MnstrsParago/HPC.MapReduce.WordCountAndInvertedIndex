import sys

for line in sys.stdin:

    parts = line.strip().lower().split()

    if not parts:
        continue

    doc_id = parts[0]

    for word in parts[1:]:
        print(f"{word}\t{doc_id}")
