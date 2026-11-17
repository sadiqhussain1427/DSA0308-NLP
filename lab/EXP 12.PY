import nltk
nltk.data.path.append(r'C:\Users\kakar\nltk_data')

from nltk.corpus import treebank
from nltk.tag import brill
from nltk.tag.brill_trainer import BrillTaggerTrainer
from nltk.tag import UnigramTagger

training_data = treebank.tagged_sents()[:3000]

initial_tagger = UnigramTagger(training_data)

templates = [
    brill.Template(brill.Pos([-1])),
    brill.Template(brill.Pos([1]))
]

trainer = BrillTaggerTrainer(initial_tagger, templates)
tagger = trainer.train(training_data, max_rules=10)

sentence = "The cat is playing"
words = nltk.word_tokenize(sentence)

print("Transformation-Based POS Tagging:")
print(tagger.tag(words))
