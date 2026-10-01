from ollama import chat
bad ="tell me about MOON"
good = "describe the moon  to a 19 years girl, including its importance, and a brief note also some quotes about beauty of the moon. Use simple language with clear headings and bullet points. Keep the explanation within 300 words and avoid complex scientific terms."
responseB = chat(
    model="llama3.2",
      messages=[
          {
              "role": "user",
                "content": bad
          }
                ]
            )
responseG = chat(
    model="llama3.2",
      messages=[
          {
              "role": "user",
                "content": good
          }
                ]
            )

print(f"Bad prompt response:{responseB['message']['content']}")
print(f"Good prompt response:{responseG['message']['content']}")