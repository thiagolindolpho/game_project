def reward(map):
    if map["difficult"] == "easy":
        return 30
    if map["difficult"] == "normal":
        return 50
    if map["difficult"] == "hard":
        return 100
