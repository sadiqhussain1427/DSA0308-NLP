import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "The cat sits on the mat"

words = nltk.word_tokenize(text)

tags = nltk.pos_tag(words)

print("POS Tagging:")
print(tags)
