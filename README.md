# Simple Python Activities

A collection of beginner-friendly Python programming exercises and challenges designed to help developers practice fundamental programming concepts including algorithms, data structures, and problem-solving skills.

## 📋 What This Project Does

This repository contains 10 standalone Python activities that cover various programming concepts:

- Array manipulation and transformations
- Algorithm optimization problems
- Grid-based operations
- Prime number calculations
- String processing
- Scheduling algorithms

Each activity is self-contained in a single Python file and can be run independently to solve specific programming challenges.

## ✨ Why This Project Is Useful

- **Learn by Doing**: Practice Python programming with real problem-solving exercises
- **No External Dependencies**: Most activities use only Python standard library (except SumPrime-B which uses colorama for colored output)
- **Beginner-Friendly**: Clear code structure with straightforward implementations
- **Interview Preparation**: Similar to common coding interview questions
- **Algorithm Practice**: Covers sorting, searching, optimization, and mathematical algorithms

## 🚀 How to Get Started

### Prerequisites

- Python 3.x installed on your system
- For SumPrime-B.py: `colorama` library (install with `pip install colorama`)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Epic2077/simple-python-activities.git
cd simple-python-activities
```

2. (Optional) Install dependencies for SumPrime-B:
```bash
pip install colorama
```

### Usage

Run any activity by executing its Python file:

```bash
python ActivityName.py
```

## 📚 Activities Overview

### 1. Average.py
**Problem**: Calculate the average of a list of numbers and compute the cumulative absolute differences from the average.

**Question**: Given a list of numbers, calculate their average. Then, for each number, compute and accumulate the absolute difference from the average. What is the total accumulated difference?

**Example Input**:
```
Enter numbers separated by spaces: 5 10 15 20
```

**Expected Output**:
```
Number: 5, Average: 12.5, Difference: 7.5
Number: 10, Average: 12.5, Difference: 10.0
Number: 15, Average: 12.5, Difference: 12.5
Number: 20, Average: 12.5, Difference: 20.0
The average is: 20
```

---

### 2. Rabbit.py
**Problem**: A rabbit starts at its home position and must collect all carrots, minimizing total distance traveled, then return home.

**Question**: Given positions on a number line where negative values represent the rabbit's home and positive values represent carrot locations, what is the minimum total distance the rabbit must travel to collect all carrots and return home using a greedy nearest-neighbor approach?

**Example Input**:
```
Enter positions: -5 3 8 1 12
```

**Explanation**: 
- Home is at position 5 (negative value -5)
- Carrots are at positions: 3, 8, 1, 12
- Rabbit uses greedy approach: always go to nearest carrot next

---

### 3. RepairService.py
**Problem**: Schedule repair service visits to maximize customer satisfaction within time constraints.

**Question**: A repairman starts at location 0. Each customer has an availability time A, location L, service duration S, and return duration R. Given a specific service order, trace the repairman's schedule showing travel times, waiting times, service times, and which customers can be served before their availability window closes.

**Example Input**:
```
Enter number of customers: 3
Enter A, L, S, R for customer: 10 5 3 2
Enter A, L, S, R for customer: 15 8 4 3
Enter A, L, S, R for customer: 20 3 2 1
Enter the order of customers to be served: 1 2 3
```

**Parameters Explained**:
- A: Customer's availability time (latest arrival time)
- L: Customer's location
- S: Service duration
- R: Return duration to base (location 0)

---

### 4. Rotate.py
**Problem**: Perform rotation operations on a grid (rows and columns).

**Question**: Given an n×n grid filled with sequential numbers (1 to n²), perform m operations where each operation rotates a specific row (left/right) or column (up/down). What does the final grid look like?

**Example Input**:
```
Enter grid size n and number of operations m: 3 2
Enter operation (t k d): R 1 R
Enter operation (t k d): C 2 D
```

**Operation Format**:
- t: Type (R for row, C for column)
- k: Row/column index (1-indexed)
- d: Direction (R=right, L=left, D=down, U=up)

**Initial 3×3 Grid**:
```
1    2    3
4    5    6
7    8    9
```

---

### 5. SamePermutation.py
**Problem**: Check if two sequences are permutations of each other.

**Question**: Given two input sequences, determine if they contain the same elements (even if in different orders). This checks if one is a permutation of the other.

**Example Input**:
```
Enter the first number or series: 12345
Enter the second number or series: 54321
```

**Expected Output**:
```
True
```

---

### 6. Shuffle.py
**Problem**: Apply riffle shuffle and swap operations to an array.

**Question**: Given an array [1, 2, 3, ..., 2n], apply a sequence of operations:
- **R** (Riffle): Interleave first half with second half: [A₁, Aₙ₊₁, A₂, Aₙ₊₂, ..., Aₙ, A₂ₙ]
- **S** (Swap): Swap all adjacent pairs: [A₂, A₁, A₄, A₃, ..., A₂ₙ, A₂ₙ₋₁]

What is the final arrangement after all operations?

**Example Input**:
```
Enter n (array will be 1..2n): 3
Enter operations (string of R/S, e.g., RSRS): RS
```

**Initial Array**: [1, 2, 3, 4, 5, 6]

**After R**: [1, 4, 2, 5, 3, 6]

**After S**: [4, 1, 5, 2, 6, 3]

---

### 7. SimpleSudoju.py
**Problem**: Solve a simplified Sudoku puzzle.

**Question**: Given an n×n grid with some cells filled and others empty (0), fill in the missing values such that each row and column contains all numbers from 1 to n exactly once. The algorithm iteratively fills cells where only one number is missing in a row or column.

**Example Input**:
```
Enter number of rows and columns: 4
Enter row 1: 1230
Enter row 2: 3401
Enter row 3: 2014
Enter row 4: 0142
```

**Expected Output** (simplified Sudoku solution):
```
1234
3401
2014
4142
```

**Note**: This uses a simple iterative approach and may not solve all configurations.

---

### 8. StringCompression.py
**Problem**: Sort and count characters in a string.

**Question**: Given a string of English letters, convert all letters to uppercase, sort them alphabetically, and count the frequency of each character.

**Example Input**:
```
Enter a string of English Letters: Hello World
```

**Expected Output**:
```
The sorted string is: DEHLLLOORW
Letter counts: {'D': 1, 'E': 1, 'H': 1, 'L': 3, 'O': 2, 'R': 1, 'W': 1}
```

---

### 9. SumPrime-A.py
**Problem**: Check if the sum of array elements in a given range is a prime number.

**Question**: Given an array L and a range [a, b], calculate the sum of elements from index a to b (inclusive). If the sum is a prime number, return it; otherwise return 0.

**Example (hardcoded)**:
```
L = [10, 1, 2, 2, 5, 12, 6]
sumPrime(L, 0, 1) → 11 (10+1=11, which is prime)
sumPrime(L, 1, 3) → 5 (1+2+2=5, which is prime)
sumPrime(L, 1, 4) → 0 (1+2+2+5=10, which is not prime)
```

**Implementation**: Uses Sieve of Eratosthenes for efficient prime checking up to 10⁶.

---

### 10. SumPrime-B.py
**Problem**: Find the largest prime sum among all contiguous subarrays.

**Question**: Given an array of numbers, find the largest prime number that can be formed by summing any contiguous subarray. The algorithm checks all possible subarrays and identifies which sums are prime, tracking the maximum prime sum found.

**Example Input**:
```
Enter a series of numbers separated by spaces: 10 1 2 2 5
```

**Process**: Checks all contiguous subarrays:
- [10] = 10 (not prime)
- [10, 1] = 11 (prime) ✓
- [10, 1, 2] = 13 (prime) ✓
- [10, 1, 2, 2] = 15 (not prime)
- ... and so on

**Expected Output**:
```
The largest prime sum of any contiguous subarray is: 13
```

**Features**: Uses colored output (green for new best prime, yellow for smaller primes, red for non-primes)

**Dependency**: Requires `colorama` library for colored terminal output.

## 🔧 Running the Activities

Each activity is interactive and will prompt you for input. Simply run:

```bash
# Example: Run the Average activity
python Average.py

# Example: Run the Rabbit activity
python Rabbit.py

# Example: Run the colored prime sum finder
python SumPrime-B.py
```

## 💡 Where to Get Help

- **Issues**: Report bugs or request features via [GitHub Issues](https://github.com/Epic2077/simple-python-activities/issues)
- **Discussions**: Ask questions in [GitHub Discussions](https://github.com/Epic2077/simple-python-activities/discussions)
- **Documentation**: Each Python file contains inline comments explaining the logic

## 🤝 Who Maintains and Contributes

### Maintainer

This project is maintained by [@Epic2077](https://github.com/Epic2077).

### Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a new branch for your feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Contribution Guidelines

- Keep activities simple and self-contained
- Use clear variable names and add comments for complex logic
- Ensure code works with Python 3.x
- Test your changes before submitting
- Follow the existing code style in the repository

## 📝 License

This project is open source and available under the [MIT License](LICENSE) (if applicable).

## 🎯 Learning Objectives

By working through these activities, you will practice:

- **Data Structures**: Arrays, lists, grids, sets, dictionaries
- **Algorithms**: Sorting, searching, greedy algorithms, Sieve of Eratosthenes
- **Problem Solving**: Breaking down complex problems into smaller steps
- **Python Basics**: Input/output, loops, conditionals, functions, list comprehensions
- **Mathematical Concepts**: Prime numbers, permutations, averages, optimization

## 🌟 Future Enhancements

Potential improvements to this project:

- Add unit tests for each activity
- Create difficulty levels (beginner, intermediate, advanced)
- Add solution explanations and time/space complexity analysis
- Include alternative approaches for solving each problem
- Add visualization tools for grid-based problems

---

**Happy Coding!** 🐍
