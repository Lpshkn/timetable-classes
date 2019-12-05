from src.data_json import DataJson
from src.parser import parse_json
from src.excel_write import write

jsonObj = DataJson('./resources/test.json')
days = parse_json(jsonObj)
write(days)


