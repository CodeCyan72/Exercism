def is_isogram(string):
    myString = string.lower()
    tracker = dict()
    valid = True
    for x in myString:
        if x.isalpha():
            if (tracker.get(x) == None):
                tracker[x] = 1
            else:
                valid = False
                break
    return valid

