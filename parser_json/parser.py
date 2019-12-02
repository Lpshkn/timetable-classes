from read_data.data_json import DataJson

NAME_INDEX = 0
GROUPS_INDEX = 1
CLASSROOM_INDEX = 2
IS_COMPUTER_INDEX = 3


class Teacher:
    """Contains information about the teacher"""

    def __init__(self, name, attributes):
        self.name = name
        self.groups = attributes[0]
        self.classroom = attributes[1]
        self.is_computer = attributes[2]


class Note:
    """Represents an info about one lesson like 'title': list_of_teachers"""

    def __init__(self, title, list_info: list):
        self.title = title
        self.teachers = self.parse(list_info)

    def parse(self, list_info):
        """Sets a list of teachers with attributes"""
        teachers = {}
        if len(list_info) != 0:
            for info in list_info:
                if len(info) != 0:
                    name = info[NAME_INDEX]
                    attributes = list([info[GROUPS_INDEX], info[CLASSROOM_INDEX], info[IS_COMPUTER_INDEX]])
                    teachers[name] = Teacher(name, attributes)
        return teachers or None


class Day:
    """Represents an info about a day"""

    def __init__(self, date, list_notes: dict):
        self.date = date
        self.notes = self.parse(list_notes)

    def parse(self, list_notes: dict):
        notes = {}
        for title in list_notes.keys():
            notes[title] = Note(title, list_notes[title])
        return notes


class Timetable:
    def __init__(self, json_object: DataJson):
        self.days = self.parse(json_object.json)

    def parse(self, json: dict):
        return [Day(day, json[day]) for day in json.keys()]
