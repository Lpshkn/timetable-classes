"""This module is required for sorting data by date"""
from collections import OrderedDict
import datetime as dt
import re

MONTHS = {"января": 1,
          "февраля": 2,
          "марта": 3,
          "апреля": 4,
          "мая": 5,
          "июня": 6,
          "июля": 7,
          "августа": 8,
          "сентября": 9,
          "октября": 10,
          "ноября": 11,
          "декабря": 12}

WEEKDAY = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]


def sort_data(json_object):
    """Function sorts a dict by date"""
    list_data = list(json_object.items())

    # element_list is an element of dictionary such as { date: value }
    # So, it's necessary to take the first element - it's the date, and sort
    # the dict by all date at first, then sort it by months.
    sort_by_month = lambda element_list: MONTHS[element_list[0].split(' ')[1]]

    list_data.sort()
    list_data.sort(key=sort_by_month)

    # Put sorted data into the ordered dict
    return OrderedDict(list_data)


def to_date(date):
    # Handle format date as 'dd.mm'
    if re.search('^ *(0?[1-9]|1[0-9]|2[0-9]|3[0-1])\.(0?[1-9]|1[0-2]) *$', date):
        date = date.strip()
        day, month = date.split('.')
        day = int(day); month = int(month)

    # Handle format date as 'dd month'
    elif re.search('^ *(0?[1-9]|1[0-9]|2[0-9]|3[0-1]) [а-я]{3,8} *$', date):
        date = date.strip()
        day, month = date.split(' ')
        day = int(day); month = MONTHS[month]
    else:
        raise Exception('Incorrect date range in -d parameter')

    year = dt.datetime.today().year
    return dt.date(year, month, day)
