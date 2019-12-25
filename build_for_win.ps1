python -m venv venv
Write-Host "Created virtual environment..."
.\venv\Scripts\activate
pip install -r requirements.txt
pyinstaller --onefile TimetableExcelParser.py
Write-Host "Successfully build .\dist\TimetableExcelParser.exe"