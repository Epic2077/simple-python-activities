entry = input("Enter a string of English Letters: ")
A = "".join(sorted(entry.upper()))
print("The sorted string is:", A)

def countLetters(A):
    letterCount = {}
    for letter in A: 
        if letter in letterCount:
            letterCount[letter] += 1
        else:
            letterCount[letter] = 1

    return letterCount
    
print("Letter counts:", countLetters(A))