

def main():
    n = int(input("Enter n (array will be 1..2n): ").strip())
    arr = list(range(1, 2 * n + 1))
    print("Initial array:", arr)

    def op_R(a):
        # R: A1, A{n+1}, A2, A{n+2}, ..., An, A{2n}
        first = a[:n]
        second = a[n:]
        out = []
        for i in range(n):
            out.append(first[i])
            out.append(second[i])
        return out

    def op_S(a):
        # S: swap adjacent pairs: A2, A1, A4, A3, ..., A{2n}, A{2n-1}
        out = a[:]
        for i in range(0, 2 * n, 2):
            out[i], out[i + 1] = out[i + 1], out[i]
        return out

    ops = input("Enter operations (string of R/S, e.g., RSRS): ").strip()
    for ch in ops:
        if ch == 'R':
            arr = op_R(arr)
        elif ch == 'S':
            arr = op_S(arr)
        else:
            print(f"Ignoring unknown op '{ch}'")
    print("Final array:", arr)

main()