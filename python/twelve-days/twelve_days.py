table = [
    "twelve Drummers Drumming, ",
    "eleven Pipers Piping, ",
    "ten Lords-a-Leaping, ",
    "nine Ladies Dancing, ",
    "eight Maids-a-Milking, ",
    "seven Swans-a-Swimming, ",
    "six Geese-a-Laying, ",
    "five Gold Rings, ",
    "four Calling Birds, ",
    "three French Hens, ",
    "two Turtle Doves, and ",
    "a Partridge in a Pear Tree."
]

ith = [
    'zeroth',
    'first',
    'second',
    'third',
    'fourth',
    'fifth',
    'sixth',
    'seventh',
    'eighth',
    'ninth',
    'tenth',
    'eleventh',
    'twelfth'
]

def recite(start_verse, end_verse):
    result = []
    while(start_verse < end_verse + 1):
        output = "On the " + ith[start_verse] +" day of Christmas my true love gave to me: "
        for i in range(start_verse):
            output += table[12 - start_verse + i]   # this probably should get cleaned up
        result.append(output)
        start_verse += 1
    return result
