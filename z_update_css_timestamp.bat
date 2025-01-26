@echo off
setlocal

REM Change to the directory where the script is located
cd /d "%~dp0"

REM Get the current timestamp in seconds
for /f "tokens=*" %%a in ('powershell -Command "[int][double]::Parse((Get-Date).ToUniversalTime().Subtract([datetime]'1970-01-01').TotalSeconds)"') do set current_time_stamp=%%a

REM Print a message indicating the update is happening
echo Updating styles.css timestamp...

REM Loop through all .html files in the current directory
for %%f in (*.html) do (
    REM Use PowerShell to perform the replacement in each file
    powershell -Command "(Get-Content '%%f') -replace '<link rel=\"stylesheet\" href=\"styles.css.*\">', '<link rel=\"stylesheet\" href=\"styles.css?%current_time_stamp%\">' | Set-Content '%%f'"
)

endlocal