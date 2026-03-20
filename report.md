# 📊 Offline Customer Support Chatbot Evaluation Report

## 1. Introduction
This project aims to build an offline customer support chatbot using Ollama and Llama 3.2 (3B). The goal is to evaluate how well a locally hosted LLM can handle e-commerce queries and compare zero-shot and one-shot prompting techniques.

---

## 2. Methodology

### Data Preparation
20 customer queries were created by adapting technical support questions into e-commerce scenarios such as order tracking, returns, and payment issues.

### Prompting Techniques
- **Zero-Shot Prompting**: Only instructions provided
- **One-Shot Prompting**: Instructions + one example

### Evaluation Metrics
- Relevance (1–5)
- Coherence (1–5)
- Helpfulness (1–5)

---

## 3. Results & Analysis

### Average Scores

| Method | Relevance | Coherence | Helpfulness |
|--------|----------|----------|-------------|
| Zero-Shot | X.X | X.X | X.X |
| One-Shot | X.X | X.X | X.X |

### Observations

- One-shot prompting produced more structured and consistent responses.
- Zero-shot responses were sometimes generic and less helpful.
- One-shot responses followed tone and format better due to example guidance.

### Example Comparison

**Query:** "My discount code is not working"

- Zero-Shot: Basic suggestion
- One-Shot: Clear steps + friendly tone

---

## 4. Conclusion

The Llama 3.2 3B model is capable of handling basic customer support queries offline. One-shot prompting significantly improves response quality. However, limitations include lack of real-time data access and occasional vague answers.

---

## 5. Limitations

- No access to actual order database
- Possible hallucinations
- Slower response time (CPU-based)

---

## 6. Future Improvements

- Add retrieval system (RAG)
- Use larger models
- Integrate with real database
- Improve prompt engineering