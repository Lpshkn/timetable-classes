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

    def __str__(self):
        return f'{self.name}: groups={self.groups}, classroom={self.classroom}, iscomputer={self.is_computer}'

    def __repr__(self):
        return self.__str__()


def parse_teachers(list_info):
    """Gets a list of teachers with attributes"""
    teachers = []
    if len(list_info) != 0:
        for info in list_info:
            if len(info) != 0:
                name = info[NAME_INDEX]
                attributes = [info[GROUPS_INDEX], info[CLASSROOM_INDEX], info[IS_COMPUTER_INDEX]]
                teachers.append(Teacher(name, attributes))
    return teachers or None


def parse_notes(list_notes: dict):
    """Gets a list of notes classes like 'title' : list_of_teachers_with_attributes """
    notes = {}
    for key, value in list_notes.items():
        notes[key] = parse_teachers(value)
    return notes


class Day:
    """Represents an info about a day"""

    def __init__(self, date, list_notes: dict):
        self.date = date
        self.notes = parse_notes(list_notes)

    def __str__(self):
        return f'\n{self.date}:\n' \
               f'   {self.notes}'

    def __repr__(self):
        return self.__str__()


class Timetable:
    def __init__(self, json_object: DataJson):
        self.days = self.parse(json_object.json)

    def parse(self, json: dict):
        return [Day(day, json[day]) for day in json.keys()]
