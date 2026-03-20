import requests
import json

# ==============================
# CONFIG
# ==============================
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"

# ==============================
# QUERIES (20)
# ==============================
queries = [
    "How do I track my order?",
    "My discount code is not working at checkout.",
    "Can I change my delivery address after placing the order?",
    "What is your return policy?",
    "I received a damaged product. What should I do?",
    "How long does shipping take?",
    "My payment failed but money was deducted. What now?",
    "Can I cancel my order after placing it?",
    "Do you offer cash on delivery?",
    "How do I apply a coupon code?",
    "I haven't received my order confirmation email.",
    "Why is my order delayed?",
    "Can I exchange a product instead of returning it?",
    "How do I contact customer support?",
    "Do you ship internationally?",
    "My order shows delivered but I didn’t receive it.",
    "How can I reset my account password?",
    "Are there any ongoing discounts or offers?",
    "What payment methods do you accept?",
    "How do I update my account details?"
]

# ==============================
# LOAD PROMPT TEMPLATES
# ==============================
def load_template(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

zero_shot_template = load_template("prompts/zero_shot_template.txt")
one_shot_template = load_template("prompts/one_shot_template.txt")

# ==============================
# QUERY OLLAMA FUNCTION
# ==============================
def query_ollama(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_ENDPOINT, json=payload)
        response.raise_for_status()

        result = response.json()
        return result.get("response", "").strip()

    except Exception as e:
        return f"Error: {str(e)}"

# ==============================
# MAIN EXECUTION
# ==============================
def main():
    with open("eval/results.md", "w", encoding="utf-8") as f:
        # Write table header
        f.write("| Query # | Customer Query | Prompt Type | Response | Relevance | Coherence | Helpfulness |\n")
        f.write("|--------|----------------|-------------|----------|-----------|-----------|--------------|\n")

        for i, query in enumerate(queries, start=1):
            print(f"Processing Query {i}...")

            # Zero-shot
            zero_prompt = zero_shot_template.replace("{query}", query)
            zero_response = query_ollama(zero_prompt)

            # One-shot
            one_prompt = one_shot_template.replace("{query}", query)
            one_response = query_ollama(one_prompt)

            # Write to file
            f.write(f"| {i} | {query} | Zero-Shot | {zero_response} |  |  |  |\n")
            f.write(f"| {i} | {query} | One-Shot | {one_response} |  |  |  |\n")

    print("\n✅ Results saved to eval/results.md")

# ==============================
# RUN
# ==============================
if __name__ == "__main__":
    main()