@echo off
setlocal
if not exist "%~dp0viewer\node.exe" (
  echo Please use Extract All on the ZIP first, then open this file in the extracted folder.
  pause
  exit /b 1
)
set "POLYCYTHEMIA_VIEWER_HOME=%~dp0viewer"
"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -NonInteractive -WindowStyle Hidden -Command "$nodePath=Join-Path $env:POLYCYTHEMIA_VIEWER_HOME 'node.exe'; $scriptPath=Join-Path $env:POLYCYTHEMIA_VIEWER_HOME 'server.mjs'; Start-Process -FilePath $nodePath -ArgumentList ([char]34 + $scriptPath + [char]34) -WorkingDirectory $env:POLYCYTHEMIA_VIEWER_HOME -WindowStyle Hidden"
if errorlevel 1 (
  echo The presentation could not start. Keep the extracted folder together and try again.
  pause
)
endlocal
