import heapq

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 2)],
    'C': [('D', 1)],
    'D': []
}

h = {'A': 4, 'B': 2, 'C': 1, 'D': 0}

def astar(start, goal):
    queue = [(h[start], 0, start)]
    visited = set()

    while queue:
        f, cost, node = heapq.heappop(queue)

        if node == goal:
            return cost

        if node in visited:
            continue

        visited.add(node)

        for next_node, weight in graph[node]:
            new_cost = cost + weight
            heapq.heappush(
                queue,
                (new_cost + h[next_node], new_cost, next_node)
            )

print("Shortest Cost:", astar('A', 'D'))
