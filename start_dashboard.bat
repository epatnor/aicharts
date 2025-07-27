:: start_dashboard.bat
@echo off
setlocal

:: Activate virtual environment if it exists
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
) else (
    echo Creating virtual environment...
    python -m venv venv
    call venv\Scripts\activate.bat
)

:: Install required packages
pip install -r requirements.txt

:: Run scraper to fetch latest data
python scraper.py

:: Start backend server in a new console window
start cmd /k "python server.py"

:: Open the dashboard in default browser
timeout /t 2 >nul
start http://localhost:8000

endlocal
