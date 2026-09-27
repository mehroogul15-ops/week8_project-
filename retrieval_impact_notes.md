# Retrieval Impact Notes

## Examples Where Retrieval Helped

1. **What is a nested loop?**
   - The model produced a response related to the question, but it did not provide the correct definition, so retrieval did not actually provide useful support.

2. **What does the return keyword do?**
   - The retrieved customer-support context was unrelated to Python, so it did not help answer the question.

3. **What does the pop() method do?**
   - The retrieved context was unrelated to the Python list method, so retrieval did not help.

## Examples Where Retrieval Did Not Help

1. **What is a local variable?**
   - Retrieval returned customer-support information about delivery instead of information about Python variables.

2. **What does the continue statement do?**
   - Retrieval returned an order-confirmation chunk, which was unrelated to the Python loop statement.

3. **What is a ZeroDivisionError?**
   - Retrieval returned payment-failure information instead of information about Python errors.

## Overall Observation

The RAG pipeline successfully retrieved and passed context to the model, but the knowledge base did not match the Python evaluation questions. This caused irrelevant customer-support information to influence the generated answers.
