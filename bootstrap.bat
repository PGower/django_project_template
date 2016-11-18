REM Setup Python Environment
virtualenv env
call env\Scripts\activate.bat
pip install -r requirements.txt

REM Setup Git Client Side Hooks
