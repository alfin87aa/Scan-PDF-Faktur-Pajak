# Scan PDF Faktur Pajak

File Watcher as Windows Services for Automation scan Faktur Pajak (Indonesia VAT Document) from PDF and save to SQL Server Database.

## Features

- Run as a Windows Services
- Watching New File PDF in specific inbox folder
- Scan QR Code File PDF Faktur Pajak
- Get data Faktur Pajak from DJP
- MS Sql Server as a Database For The Output Scan

## Installation

Required [Python](https://www.python.org/) Recommend 3.11 +.

Install Python Virtual Environment and Python Package.

```sh
git clone git@github.com:alfin87aa/Scan-PDF-Faktur-Pajak.git 
cd Scan-PDF-Faktur-Pajak-master
ren "config copy.ini" "config.ini"
python3 -m venv venv
.\venv\Scripts\activate
python3 -m pip install -r requirements.txt
```

Configuration

```ini
[PathWatcher]
inbox = .\FP\inbox                      # Folder directory to be watched by services
outbox = .\FP\outbox                    # Output the file after the proccess finish

[Database]
host = .\SQLEXPRESS                     # Host of the database
database = ETAX                         # Database Name
user = dev                              # Username database connection
password = 123                          # Password database connection

[Djp]
djpUrl = svc.efaktur.pajak.go.id        # DJP Url 

[Etax]
compCode = 01                           # The Service Run As Company Code Etax Application
baseUrl = http://etax.com               # Base URL Domain Etax Application
endpointlogin = /Account/Login          # Endpoint Etax Application For Login
endpointScan1 = /VatIn/getXMLrequest    # Endpoint Etax Application For Scan 1
username = test                         # User Etax Application
password = 123                          # Password Etax Application

[Logger]
logfilepath = .\logs                    # Path Folder For Logging File
```
For Install As A Windows Services...

```
Run As Administator File serviceInstall.bat
```

For Uninstall...

```
Run As Administator File serviceUninstall.bat
```