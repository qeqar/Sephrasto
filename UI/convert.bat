for /r %%f in (*.ui) do CALL pyuic5.bat -x %%~nf.ui -o ../%%~nf.py