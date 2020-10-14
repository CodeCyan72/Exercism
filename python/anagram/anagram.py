def find_anagrams(word, candidates):
    lowerWord = word.lower()
    sortedWord = sorted(lowerWord)
    return [candidate for candidate in candidates if sortedWord == sorted(candidate.lower()) and lowerWord != candidate.lower()]
