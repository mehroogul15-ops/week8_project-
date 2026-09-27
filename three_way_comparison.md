# Three-Way Comparison

## Scoring
- **Strong** = accurate, clear, complete, and directly answers the question.
- **Acceptable** = partly correct or useful, but missing important detail.
- **Weak** = incorrect, irrelevant, incomplete, repetitive, or contains invented information.

| # | Question | Base Model | Fine-Tuned Model | RAG Model |
|---|---|---|---|---|
| 1 | What is a local variable? | Weak | Weak | Weak |
| 2 | What does the continue statement do? | Weak | Weak | Weak |
| 3 | What is a nested loop? | Weak | Weak | Weak |
| 4 | What does the return keyword do? | Weak | Weak | Weak |
| 5 | What is a ZeroDivisionError? | Weak | Acceptable | Weak |
| 6 | What is mutable vs immutable? | Weak | Weak | Weak |
| 7 | What is the purpose of the pass statement? | Weak | Weak | Weak |
| 8 | What does the pop() method do? | Weak | Weak | Weak |
| 9 | What is a TypeError? | Weak | Weak | Weak |

## Tallies

### Base Model
- Strong: 0
- Acceptable: 0
- Weak: 9

### Fine-Tuned Model
- Strong: 0
- Acceptable: 1
- Weak: 8

### RAG Model
- Strong: 0
- Acceptable: 0
- Weak: 9

## Outright Wins, Ties, and Losses

Because all three systems were evaluated on the same nine questions:

- **Base Model:** 0 outright wins, 8 ties, 1 loss
- **Fine-Tuned Model:** 1 outright win, 8 ties, 0 losses
- **RAG Model:** 0 outright wins, 8 ties, 1 loss

The fine-tuned model was the only system rated above weak on a question: its ZeroDivisionError answer was partially correct because it identified the concept as a zero-division error, although it did not explain the cause.

## Important Observation

The RAG system used a customer-support knowledge base while the evaluation questions were about Python programming. Because the knowledge base did not contain the required Python information, retrieval often supplied irrelevant customer-support context. This shows that RAG quality depends heavily on having a knowledge base that matches the questions being asked.

The fine-tuned model also performed poorly overall, with repetitive or incorrect answers on most questions.

The base model produced short but generally incorrect or incomplete answers on this evaluation set.

This comparison is intentionally honest: the results do not show a strong system on these particular Python evaluation questions.
