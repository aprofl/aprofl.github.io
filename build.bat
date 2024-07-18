@echo off

python script/cleanup_file.py
if %errorlevel% neq 0 (
    echo Error occurred in cleanup_file.py
    exit /b %errorlevel%
)

python script/add_index.py
if %errorlevel% neq 0 (
    echo Error occurred in add_in dex.py
    exit /b %errorlevel%
)

:: 메타데이터 추가 스크립트 실행
python script/add_meta.py
if %errorlevel% neq 0 (
    echo Error occurred in add_meta.py
    exit /b %errorlevel%
)

:: 이미지 경로 변경 스크립트 실행
python script/change_image.py
if %errorlevel% neq 0 (
    echo Error occurred in change_image.py
    exit /b %errorlevel%
)


python script/cleanup_code.py
if %errorlevel% neq 0 (
    echo Error occurred in cleanup_code.py
    exit /b %errorlevel%
)

python script/sync.py
if %errorlevel% neq 0 (
    echo Error occurred in sync.py
    exit /b %errorlevel%
)

:: Image를 상대 경로로 복사
:: python copy_image.py
:: if %errorlevel% neq 0 (
::     echo Error occurred in copy_image.py
::     exit /b %errorlevel%
:: )

:: public 폴더 삭제
rmdir /s /q public

:: Hugo
hugo
if %errorlevel% neq 0 (
    echo Error occurred in hugo
    exit /b %errorlevel%
)
