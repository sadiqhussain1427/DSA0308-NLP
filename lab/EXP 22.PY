from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "Natural language processing is interesting",
    "Machine learning is a part of artificial intelligence",
    "Natural language processing uses machine learning"
]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

print("TF-IDF Features:")
print(vectorizer.get_feature_names_out())

print("\nTF-IDF Matrix:")
print(tfidf_matrix.toarray())
