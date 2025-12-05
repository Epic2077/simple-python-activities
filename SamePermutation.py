def samePermutation(seq1, seq2):
    # seq1 and seq2 are lists of ints
    if len(seq1) != len(seq2):
        return False
    return sorted(seq1) == sorted(seq2)



entry1 = input("Enter the first number or series: ")
entry2 = input("Enter the second number or series: ")



print(samePermutation(entry1, entry2))