import nltk

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

words = ["playing", "cats", "happily", "studies"]

for word in words:
    print(word, "->", lemmatizer.lemmatize(word))
