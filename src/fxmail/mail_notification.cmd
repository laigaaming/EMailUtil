@echo off
cls

SETLOCAL ENABLEDELAYEDEXPANSION
SET FXData_PRJ_PATH=E:\Python\PycharmProjects\EMailUtil

python %FXData_PRJ_PATH%\src\fxmail\notification_of_completion.py

exit 0
