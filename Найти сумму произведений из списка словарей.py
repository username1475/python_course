import json

# TODO решите задачу
def task() -> float:
    with open('input.json', 'r') as file:
        json_data = json.load(file)
    result = [dct['score']*dct['weight'] for dct in json_data]
    return round(sum(result), 3)

print(task())
