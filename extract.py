#!/usr/bin/env python3

from bulstem.stem import BulStemmer
import glob
import os
import sys
import re
import string
import tempfile


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


if (len(sys.argv) < 3):
    print("Please, give barrier that defines a word as book specific, and a barrier that defines a word as genre specific")
    exit(1)

tmp_file_fd = tempfile.NamedTemporaryFile()
tmp_file = tmp_file_fd.name

cities = read_file("/root/Git/Book-Classifier/noise_data/city_names.txt")
countries = read_file("/root/Git/Book-Classifier/noise_data/country_names.txt")
stops = read_file("/root/Git/Book-Classifier/noise_data/grammar_words.txt")
names = read_file("/root/Git/Book-Classifier/noise_data/human_names.txt")

stemmer = BulStemmer.from_file('stem-context-1')
for category in glob.glob("*"):
    print("Starting", category)
    words_counter = 0
    words_per_book = open(tmp_file, 'w')

    os.chdir(category + "/txt")
    for book in glob.glob("*txt"):
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

        for word, count in words.items():
            if (count > words_counter * sys.argv[1]):  # best so far 0.00001
                words_per_book.write(word + "\n")
        words.clear()
    words_per_book.close()

    # After processing each book, summarize the category
    words = dict()
    words_per_book = open(tmp_file)
    for word in words_per_book:
        dict_word(word, words, 1)
    words_per_book.close()

    words_per_category = open("../" + category + ".words", "w")
    for key, val in words.items():
        if (val > len(glob.glob("*txt")) * sys.argv[2]):  # best so far 0.1
            words_per_category.write(key)

    words_per_category.close()
    os.chdir("../..")
