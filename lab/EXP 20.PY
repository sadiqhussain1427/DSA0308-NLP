import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'every' | 'a'
N -> 'student' | 'book'
V -> 'reads'
""")

parser = nltk.ChartParser(grammar)

sentence = ['every', 'student', 'reads', 'a', 'book']

print("FOPC Parser Output:")

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
