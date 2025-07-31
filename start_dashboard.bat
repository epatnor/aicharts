:: start_dashboard.bat
@echo off
setlocal

echo 🚀 Starting AICharts setup...

:: Pull latest changes from GitHub
echo 🔄 Pulling latest changes from GitHub...
git pull || (
    echo ❌ Failed to pull from GitHub
    exit /b 1
)

:: Create and activate virtual environment if missing
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
) else (
    echo 📦 Creating virtual environment...
    python -m venv venv
    if exist venv\Scripts\activate.bat (
        call venv\Scripts\activate.bat
    ) else (
        echo ❌ Failed to create virtual environment
        exit /b 1
    )
)

:: Upgrade pip (silently)
python -m pip install --upgrade pip >nul

:: Install required packages
echo 📦 Installing dependencies...
pip install -r requirements.txt || (
    echo ❌ Failed to install packages
    exit /b 1
)

:: Run scraper to fetch latest benchmark data
echo 🧹 Running scraper...
python scraper.py || (
    echo ❌ Scraper failed
    exit /b 1
)

:: Start backend server in a new console window
echo 🌐 Starting server...
start cmd /k "python server.py"

:: Open dashboard in browser after delay
timeout /t 2 >nul
start http://localhost:8000

echo ✅ Done!
endlocal
