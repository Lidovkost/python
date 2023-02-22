def inverse_geometric_progression(times, number = 1, progression_size = 2):
    if times == 1:
        return number
    return number + inverse_geometric_progression(times-1, number/(-progression_size),progression_size)
print(inverse_geometric_progression(122))