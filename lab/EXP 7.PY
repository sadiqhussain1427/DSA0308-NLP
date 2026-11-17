from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["playing", "played", "plays", "running", "happily"]

for word in words:
    result = ps.stem(word)
    print(word, "->", result)
