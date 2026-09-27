import os
import json

input_folder = "knowledge_base"
output_file = "chunks.jsonl"

chunks = []

for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        filepath = os.path.join(input_folder, filename)

        with open(filepath, "r", encoding="utf-8") as file:
            text = file.read().strip()

        if text:
            chunks.append({
                "source": filename,
                "text": text
            })

with open(output_file, "w", encoding="utf-8") as file:
    for chunk in chunks:
        file.write(json.dumps(chunk) + "\n")

print(f"Created {len(chunks)} chunks.")
