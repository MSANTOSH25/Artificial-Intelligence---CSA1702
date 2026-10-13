colors = ["Red", "Green", "Blue"]

map_data = {
    "A": ["B", "C"],
    "B": ["A", "C"],
    "C": ["A", "B"]
}

result = {}

for region in map_data:
    for color in colors:
        if all(result.get(n) != color for n in map_data[region]):
            result[region] = color
            break

print("Map Coloring:")
for region, color in result.items():
    print(region, ":", color)
