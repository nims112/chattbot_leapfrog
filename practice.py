import ollama

def ask(prompt):
     response=ollama.chat(
          model="qwen2.5:3b",
          messages=[{"role": "user", "content": prompt}]
     )
     return response['message']['content']

promt="Hello"
print(ask(promt))
