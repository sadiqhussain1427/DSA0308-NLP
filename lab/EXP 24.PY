import nltk

text = "Ravi bought a book. He reads it every day."

sentences = nltk.sent_tokenize(text)

print("Reference Resolution:")

for sentence in sentences:
    print(sentence)

print("He -> Ravi")
print("It -> Book")
