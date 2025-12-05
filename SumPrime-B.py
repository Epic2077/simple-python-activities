def makeSieve():
    MAX = 10 ** 6 +1
    isPrime = [True] * MAX
    isPrime[0] = isPrime[1] = False
    for i in range(2, MAX):
        if not isPrime[i]:
            continue
        for j in range(i * i, MAX, i):
            isPrime[j]= False
    return isPrime

isPrime = makeSieve()

def sumBiggestPrime(A):
    bestPrime = -1
    n = len(A)

    nonContiguousSum = 0
    for start in range(n):
        currentSum = 0
        for end in range(start, n):
            currentSum += A[end]
            currentNon = A[start] + A[end]
            if isPrime[currentNon] and currentNon > nonContiguousSum:
                nonContiguousSum = currentNon


            if isPrime[currentSum]:
                if currentSum > bestPrime and currentSum > nonContiguousSum:
                    bestPrime = currentSum
                else:
                    bestPrime = nonContiguousSum
    return bestPrime

print("The largest prime sum of any contiguous subarray is:", sumBiggestPrime([10, 1, 2, 2, 5, 12, 6]))