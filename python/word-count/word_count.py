import collections
import re

def count_words(sentence):
    sentence = sentence.lower()
    words = re.split('\s', sentence)
    words = [word.strip("'!&@$%^") for word in words]
    counter = collections.Counter()
    for word in words:
        if word != "":
            counter[word] += 1
    return counter
