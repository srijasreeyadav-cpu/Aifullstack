with open("fest_info.txt", encoding="utf-8") as f:
    text = f.read()
print(f"Your file has {len(text)} characters.")
print()
print("sample text:",text[:300])

def chunk_text(text,chunk_size=300, overlap=50):
    chunks=[]
    start=0
    while start<len(text):
        chunks.append(text[start:start+chunk_size])
        start+=chunk_size-overlap
    return chunks 
chunks=chunk_text(text)
print(f"Total {len(chunks)} chunks created.")
for i in range(len(chunks)):
    print(f"chunk {i+1}: {chunks[i]}")
    print()
    print("----------------------------------------------")