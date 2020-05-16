#!/usr/bin/env python3

import requests
import nltk

url = "https://raw.githubusercontent.com/PdxCodeGuild/Programming102/master/resources/countwords.txt"

r = requests.get(url)

raw_text = r.text
text_no_newlines = raw_text.replace("\n", " ")

words = nltk.word_tokenize(text_no_newlines)

word_dist = nltk.FreqDist(words)

print(f"10 most common words: {word_dist.most_common(10)}")
