position = list(map(int, input("Enter positions: ").split()))

for x in position:
    if x < 0:
        home = -x
        break

carrots = [x for x in position if x > 0]

current = home
total = 0

while carrots:

    distances = [(abs(c - current), c) for c in carrots]
    distances.sort()

    nearest = distances[0][1]

    total += abs(nearest - current)
    print()
    current = nearest

    carrots.remove(nearest)

total += abs(home - current)

print("Total distance traveled by the rabbit:", total)