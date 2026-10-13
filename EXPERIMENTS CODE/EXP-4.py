from collections import deque

def solve():
    start = (3, 3, 1)
    goal = (0, 0, 0)

    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        m, c, boat = state

        if state == goal:
            print("Solution Found")
            print("Number of Steps:", len(path))
            return

        moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

        for dm, dc in moves:
            if boat == 1:
                new = (m-dm, c-dc, 0)
            else:
                new = (m+dm, c+dc, 1)

            nm, nc, nb = new

            if 0 <= nm <= 3 and 0 <= nc <= 3:
                if (nm == 0 or nm >= nc) and (3-nm == 0 or 3-nm >= 3-nc):
                    if new not in visited:
                        visited.add(new)
                        queue.append((new, path + [new]))

solve()
