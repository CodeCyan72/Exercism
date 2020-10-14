import re
def abbreviate(words):
    return "".join([x.upper().strip("_")[0] for x in re.split('[\s-]+',words)])
