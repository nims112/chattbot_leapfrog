import ollama
def ask(prompt):
    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {"role": "system", "content": "You are a helpful assistant.You only answer in greek."},
            {"role": "user", "content": prompt},
            ]
    )
    return response["message"]["content"]

promt="Hello"
print(ask(promt))