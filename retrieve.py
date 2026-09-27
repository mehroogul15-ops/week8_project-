import re


def clean_words(text):
    return set(re.findall(r"\b\w+\b", text.lower()))


def retrieve(query, chunks):
    query_words = clean_words(query)

    scored_chunks = []

    for chunk in chunks:
        text = chunk["text"]
        text_words = clean_words(text)

        score = len(query_words & text_words)

        scored_chunks.append((score, text))

    scored_chunks.sort(reverse=True)

    return [text for score, text in scored_chunks if score > 0]
