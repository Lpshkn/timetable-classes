# TimetableExcelParser
## Description
Parses timetable of classes (input .xlsx file) to .xlsx file.

##### Optional arguments:  
    
  ```-i, --input``` - input .xlsx file  
  ```-o, --output``` - output .xlsx file  
  ```-k, --kvant``` - move "special" lessons to the field under the date  
  ```-d, --date``` - write information about days between current dates  
  ```-l, --logs``` - logfile (default - logs.txt)  

## Usage
- ```git clone https://github.com/LeadNess/TimetableExcelParser.git```
- ```cd timetable-classes```
- ```sudo python3 setup.py install```

- ```timetable-classes [-o, --output <output_xlsx>] [-k] [-d "dd.mm:dd.mm"] json_file```



## Example

This command converts timatable.xlsx to output.xlsx. Logfile logs.txt with information about skipped cells will be created in current folder: 

```TimetableExcelParser -i timatable.xlsx -o output.xlsx```

This command converts timatable.xlsx to output.xlsx with lessons from specified time period, where 'special lessons' will be in the cell below the date:

```TimetableExcelParser -i timatable.xlsx -o output.xlsx -k -d '10.01:15.9'```

Option `-d` can be specified as:
```
-d '01.01:10.12'
-d '1.01:10.12'
-d ' 1.1 : 10.12 '
-d ' 1 января : 10 декабря '
-d ' 01 января : 09 декабря '
```