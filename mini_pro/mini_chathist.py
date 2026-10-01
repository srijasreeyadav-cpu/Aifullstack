from ollama import chat 
print("WELCOME VANDY!!! HOPING TO HAVE A GREAT CONVERSATION....")
system_msg = "you are a friendly tutor,answer in a warm way,in just one line "
history = [{"role": "system","content":system_msg}]
while True:
    question= input("You:")
    if question == "":
        print("Sana🤖:Please type something!!!")
        continue
    if question.lower().strip() == "/history":
        print("----Your Conversation so far....")
        if len(history)<2:
            print("Nothing here so far!")
        for msg in history[1:]:
            if msg["role"] == "user":
                speaker = "You"
            else:
                speaker = "Sana🤖"
            print(f"{speaker}:{msg['content']}")
        print("...................................")
        print()
        continue
    if question.lower().strip()=="/clear":
        history=[{"role":"system","content":system_message}]
        print("Sana🤖:Conversation history cleared. start a fresh conversation!")
        print()
        continue
    if question.lower().strip()=="/help":
        print("----Available Commands----")
        print("/history - View conversation history")
        print("/clear - Clear conversation history")
        print("/help - Show this help message")
        print("/exit - Exit the chatbot")
        print("--------------------------")
        print()
        continue
    if question.lower().strip()=="/personality":
        print("Sana🤖:I am a rapper chatbot, I answer in a rap style with 1 line rhyme and an emoji at the end of my answer.")
        print()
        continue
    if question.lower().strip() == "exit":
        print("Sana🤖: See you soon vandy...please come back soon!🤧🤧🤧")
        break
    history.append({"role" : "user","content" : question})
    try:
        response = chat(
            model = "llama3.2",
            messages = history
        )
        reply = response['message']['content']
        history.append({"role":"assisstant","content":reply})
        print(f"Sana🤖:{reply}")
        print()
    except Exception as e:
        print(f"Sana🤖:Something went wrong....{e}")