words = ["The", "cat", "runs"]

tag_prob = {
    "The": {"DT": 0.9, "NN": 0.1},
    "cat": {"NN": 0.8, "VB": 0.2},
    "runs": {"VBZ": 0.9, "NNS": 0.1}
}

print("Stochastic POS Tagging:")

for word in words:
    tag = max(tag_prob[word], key=tag_prob[word].get)
    print(word, "->", tag)
