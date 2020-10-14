def latest(scores):
    return scores.pop()


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    scores.sort()
    scores.reverse()
    return scores[0:3]
