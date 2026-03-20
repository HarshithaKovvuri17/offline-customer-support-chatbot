# 🤖 Offline Customer Support Chatbot (Ollama + Llama 3.2)

## 📌 Project Overview
This project implements an offline AI-powered customer support chatbot for a fictional e-commerce platform using Ollama and the Llama 3.2 (3B) model.

The chatbot is capable of answering common customer queries such as order tracking, return policies, payment issues, and account management — all without sending any data to external servers. This ensures complete data privacy and eliminates API costs.

---

## 🎯 Objective
- Build a fully offline chatbot using a local LLM
- Compare Zero-Shot and One-Shot prompting techniques
- Evaluate model performance using manual scoring
- Understand prompt engineering and LLM behavior

---

## 🚀 Features
- ✅ Fully offline (no internet required after setup)
- ✅ Uses Llama 3.2 model via Ollama
- ✅ Supports Zero-Shot and One-Shot prompting
- ✅ Handles 20 real-world e-commerce queries
- ✅ Stores responses in structured format
- ✅ Includes manual evaluation system

---

## 🧠 Technologies Used
- Python3
- Ollama (Local LLM runtime)
- Llama 3.2 (3B model)
- Requests Library (API calls)
- Huggingface Datasets (optional)

---

## 🏗️ System Architecture
User Query
↓
chatbot.py
↓
HTTP Request (POST)
↓
Ollama Server (localhost:11434)
↓
Llama 3.2 Model
↓
Generated Response
↓
Saved to eval/results.md


---

## 📂 Project Structure
```
offline-chatbot/
│
├── chatbot.py                     ✅ Main Python script
├── README.md                      ✅ Project overview
├── setup.md                       ✅ Setup instructions
├── report.md                      ✅ Evaluation analysis
│
├── prompts/                       ✅ Prompt templates folder
│   ├── zero_shot_template.txt
│   └── one_shot_template.txt
│
├── eval/                          ✅ Output folder
│   └── results.md
│
├── .gitignore           
└── venv/                          (DO NOT upload to GitHub)
```
---

## 🧪 Prompting Techniques

### 🔹 Zero-Shot Prompting
- No examples provided
- Model relies only on instructions

### 🔹 One-Shot Prompting
- Includes one example
- Improves response quality and structure

---

## 📊 Evaluation Metrics

The chatbot responses are evaluated manually using:

- **Relevance (1–5)** → How well response matches query
- **Coherence (1–5)** → Grammar and clarity
- **Helpfulness (1–5)** → Practical usefulness

---

## 📈 Key Findings

- One-Shot prompting produced more structured and helpful responses
- Zero-Shot responses were sometimes generic
- Llama 3.2 performs well for basic customer support tasks
- Prompt design significantly impacts output quality

---

## ⚠️ Limitations

- No access to real-time order or user data
- Possible hallucinations in responses
- Slower performance on CPU systems
- Limited reasoning compared to larger models

---

## 🔮 Future Improvements

- 🔹 Integrate Retrieval-Augmented Generation (RAG)
- 🔹 Connect to real database for live data
- 🔹 Use larger models (7B / 13B)
- 🔹 Build UI using Streamlit or React
- 🔹 Add conversation memory

---

## 🏁 Conclusion

This project demonstrates that local LLMs like Llama 3.2 can be effectively used to build privacy-focused customer support systems. One-shot prompting significantly enhances performance, making prompt engineering a critical skill in AI application development.

---

## 👩‍💻 Author

Kovvuri Harshitha

---

## 📌 Note

This project is built for educational purposes to explore offline AI capabilities and prompt engineering techniques.