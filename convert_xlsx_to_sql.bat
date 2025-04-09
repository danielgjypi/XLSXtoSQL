@echo off
setlocal ENABLEDELAYEDEXPANSION

echo Please place all your .XLSX files inside the "files" folder, and name them what you want the table name to be.
pause

REM Set folder with .xlsx files
set "SOURCE_DIR=files"


REM Loop through all .xlsx files
for %%f in (%SOURCE_DIR%\*.xlsx) do (
    echo Converting %%f to SQL...
    python xlsx_to_sql.py "%%f"
)

echo Done converting all files.
pause
