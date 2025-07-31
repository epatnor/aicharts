:: start_dashboard.bat
@echo off
setlocal

:: Gå till scriptets katalog
cd /d %~dp0

echo 🚀 Starting AICharts setup...

:: Hämta senaste ändringar från GitHub
echo 🔄 Pulling latest changes from GitHub...
git pull || (
    echo ❌ Failed to pull from GitHub
    exit /b 1
)

:: Skapa och aktivera virtuell miljö om den saknas
if not exist venv\Scripts\activate.bat (
    echo 📦 Creating virtual environment...
    python -m venv venv || (
        echo ❌ Failed to create virtual environment
        exit /b 1
    )
)

call venv\Scripts\activate.bat

:: Uppgradera pip tyst
python -m pip install --upgrade pip >nul

:: Installera beroenden
echo 📦 Installing dependencies...
pip install -r requirements.txt || (
    echo ❌ Failed to install packages
    exit /b 1
)

:: Kör scraper för att hämta senaste benchmarkdata
echo 🧹 Running scraper...
python scraper.py || (
    echo ❌ Scraper failed
    exit /b 1
)

:: Starta servern direkt (i samma fönster)
echo 🌐 Starting server...
python server.py

:: (valfritt) Öppna webbläsaren efter 2 sekunder
:: timeout /t 2 >nul
:: start http://localhost:8000

echo ✅ Done!
endlocal
