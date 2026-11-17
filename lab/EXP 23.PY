import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the' | 'a'
N -> 'boy' | 'ball'
V -> 'kicked'
""")

parser = nltk.ChartParser(grammar)

sentence = ['the', 'boy', 'kicked', 'a', 'ball']

print("Syntax-Driven Semantic Analysis:")

for tree in parser.parse(sentence):
    print(tree)
