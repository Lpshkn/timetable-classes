python -m venv venv
echo Created virtual environment...
.\venv\Scripts\activate
pip install -r requirements.txt
pyinstaller --onefile TimetableExcelParser.py
echo Successfully build .\dist\TimetableExcelParser.exe
