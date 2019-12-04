"""Each value in the Json-object represents as
{
    'Date':
            {
                'Note_1' : list_info_about_teachers,
                ...
                'Note_4' : list_info_about_teachers
            }
}
Therefore, there is defines a parser of json-object, then defines a parser of Notes and list of teachers
with theirs attributes(name, groups, classroom, is computer)"""

from read_data.data_json import DataJson

NAME_INDEX = 0
GROUPS_INDEX = 1
CLASSROOM_INDEX = 2
IS_COMPUTER_INDEX = 3


def parse_teachers(list_info) -> tuple:
    """Gets a list of teachers with attributes"""
    teachers = []
    if len(list_info) != 0:
        for info in list_info:
            if len(info) != 0:
                name = info[NAME_INDEX]
                attributes = [info[GROUPS_INDEX], info[CLASSROOM_INDEX], info[IS_COMPUTER_INDEX]]
                teachers.append(Teacher(name, attributes))
    return tuple(teachers) or None


def parse_notes(list_notes: dict) -> tuple:
    """Gets a list of notes classes like 'title' : list_of_teachers_with_attributes """
    notes = []
    for title, value in list_notes.items():
        teachers = parse_teachers(value)
        if teachers is not None:
            note = Note(title, teachers)
            notes.append(note)
    return tuple(notes) or None


def parse_json(json_object: DataJson) -> tuple:
    """Function parses json object to a list of days"""
    days = []
    for date, value in json_object.json.items():
        notes = parse_notes(value)
        if notes is not None:
            day = Day(date, notes)
            days.append(day)
    return tuple(days)


class Day:
    def __init__(self, date, notes):
        self.date = date
        self.notes = notes


class Note:
    def __init__(self, title, teachers):
        self.title = title
        self.teachers = teachers


class Teacher:
    """Contains information about the teacher"""

    def __init__(self, name, attributes):
        self.name = name
        self.groups = attributes[0]
        self.classroom = attributes[1]
        self.is_computer = attributes[2]
