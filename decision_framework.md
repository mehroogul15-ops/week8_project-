# Decision Framework: RAG vs Fine-Tuning vs Both

## RAG

I would choose RAG when the system needs to use changing or frequently updated information. With RAG, I can update the source documents without retraining the model. This makes it useful for FAQs, policies, product information, manuals, and other knowledge that may change.

From this week's work, I learned that RAG also depends on having the correct knowledge base. If the questions and source documents do not match, retrieval can return irrelevant information.

## Fine-Tuning

I would choose fine-tuning when I mainly want to change how a model behaves, responds, or follows a particular style. Fine-tuning can teach the model a desired response pattern, but changing factual information requires another training run.

In my evaluation, the fine-tuned model still produced several incorrect or repetitive answers. This showed me that fine-tuning does not automatically make a model accurate.

## Both RAG and Fine-Tuning

I would use both when a project needs a specific response style or behavior as well as access to up-to-date external knowledge.

For example, a customer-support assistant could be fine-tuned to follow a helpful support style while RAG provides the latest product policies, shipping information, and FAQs.

## My Decision Process

For a new use case, I would first ask what kind of information the system needs.

1. If the main requirement is changing factual information, I would start with RAG.
2. If the main requirement is changing the model's behavior or response style, I would consider fine-tuning.
3. If both changing knowledge and specialized behavior are important, I would consider using both.
4. I would always test the chosen approach on representative evaluation questions before deciding that it works well.

## What I Learned This Week

The three-way comparison showed me that no single approach automatically solves every problem. RAG can provide useful external context, but only when the knowledge base contains information relevant to the question. Fine-tuning can influence model behavior, but it does not guarantee correct answers. The choice should therefore depend on the actual requirements and evaluation results of the use case.
