@echo off
title Setup + Run Python Project

echo ==============================
echo  Verificando Python...
echo ==============================

python --version >nul 2>&1
if errorlevel 1 (
    echo Python nao encontrado no PATH.
    echo Tentando com "py"...
    py --version >nul 2>&1
    if errorlevel 1 (
        echo ERRO: Python nao instalado ou nao no PATH.
        pause
        exit /b
    ) else (
        set PY=py
    )
) else (
    set PY=python
)

echo.
echo Usando: %PY%

echo ==============================
echo  Atualizando pip
echo ==============================
%PY% -m pip install --upgrade pip

echo ==============================
echo  Instalando requirements.txt
echo ==============================
if exist requirements.txt (
    %PY% -m pip install -r requirements.txt
) else (
    echo ERRO: requirements.txt nao encontrado.
    pause
    exit /b
)

echo ==============================
echo  Rodando script.py
echo ==============================
if exist script.py (
    %PY% script.py
) else (
    echo ERRO: script.py nao encontrado.
    pause
    exit /b
)

pause