def vacuum():
    rooms = {"A": "Dirty", "B": "Dirty"}

    print("Initial:", rooms)

    for room in rooms:
        if rooms[room] == "Dirty":
            rooms[room] = "Clean"

    print("Final  :", rooms)

vacuum()
