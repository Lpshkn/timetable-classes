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
    def __init__(self, title, list_lessons):
        self.title = title
        self.teachers = self.get_teachers(list_lessons)

    def get_teachers(self, list_lessons):
        """Gets a list of teachers with attributes"""
        teachers = {}
        for lesson in list_lessons:
            name = lesson[NAME_INDEX]
            attributes = list([lesson[GROUPS_INDEX], lesson[CLASSROOM_INDEX], lesson[IS_COMPUTER_INDEX]])
            teachers[name] = Teacher(name, attributes)
        return teachers

