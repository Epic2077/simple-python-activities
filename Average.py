def average(numbers):
    av = sum(numbers) / len(numbers) if numbers else 0

    space = 0
    for i in range(len(numbers)):
        space = space + abs(numbers[i] - av)
        print(f"Number: {numbers[i]}, Average: {av}, Difference: {space}")
    return int(space)

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("The average is:", average(numbers))