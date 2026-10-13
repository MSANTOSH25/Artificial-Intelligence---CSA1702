from collections import deque

goal = "123456780"

moves = {
    0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
    3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8],
    6: [3, 7], 7: [4, 6, 8], 8: [5, 7]
}

def solve(start):
    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        state, steps = queue.popleft()

        if state == goal:
            return steps

        blank = state.index("0")

        for pos in moves[blank]:
            s = list(state)
            s[blank], s[pos] = s[pos], s[blank]
            new_state = "".join(s)

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, steps + 1))

    return -1

start = input("Enter 8-puzzle state (0 = blank): ")

steps = solve(start)

print("\nInitial State :", start)
print("Moves Required:", steps)
print("Goal State    :", goal)
