#!/usr/bin/env python3

from bulstem.stem import BulStemmer
from collections import Counter
import glob
import json
import os
import re
import string
import sys


def read_file(filename):
    path = os.path.join(os.path.dirname(sys.argv[0]), "noise_data", filename)
    with open(path) as tmp_fd:
        return tmp_fd.read()


def dict_word(word, words, val):
    if word in words:
        words[word] += val
    else:
        words[word] = val


cities = read_file("city_names.txt")
countries = read_file("country_names.txt")
stops = read_file("grammar_words.txt")
names = read_file("human_names.txt")

stemmer = BulStemmer.from_file('stem-context-1')


def extract_words(book, N):
    with open(book) as book_fd:
        raw_words = dict()
        words = dict()
        try:
            for line in book_fd:
                for word in line.split():
                    dict_word(word, raw_words, 1)
        except UnicodeDecodeError:
            print("Book", book, "has some non utf-8 chars and was not scanned to the end")

        for word, count in raw_words.items():
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

    top_words = Counter(words).most_common(N)
    words.clear()

    tmp = list()
    for word in top_words:
        tmp.append(word[0])

    top_words.clear()
    return ' '.join(tmp)


def main():
    books = dict()
    for category in glob.glob("*"):
        print("Starting", category)

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
            N = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
            books[id]["words"] = extract_words(book, N)

        os.chdir("../..")

    with open("/tmp/ops.json", 'w') as tmp:
        json.dump(books, tmp, ensure_ascii=False)


if __name__ == "__main__":
    main()
