import nltk
nltk.data.path.append(r'C:\Users\kakar\nltk_data')

from nltk.corpus import wordnet

word = "dog"

synsets = wordnet.synsets(word)

print("Word:", word)
print("Synsets:")

for syn in synsets:
    print(syn.name(), ":", syn.definition())
