
for /R %%f in (*.ui) do (
pyside2-uic "%%~nf".ui -o "%%~nf".py
ReplaceText.vbs %%~nf.py "import icons_rc" "import user_interface.icons_rc")
pause
