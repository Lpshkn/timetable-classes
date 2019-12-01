import json


def load_data(json_file):
    """Function loads data from file to Json-object"""

    if json_file is not None:
        with open(json_file, 'r') as file:
            return json.load(file)


class DataJson:

    def __init__(self, file_json):
        self.json = load_data(file_json)
