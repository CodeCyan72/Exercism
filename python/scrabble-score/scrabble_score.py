import collections

# The 
# def foo(myWord):
# ...     letters = myWord.split()
# ...     array = [x.strip(",") for x in letters]
# ...     return array

# table = [
#     (1, ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']),
#     (2, ['D', 'G']),
#     (3, ['B', 'C', 'M', 'P']),
#     (4, ['F', 'H', 'V', 'W', 'Y']),
#     (5, ['K']),
#     (8, ['J', 'X']),
#     (10, ['Q', 'Z'])
# ]

# given = dict()
# >>> for x in table:
# ...     for y in x[1]:
# ...             given[y] = x[0]
# Look up table created using the terminal and the table above
lut = {'A': 1, 'C': 3, 'B': 3, 'E': 1, 'D': 2, 'G': 2, 'F': 4, 'I': 1, 'H': 4, 'K': 5, 'J': 8, 'M': 3, 'L': 1,
    'O': 1, 'N': 1, 'Q': 10, 'P': 3, 'S': 1, 'R': 1, 'U': 1, 'T': 1, 'W': 4, 'V': 4, 'Y': 4, 'X': 8, 'Z': 10}


def score(word):
    word = word.upper()
    letters = [x for x in word]
    counter = collections.Counter(letters)
    score = 0

    for letter in counter:
        multiplier = lut.get(letter)
        score += multiplier * counter[letter]

    return score
