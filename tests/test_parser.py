"""Test for the parser module"""

import unittest
import src.parser as parser


class ParserTest(unittest.TestCase):
    def test_parse(self):
        json_obj = parser.DataJson('tests_resources/test.json')
        tt = parser.Timetable(json_obj)
        print(tt.days)

