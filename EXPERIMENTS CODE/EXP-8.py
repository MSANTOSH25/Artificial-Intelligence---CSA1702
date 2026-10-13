from itertools import permutations

distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cities = [1, 2, 3]
best = 9999
route = None

for p in permutations(cities):
    cost = distance[0][p[0]]

    for i in range(len(p)-1):
        cost += distance[p[i]][p[i+1]]

    cost += distance[p[-1]][0]

    if cost < best:
        best = cost
        route = (0,) + p + (0,)

print("Best Route:", route)
print("Minimum Cost:", best)
