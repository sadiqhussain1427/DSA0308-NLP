import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the'
N -> 'boy' | 'ball'
V -> 'kicked'
""")

parser = nltk.ChartParser(grammar)

sentence = ['the', 'boy', 'kicked', 'the', 'ball']

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
