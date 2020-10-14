def distance(strand_a, strand_b):
    if (len(strand_a) == len(strand_b)):
        hamDist = 0
        for i in range(len(strand_a)):
            if strand_a[i] != strand_b[i]:
                hamDist += 1
        return hamDist
    else:
        raise ValueError("Strings were not of the same length")
