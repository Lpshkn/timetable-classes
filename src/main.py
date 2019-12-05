from src.parser import parse_json
from src.excel_write import write
from src.data_json import load_data

def main():
    jsonObj = load_data('./../resources/test.json')
    days = parse_json(jsonObj)
    write(days)

if __name__ == '__main__':
    main()

