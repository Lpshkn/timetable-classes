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
**WARNING**: When installed on windows requires python3 as 'python' in '%PATH" variable  
- ```git clone https://github.com/Nikshepel/timetable-classes.git```
- ```cd timetable-classes```
- Depending on the system: ```./build_for_linux``` or ```powershell .\build_for_win.ps1```  
Сreated executable file will be located in TimetableExcelParser/dist/
- ```TimetableExcelParser [-i, --input <input_xlsx> [-o, --output <output_xlsx>] [-d, --dates "dd.mm:dd.mm"] [-k, --kvant] [-l, --logs <logfile>] ```



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
