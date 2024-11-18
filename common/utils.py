import json


def build_data(json_file: str):
    test_data = []
    with open(json_file, encoding='utf-8') as f:
        json_data = json.load(f)
        for data in json_data:
            test_data.append(tuple(data.values()))
    return test_data

class Utils:
    def __init__(self):
        pass

