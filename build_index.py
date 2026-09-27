import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

with open("chunks.jsonl", "r", encoding="utf-8") as file:
    chunks = [json.loads(line) for line in file]

texts = [chunk["text"] for chunk in chunks]

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(texts, normalize_embeddings=True)

embeddings = np.array(embeddings, dtype="float32")

index = faiss.IndexFlatIP(embeddings.shape[1])
index.add(embeddings)

faiss.write_index(index, "knowledge_base.index")

with open("chunk_metadata.json", "w", encoding="utf-8") as file:
    json.dump(chunks, file, indent=2)

print(f"Indexed {len(chunks)} chunks.")
print(f"Embedding size: {embeddings.shape[1]}")
