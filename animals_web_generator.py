import json


def load_data(file_path):
    """
    :param file_path: animal_data.json
    :return: Function to load the JSON data from a file
    """
    with open(file_path, "r") as file:
        data = json.load(file)
        return data