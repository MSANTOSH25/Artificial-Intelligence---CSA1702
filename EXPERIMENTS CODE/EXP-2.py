from collections import deque

def water_jug(a, b, target):
    queue = deque([(0, 0)])
    visited = set()

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if x == target or y == target:
            return (x, y)

        states = [
            (a, y),              # Fill Jug A
            (x, b),              # Fill Jug B
            (0, y),              # Empty Jug A
            (x, 0),              # Empty Jug B
            (x - min(x, b-y), y + min(x, b-y)),
            (x + min(y, a-x), y - min(y, a-x))
        ]

        for state in states:
            if state not in visited:
                queue.append(state)

    return None

a = int(input("Enter capacity of Jug A: "))
b = int(input("Enter capacity of Jug B: "))
target = int(input("Enter target amount: "))

result = water_jug(a, b, target)

print("\nSolution:", result)
print("Target achieved:", target)
