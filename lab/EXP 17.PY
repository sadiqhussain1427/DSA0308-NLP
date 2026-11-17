import nltk

grammar = nltk.PCFG.fromstring("""
S -> NP VP [1.0]
NP -> Det N [0.6] | 'John' [0.4]
VP -> V NP [0.7] | V [0.3]
Det -> 'the' [1.0]
N -> 'dog' [0.5] | 'cat' [0.5]
V -> 'saw' [1.0]
""")

parser = nltk.ViterbiParser(grammar)

sentence = ['John', 'saw', 'the', 'dog']

print("PCFG Parsing:")

for tree in parser.parse(sentence):
    print(tree)
    print("Probability:", tree.prob())
