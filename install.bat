@echo off
chcp 65001 >nul 2>&1
cls

echo.
echo   @@@@@@  @@    @@ @@      @@@@@@@  @@@@@@  @@@@@@
echo  @@       @@    @@ @@      @@      @@    @@ @@   @@
echo   @@@@@@  @@    @@ @@      @@@@@   @@    @@ @@@@@@
echo        @@ @@    @@ @@      @@      @@    @@ @@   @@
echo   @@@@@@   @@@@@@  @@@@@@@ @@       @@@@@@  @@   @@
echo.
echo   ^> CODE   intelligent terminal assistant
echo   ────────────────────────────────────────────────────
echo   installer  --  by @lavateam_IR
echo   ────────────────────────────────────────────────────
echo.

:: Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo   [ERROR] Python not found.
    echo   Please install Python from https://python.org
    echo   Make sure to check "Add Python to PATH" during install.
    pause
    exit /b 1
)

for /f "tokens=2 delims= " %%v in ('python --version 2^>^&1') do set PY_VER=%%v
echo   [OK] Python %PY_VER% detected

:: Check pip
python -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo   [ERROR] pip not found.
    pause
    exit /b 1
)
echo   [OK] pip ready

:: Create install dir
set INSTALL_DIR=%USERPROFILE%\.sulfor\pkg
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

:: Download files
echo   [~] Downloading Sulfor Code...

set BASE_URL=https://lavateam_IR.github.io/sulfor-code

powershell -Command "Invoke-WebRequest -Uri '%BASE_URL%/sulfor.py' -OutFile '%INSTALL_DIR%\sulfor.py' -UseBasicParsing" >nul 2>&1
if %errorlevel% neq 0 (
    echo   [ERROR] Failed to download sulfor.py
    echo   Check your internet connection or GitHub Pages status.
    pause
    exit /b 1
)

powershell -Command "Invoke-WebRequest -Uri '%BASE_URL%/setup.py' -OutFile '%INSTALL_DIR%\setup.py' -UseBasicParsing" >nul 2>&1
if %errorlevel% neq 0 (
    echo   [ERROR] Failed to download setup.py
    pause
    exit /b 1
)

echo   [OK] Files downloaded

:: Install
echo   [~] Installing Sulfor Code...
python -m pip install --quiet --upgrade "%INSTALL_DIR%"
if %errorlevel% neq 0 (
    echo   [ERROR] Installation failed.
    pause
    exit /b 1
)
echo   [OK] Sulfor Code installed

echo.
echo   ────────────────────────────────────────────────────
echo   Sulfor Code is ready!
echo.
echo   Run:   sulfor run
echo.
echo   by @lavateam_IR
echo   ────────────────────────────────────────────────────
echo.
pause
