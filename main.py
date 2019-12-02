from parser_json.parser import Teacher
from read_data.data_json import DataJson
from parser_json.parser import Timetable
import json

jsonObj = DataJson('./resources/test.json')
timetable = Timetable(jsonObj)
print(timetable.days)
