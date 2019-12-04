from parser_json.parser import Teacher
from read_data.data_json import DataJson
from parser_json.parser import parse_json
import json
from excel_write.excel_write import write

jsonObj = DataJson('./resources/test.json')
days = parse_json(jsonObj)
write(days)


