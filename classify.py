#!/usr/bin/env python3

import json
import pandas as pd
import sys

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
# Performance metric
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
# Binary Relevance
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer

from extract import extract_words


if len(sys.argv) != 3:
    print("Usage: python3", sys.argv[0], "DATASET BOOK")
    exit(1)

with open(sys.argv[1]) as books_fd:
    books_json = json.load(books_fd)
books = pd.DataFrame.from_dict(books_json).transpose()

multilabel_binarizer = MultiLabelBinarizer()
multilabel_binarizer.fit(books['genre'])
y = multilabel_binarizer.transform(books['genre'])

tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=7000)

xtrain, xval, ytrain, yval = train_test_split(books['words'], y, test_size=0.1, random_state=48)

xtrain_tfidf = tfidf_vectorizer.fit_transform(xtrain)
xval_tfidf = tfidf_vectorizer.transform(xval)

lr = LogisticRegression()
clf = OneVsRestClassifier(lr)
clf.fit(xtrain_tfidf, ytrain)

threshold = 0.1225  # threshold value

# predict probabilities
y_pred_prob = clf.predict_proba(xval_tfidf)
y_pred = (y_pred_prob >= threshold).astype(int)
result = f1_score(yval, y_pred, average="micro")
print(result)
N = len(books_json.popitem()[1]["words"].split())
q = extract_words(sys.argv[2], N)
q_vec = tfidf_vectorizer.transform([q])

q_pred_prob = clf.predict_proba(q_vec)
q_pred_new = (q_pred_prob >= threshold).astype(int)
print(multilabel_binarizer.inverse_transform(q_pred_new))
