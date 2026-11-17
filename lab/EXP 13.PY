import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the'
N -> 'cat' | 'mouse'
V -> 'chased'
""")

parser = nltk.TopDownChartParser(grammar)

sentence = ['the', 'cat', 'chased', 'the', 'mouse']

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
