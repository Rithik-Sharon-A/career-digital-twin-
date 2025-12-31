@echo off
echo ========================================
echo   Career Digital Twin - Starting...
echo ========================================
echo.

cd /d "%~dp0"

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Start Flask server
echo Starting Flask backend on http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.
python app.py

pause


