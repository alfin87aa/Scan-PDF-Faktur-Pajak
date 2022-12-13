cd %~dp0
START /B /WAIT .\nssm.exe install eTaxScanPDF %~dp0venv\Scripts\python.exe %~dp0main.py
START /B /WAIT .\nssm.exe set eTaxScanPDF DisplayName "eTax Scan QR On PDF Faktur Pajak"
START /B /WAIT .\nssm.exe set eTaxScanPDF Description "Watcher PDF File Faktur Pajak And Scan The QR Code"
START /B /WAIT .\nssm.exe set eTaxScanPDF AppDirectory %~dp0
START /B /WAIT .\nssm.exe set eTaxScanPDF Start SERVICE_AUTO_START
START /B /WAIT .\nssm.exe set eTaxScanPDF AppStdout %~dp0logs\stdout.log
START /B /WAIT .\nssm.exe set eTaxScanPDF AppStderr %~dp0logs\stderr.log
START /B /WAIT .\nssm.exe start eTaxScanPDF
PAUSE