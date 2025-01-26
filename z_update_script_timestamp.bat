@echo off
setlocal

REM Change to the directory where the script is located
cd /d "%~dp0"

REM Get the current timestamp in seconds
for /f "tokens=*" %%a in ('powershell -Command "[int][double]::Parse((Get-Date).ToUniversalTime().Subtract([datetime]'1970-01-01').TotalSeconds)"') do set current_time_stamp=%%a

REM Print a message indicating the update is happening
echo Updating script.js timestamp...

REM Use PowerShell to perform the replacement in script.js
powershell -Command "(Get-Content 'script.js') -replace 'fetch\(\''left-panel.html[^\'']*\''\)', 'fetch(''left-panel.html?t=%current_time_stamp%'')' | Set-Content 'script.js'"

endlocal