from src.parser import parse_json
from src.excel_write import write
from src.data_json import load_data
import sys
import argparse as ap


def arguments_parser():
    parser = ap.ArgumentParser(description="""It parses a JSON-file to .xlsx file""",
                               prog='timetable-classes')

    parser.add_argument('input',
                        help='input JSON file',
                        type=ap.FileType())

    parser.add_argument('-o', '--output',
                        help='output .xlsx file (default="output.xlsx")',
                        default='output.xlsx',
                        type=ap.FileType('w'))

    return parser


def main():
    args = arguments_parser().parse_args(sys.argv[1:])

    jsonObj = load_data(args.input.name)
    days = parse_json(jsonObj)
    write(days, args.output.name)


if __name__ == '__main__':
    main()

