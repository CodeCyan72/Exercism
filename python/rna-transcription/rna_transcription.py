table = {
    "A":"U",
    'T':'A',
    'C':'G',
    'G':'C'
}

def to_rna(dna_strand):
    transcriptedStrand = ""
    for x in dna_strand:
        if (table.get(x) != None):
            transcriptedStrand += table.get(x)
        else:
            raise Exception("That is not a valid input!")
    return transcriptedStrand
