import collections as c

def is_pangram(sentence):
    sentence = sentence.upper()
    letters = [x for x in sentence]
    counter = c.Counter()
    for i in letters:
        if i.isalpha():
            counter[i] += 1
    if len(counter.keys()) == 26:
        return True
    else:
        return False


