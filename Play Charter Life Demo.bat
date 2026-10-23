@echo off
cd /d "%~dp0"
where py >nul 2>nul && (py -3 serve.py & goto :end)
where python >nul 2>nul && (python serve.py & goto :end)
echo Python 3 was not found. Install it from python.org, or use the desktop/ folder (see README.txt).
pause
:end
