"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""
import numpy as np
import collections as col
# Score categories.
# Change the values as you see fit.
YACHT = lambda dice: 50 if np.all(list(map(lambda x: x == dice[0], dice))) else 0
ONES = lambda dice : dice.count(1)
TWOS = lambda dice : dice.count(2) * 2
THREES = lambda dice : dice.count(3) * 3
FOURS = lambda dice : dice.count(4) * 4
FIVES = lambda dice : dice.count(5) * 5
SIXES = lambda dice : dice.count(6) * 6
FULL_HOUSE = lambda dice : sum(dice) if isHouse(dice) else 0
FOUR_OF_A_KIND = lambda dice : 4 * isFour(dice)
LITTLE_STRAIGHT = lambda dice : 30 if np.all(list(map(lambda x : np.any(list(map(lambda a : a == x, dice))), range(1,6)))) else 0
BIG_STRAIGHT = lambda dice : 30 if np.all(list(map(lambda x : np.any(list(map(lambda a : a == x, dice))), range(2,7)))) else 0
CHOICE = lambda dice: sum(dice)


def isFour(dice):
    counter = col.Counter(dice)
    if len(counter) < 3:
        for i in range(1, 7):
            if counter[i] >= 4:
                return i
    return 0

def isHouse(dice):
    counter = col.Counter(dice)
    if len(counter) == 2:
        myList = list(counter)
        amount = counter[myList[0]]
        if amount == 2 or amount == 3:
            return True
    return False

def score(dice, category):
    return category(dice)
