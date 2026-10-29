@echo off
chcp 65001 >nul
title Academia IA - Vinculador de Dominio FreeDomain
cd /d "%~dp0"

echo ===================================================================
echo     ACADEMIA IA - VINCULAR DOMINIO FREEDOMAIN (.dpdns.org / .us.kg)
echo ===================================================================
echo.
echo Este asistente te permite conectar tu servidor local de Academia IA
echo con un dominio público gratuito de DigitalPlat FreeDomain.
echo.
echo Pasos previos:
echo  1. Registrá tu dominio en https://dash.domain.digitalplat.org/
echo  2. Asignale los nameservers de Cloudflare según el tutorial.
echo.
echo ===================================================================
echo Seleccioná una opción:
echo   [1] Iniciar servidor local (http://localhost:8000)
echo   [2] Generar túnel público con localtunnel (npx localtunnel)
echo   [3] Abrir guía paso a paso de FreeDomain (CONFIGURAR_DOMINIO_FREEDOMAIN.md)
echo   [4] Salir
echo ===================================================================
echo.
set /p opt="Opción [1-4] (por defecto 1): "
if "%opt%"=="" set opt=1

if "%opt%"=="1" goto start_local
if "%opt%"=="2" goto start_tunnel
if "%opt%"=="3" goto open_guide
if "%opt%"=="4" exit /b 0

:start_local
echo.
echo Iniciando servidor en http://localhost:8000...
start "Academia IA - Servidor" /min cmd /k "cd /d \"%~dp0academia_dinero_v2\" && npx http-server . -p 8000 -c-1"
ping 127.0.0.1 -n 3 >nul
start "" http://localhost:8000
echo Servidor iniciado. Podés vincularlo a tu dominio FreeDomain.
pause
exit /b 0

:start_tunnel
echo.
echo Asegurate de que el servidor local esté corriendo.
set /p sub="Elegí un subdominio para el túnel (ej: miacademia2026): "
if "%sub%"=="" set sub=academiaia%RANDOM%
echo Levantando túnel público para http://localhost:8000...
echo Copiá la URL resultante y usala como CNAME en tu DNS de FreeDomain.
npx localtunnel --port 8000 --subdomain %sub%
pause
exit /b 0

:open_guide
start "" notepad "CONFIGURAR_DOMINIO_FREEDOMAIN.md"
exit /b 0
