import json


def load_data(json_file = None, json_object = None):
    """Function loads data from file/string to Json-object"""

    if json_file is not None:
        with open(json_file, 'r') as file:
            return json.load(file)

    elif json_object is not None:
        return json.loads(json_object)

    raise IOError('На вход не подан ни файл, ни строка')


class DataJson:

    def __init__(self, file_json):
        self.json = load_data(file_json)


