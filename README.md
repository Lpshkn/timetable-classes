# Timetable of classes
## Description
This is a parser of JSON files to Excel table.

##### Positional arguments:  

```input``` - input JSON file

##### Optional arguments:

```-o, --output``` - output .xlsx file

```-k, --kvant``` - move "special" lessons to the field under the date

```-d, --date``` - print dates specify in date string

## Usage
- ```git clone https://github.com/Nikshepel/timetable-classes.git```
- ```cd timetable-classes```
- ```sudo python3 setup.py install```

- ```timetable-classes [-o, --output <output_xlsx>] [-k] [-d "dd.mm:dd.mm"] json_file```



## Example:

This command converts my_json_file.json (JSON file) to file.xlsx (Excel file)  

```timetable-classes -o file.xlsx my_json_file.json```

This command creates .xlsx file which 'special lessons' are in the cell below the date and 
prints only days specify in the this range

```timetable-classes -o file.xlsx -k -d '10.01:15.9' file.json```

Option `-k` may be such as
```
-d '01.01:10.12'
-d '1.01:10.12'
-d ' 1.1 : 10.12 '
-d ' 1 января : 10 декабря '
-d ' 01 января : 09 декабря '
```