from colorama import init, Fore, Style

init()
MAX = 10**6 +1
isPrime = [True] * MAX
isPrime[0] = isPrime[1] = False

for i in range(2, MAX):
    if not isPrime[i]:
        continue
    for j in range(i * 2, MAX, i):
        isPrime[j] = False

entry = input("Enter a series of numbers separated by spaces: ")
A = list(map(int, entry.split()))
print("You entered:", A)

bestPrime = -1
n = len(A)
print("n =", n)
for start in range(n):
    currentSum = 0
    print(f"Starting new subarray at index {start}")
    for end in range(start, n):
        currentSum += A[end]
        print(f"  Adding A[{end}] = {A[end]}, currentSum now {currentSum}")
        if isPrime[currentSum]:
            if currentSum > bestPrime:
                bestPrime = currentSum
                print(Fore.GREEN + f"    New best prime found: {bestPrime}" + Style.RESET_ALL)
            else:

                print(Fore.YELLOW + f"    Current sum {currentSum} is prime but not larger than best prime {bestPrime}." + Style.RESET_ALL)
        else :
            print(Fore.RED + f"    Current sum {currentSum} is not prime." + Style.RESET_ALL)


print("The largest prime sum of any contiguous subarray is:", bestPrime)