def plural(word):
    if word.endswith(("s", "sh", "ch", "x", "z")):
        return word + "es"
    elif word.endswith("y") and word[-2] not in "aeiou":
        return word[:-1] + "ies"
    else:
        return word + "s"


words = ["cat", "box", "baby", "book"]

for word in words:
    print(word, "->", plural(word))
