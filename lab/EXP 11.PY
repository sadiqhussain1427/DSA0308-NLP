import nltk

text = "The cat is playing happily"
words = nltk.word_tokenize(text)

patterns = [
    (r".*ing$", "VBG"),
    (r".*ly$", "RB"),
    (r".*s$", "NNS"),
    (r".*", "NN")
]

tagger = nltk.RegexpTagger(patterns)
tags = tagger.tag(words)

print("Rule-Based POS Tagging:")
print(tags)
