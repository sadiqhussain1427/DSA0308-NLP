text = "I love natural language processing"

words = text.split()

print("Bigrams:")

for i in range(len(words) - 1):
    print(words[i], words[i+1])

print("Generated Text:")
print(text)
