@echo off
title Academia IA
cd /d "%~dp0"

echo ===================================================================
echo                     ACADEMIA IA - INICIANDO
echo ===================================================================
echo.

where node >nul 2>&1
if errorlevel 1 (
    echo [AVISO] Node.js no esta instalado en el sistema.
    echo Abriendo version autonoma directamente en tu navegador...
    start "" "Academia del Dinero.html"
    echo.
    echo Podes instalar Node.js desde https://nodejs.org/ para el servidor completo.
    pause
    exit /b 0
)

echo Iniciando servidor web de Academia IA...
echo (Esta ventana mantendra corriendo el servidor web)
echo.

cd /d "%~dp0academia_dinero_v2"
node server.js

if errorlevel 1 (
    echo.
    echo Ocurrio un problema al ejecutar el servidor.
    echo Abriendo version autonoma de respaldo...
    cd /d "%~dp0"
    start "" "Academia del Dinero.html"
    pause
)
