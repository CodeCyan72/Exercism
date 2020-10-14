def primes(limit):
    sand = list(range(2, limit+1)) # AKA the things you put in the sieve
    latestIndex = 0
    while latestIndex < len(sand):
        # Use latestIndex to remove multiples of that number found at 
        for i in range(sand[latestIndex] * 2, limit+1, sand[latestIndex]):
            try:
                sand.remove(i)
            except:
                pass # No need to freak out

        latestIndex += 1
    return sand