#!/usr/bin/env python3

import json
import pandas as pd
import sys
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
# Binary Relevance
from sklearn.multiclass import OneVsRestClassifier
# Performance metric
from sklearn.metrics import f1_score
from sklearn.feature_extraction.text import TfidfVectorizer
from extract import extract_words

books_fd = open(sys.argv[1])
books_json = json.loads(books_fd.read())
books = pd.DataFrame.from_dict(books_json).transpose()


multilabel_binarizer = MultiLabelBinarizer()
multilabel_binarizer.fit(books['genre'])
y = multilabel_binarizer.transform(books['genre'])

tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=10000)

xtrain, xval, ytrain, yval = train_test_split(books['words'], y, test_size=0.2, random_state=9)

xtrain_tfidf = tfidf_vectorizer.fit_transform(xtrain)
xval_tfidf = tfidf_vectorizer.transform(xval)

lr = LogisticRegression()
clf = OneVsRestClassifier(lr)
clf.fit(xtrain_tfidf, ytrain)

t = 0.25  # threshold value

# predict probabilities
# y_pred_prob = clf.predict_proba(xval_tfidf)
# y_pred = clf.predict(xval_tfidf)
# y_pred_new = (y_pred_prob >= t).astype(int)
# result = f1_score(yval, y_pred, average="micro")

# print(multilabel_binarizer.inverse_transform(y_pred_new)[3])

q = extract_words(sys.argv[2])
q_vec = tfidf_vectorizer.transform([q])

q_pred_prob = clf.predict_proba(q_vec)
q_pred = clf.predict(q_vec)
q_pred_new = (q_pred_prob >= t).astype(int)
print(multilabel_binarizer.inverse_transform(q_pred_new))
