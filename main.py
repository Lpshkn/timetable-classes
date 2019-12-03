from parser_json.parser import Teacher
from read_data.data_json import DataJson
from parser_json.parser import parse_json
import json

jsonObj = DataJson('./resources/test.json')
days = parse_json(jsonObj)

print(days)


