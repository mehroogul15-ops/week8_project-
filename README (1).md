# RAG vs Fine-Tuning Showdown

## Use Case

This project compares a fine-tuned model with a Retrieval-Augmented Generation (RAG) system for answering questions using a specific knowledge base.

## What is RAG?

RAG stands for Retrieval-Augmented Generation. In simple words, RAG first searches a knowledge base for useful information and then uses the retrieved information to generate an answer.

## Headline Result

The RAG system was evaluated on the same evaluation questions used for the fine-tuned model. The results are documented in `three_way_comparison.md`.

## What I Would Try Next

For future improvements, I would consider combining RAG with fine-tuning, improving retrieval quality, adding re-ranking, and expanding the knowledge base.

## Project Structure

- `knowledge_base/` — source knowledge
- `chunks.jsonl` — chunked knowledge
- `chunk_documents.py` — document chunking
- `build_index.py` — index construction
- `retrieve.py` — retrieval
- `rag_pipeline.py` — RAG pipeline
- `rag_eval_results.jsonl` — RAG evaluation results
- `retrieval_samples.md` — retrieval examples
- `retrieval_impact_notes.md` — retrieval analysis
- `three_way_comparison.md` — base vs fine-tuned vs RAG comparison
- `decision_framework.md` — RAG vs fine-tuning decision framework
