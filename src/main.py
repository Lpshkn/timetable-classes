from src.parser import parse_json
from src.excel_write import write
from src.data_json import load_data

jsonObj = load_data('./resources/test.json')
days = parse_json(jsonObj)
write(days)


