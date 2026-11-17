import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the'
N -> 'dog' | 'cat'
V -> 'chased'
""")

parser = nltk.EarleyChartParser(grammar)

sentence = ['the', 'dog', 'chased', 'the', 'cat']

print("Earley Parser Output:")

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
