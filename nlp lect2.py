import pandas as pd
import string
import re
import nltk 
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Sample corpus
corpus = [
    "This is the first document.",
    "This document is the second document."
]

# Bag-of-Words
vectorizer = CountVectorizer()
X_bow = vectorizer.fit_transform(corpus)
print("BoW features (array):")
print(X_bow.toarray())
print("BoW feature names:")
print(vectorizer.get_feature_names_out())

# TF-IDF
tfidf_vectorizer = TfidfVectorizer()
X_tfidf = tfidf_vectorizer.fit_transform(corpus)
print("\nTF-IDF features (array):")
print(X_tfidf.toarray())
print("TF-IDF feature names:")
print(tfidf_vectorizer.get_feature_names_out())
