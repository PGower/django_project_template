REM Setup Python Environment
virtualenv env
call env\Scripts\activate.bat
pip install -r requirements.txt

REM Setup Git Client Side Hooks

REM Setup Docs Folder with Sphinx
sphinx-quickstart.exe -q --sep --project="{{ project_name }}" --author="Paul Gower" -v "0.1" -r "0.1" -l "en" --suffix=".rst" --master="index" --ext-autodoc --makefile --batchfile ..\..\docs
