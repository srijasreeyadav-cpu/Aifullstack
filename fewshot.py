from ollama import chat

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {
        "role": "user",
        "content": "I loved the acting but the ending was disappointing."
    }
]

response = chat(
    model="llama3.2",
    messages=messages
)

print(response["message"]["content"])