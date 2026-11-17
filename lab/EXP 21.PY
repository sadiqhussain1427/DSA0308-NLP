import nltk
nltk.data.path.append(r'C:\Users\kakar\nltk_data')

from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

sentence = "I went to the bank to deposit money"

words = word_tokenize(sentence)

sense = lesk(words, 'bank')

print("Sentence:", sentence)
print("Word: bank")

if sense:
    print("Meaning:", sense.definition())
else:
    print("Meaning not found")
