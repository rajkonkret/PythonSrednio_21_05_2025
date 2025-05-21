nasted_data = {
    "a": 1,
    "b": {
        "c": 2,
        "d": [3, 4, {"e": 5}]
    },
    "f": [6, 7]
}


# odczytanie i zsumowanie wszystkich wartości ze słownika
def sum_nestesd(data):
    total = 0
    if isinstance(data, dict):
        for key, value in data.items():
            total += sum_nestesd(value)
    elif isinstance(data, list):
        for item in data:
            total += sum_nestesd(item)
    elif isinstance(data, (int, float)):
        total += data

    return total

result = sum_nestesd(nasted_data)
print("Sum is:", result)
