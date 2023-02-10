chcp 65001
@echo off
echo 创建文件中...
for /l %%i in (0, 1, 10) do (
	echo 第%%i个文件 >> 文件.%%i.txt
)
echo 创建完毕