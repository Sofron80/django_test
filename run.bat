@echo off

IF %1.==m. GOTO :No1
IF %1.==mm. GOTO :No2
IF %1.==. GOTO :No3

GOTO End1

:No1
echo %1
python manage.py migrate
goto :End3

:No2
python manage.py makemigrations
goto :End3

:No3
python manage.py runserver
GOTO :End3

:End3




