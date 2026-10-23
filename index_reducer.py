import sys

current_word = None
docs = []

for line in sys.stdin:

    word, doc_id = line.strip().split("\t")

    if word == current_word:

        if doc_id not in docs:
            docs.append(doc_id)

    else:

        if current_word is not None:
            print(f"{current_word}\t{','.join(docs)}")

        current_word = word
        docs = [doc_id]

if current_word is not None:
    print(f"{current_word}\t{','.join(docs)}")
