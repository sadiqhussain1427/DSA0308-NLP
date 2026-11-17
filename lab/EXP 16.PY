import nltk

grammar = nltk.CFG.fromstring("""
S -> NP_SG VP_SG
S -> NP_PL VP_PL
NP_SG -> 'He' | 'She'
NP_PL -> 'They' | 'We'
VP_SG -> 'runs' | 'plays'
VP_PL -> 'run' | 'play'
""")

parser = nltk.ChartParser(grammar)

sentences = [
    ['He', 'runs'],
    ['They', 'run'],
    ['She', 'plays'],
    ['We', 'play']
]

for sentence in sentences:
    print("Sentence:", " ".join(sentence))
    trees = list(parser.parse(sentence))
    if trees:
        print("Correct Subject-Verb Agreement")
    else:
        print("Incorrect Subject-Verb Agreement")
