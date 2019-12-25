import sys
import argparse
import logging
from src.timetable2json.JSONSerializer import JSONSerializer
from src.timetable_classes.parser import parse_json
from src.timetable_classes.excel_write import write
from src.timetable_classes.date import sort_data


def create_parser():
    parser = argparse.ArgumentParser(
        prog='TimetableExcelParser',
        description='Parses timetable of classes (input .xlsx file) to .xlsx file',
        epilog='(c) LeadNess/Nikshepel 2019',
    )
    parser.add_argument(
        '-i', '--input',
        help='input .xlsx file',
        type=argparse.FileType(),
        required=True
    )
    parser.add_argument(
        '-o', '--output',
        help='output .xlsx file (default="output.xlsx")',
        default='output.xlsx',
        type=str
    )
    parser.add_argument(
        '-k', '--kvant',
        help='move information about lessons in KVANT to the first line under date',
        action='store_true'
    )
    parser.add_argument(
        '-d', '--dates',
        help='''write information about days between current dates
        (dates format: '01.01:10.12' or '1 января : 10 декабря')
        ''',
        type=str
    )
    parser.add_argument(
        '-l', '--logs',
        help='logfile (default - logs.txt)',
        default='logs.txt'
    )
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args(sys.argv[1:])

    logger = logging.getLogger("timetable_parser")
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler(args.logs, mode='w')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    json_object = JSONSerializer.serialize(excel_file=args.input.name).loads()
    json_object = sort_data(json_object)
    days = parse_json(json_object, args.kvant)
    write(days, args.output)

    print("Complete parsing %s into %s, written logs to %s" % (args.input.name, args.output, args.logs))


if __name__ == '__main__':
    main()
