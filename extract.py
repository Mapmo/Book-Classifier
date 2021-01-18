#!/usr/bin/env python3

from bulstem.stem import BulStemmer
from collections import Counter
import glob
import json
import os
import re
import string


def read_file(path):
    tmp_fd = open(path)
    tmp_str = tmp_fd.read()
    tmp_fd.close()
    return tmp_str


def dict_word(word, words, val):
    if word in words:
        words[word] += val
    else:
        words[word] = val


cities = read_file("/root/Git/Book-Classifier/noise_data/city_names.txt")
countries = read_file("/root/Git/Book-Classifier/noise_data/country_names.txt")
stops = read_file("/root/Git/Book-Classifier/noise_data/grammar_words.txt")
names = read_file("/root/Git/Book-Classifier/noise_data/human_names.txt")

stemmer = BulStemmer.from_file('stem-context-1')

books = dict()
for category in glob.glob("*"):
    print("Starting", category)
    words_counter = 0

    os.chdir(category + "/txt")
    for book in glob.glob("*txt"):

        id, book_name = book.split('-', 1)
        if id in books.keys():
            books[id]["genre"].append(category)
            continue

        books[id] = dict()
        books[id]["name"] = book_name[:-4]
        books[id]["genre"] = list()
        books[id]["genre"].append(category)
        books[id]["words"] = list()

        book_fd = open(book)
        raw_words = dict()
        words = dict()
        try:
            for line in book_fd:
                for word in line.split():
                    dict_word(word, raw_words, 1)
        except UnicodeDecodeError:
            print("Book", book, "has some non utf-8 chars and was not scanned to the end")

        for word, count in raw_words.items():
            words_counter += count
            word = word.strip(string.punctuation + "„“—")
            if len(word) < 2 or word in cities or word in names or word in stops:
                continue
            word = word.lower()
            if re.search(r"[^а-я]", word):
                continue
            try:
                word = stemmer.stem(word)
                dict_word(word, words, count)
            except KeyError:
                continue
        raw_words.clear()
        book_fd.close()

        top_words = Counter(words).most_common(1000)

        for word in top_words:
            books[id]["words"].append(word[0])
        books[id]["words"] = ' '.join(books[id]["words"])

        top_words.clear()
        words.clear()

    os.chdir("../..")
tmp = open("/tmp/ops.json", 'w')
tmp.write(json.dumps(books, ensure_ascii=False))
