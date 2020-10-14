class Luhn:
    array = []
    validChars = True
    def __init__(self, card_num):
        self.array = []
        self.validChars = True # True till proven otherwise
        try:
            self.array.extend([int(x) for x in ''.join(card_num.split())])
        except: # Remember that there was an invalid character
            self.validChars = False
        

    def valid(self):
        # Based off of a check in reading the characters in
        if self.validChars == False:
            return False

        if len(self.array) > 1:
            temp = []
            temp.extend(reversed(self.array))
            for i in range(1, len(temp), 2):
                temp[i] *= 2
                if temp[i] > 9:
                    temp[i] -= 9

            tempSum = sum(temp)
            if (tempSum % 10) == 0:
                return True
            else:
                return False
        else:
            return False

# haha = Luhn('59')
# value = haha.valid()