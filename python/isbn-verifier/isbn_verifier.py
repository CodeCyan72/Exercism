def is_valid(isbn):
    digits = [int(x) for x in isbn if x.isdigit()]
    if len(digits) == 9 and isbn[len(isbn) - 1] == 'X':
        digits.append(10)
    digits.reverse()
    if len(digits) == 10:
        for i in range(1, 11):
            digits[i-1] *= i
        value = sum(digits)
        if (value % 11) == 0:
            return True
    return False
