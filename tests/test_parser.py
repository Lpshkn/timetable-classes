"""Test for the parser module"""

import unittest
import json
import read_data.data_json as dj
import parser_json.parser as parser


class ParserTest(unittest.TestCase):
    def test_parse(self):
        json_obj = parser.DataJson('tests_resources/test.json')
        tt = parser.Timetable(json_obj)
        print(tt.days)

