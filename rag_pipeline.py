import json
import sys
import faiss
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("knowledge_base.index")

with open("chunk_metadata.json", "r", encoding="utf-8") as file:
    chunks = json.load(file)

model_path = "/content/drive/MyDrive/flan_t5_day5/checkpoint-27"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

def answer_question(question, top_k=3):
    query_embedding = embedding_model.encode(
        [question],
        normalize_embeddings=True
    )

    scores, indices = index.search(query_embedding, top_k)

    context = "\n\n".join(
        chunks[index_id]["text"]
        for index_id in indices[0]
    )

    prompt = f"""Answer the question using only the information provided in the context.
If the context does not contain the answer, say: "The provided context does not contain enough information to answer this question."

Context:
{context}

Question:
{question}

Answer:"""

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=100
    )

    return tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

if __name__ == "__main__":
    question = " ".join(sys.argv[1:])
    print("\nQuestion:", question)
    print("Answer:", answer_question(question))
