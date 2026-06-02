@echo off
set /p msg=请输入提交信息: 
git.exe add .
git.exe commit -m "%msg%"
git.exe push --progress "origin" main:main
pause