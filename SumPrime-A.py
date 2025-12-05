def makeSieve(limit=10**6):
    isPrime = [True] * limit
    isPrime[0] = isPrime[1] = False
    max_i = int(limit**0.5) + 1
    for i in range(2, max_i):
        if isPrime[i] == False:
            continue
        for j in range(i * i, limit, i):
            isPrime[j] = False
    return isPrime

isPrime = makeSieve()

def sumPrime(L, a, b,):
    total = 0
    for i in range(a, b + 1):
        total += L[i]
        print(f"Adding L[{i}] = {L[i]}, total now {total}")

    if total >= 0 and total < len(isPrime) and isPrime[total]:
        print(f"Total {total} is prime.")
        return total
    else:
        return 0

L = [10, 1, 2, 2, 5, 12, 6]
print(sumPrime(L, 0, 1))
print(sumPrime(L, 1, 3))
print(sumPrime(L, 1, 4))