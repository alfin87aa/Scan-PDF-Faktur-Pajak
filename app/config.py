from configparser import ConfigParser
import os

config = ConfigParser()
config.read(os.getcwd() + '\config.ini')

FOLDER_INBOX = config['PathWatcher']['inbox']
FOLDER_OUTBOX = config['PathWatcher']['outbox']

SQLALCHEMY_DATABASE_URI = f'mssql+pyodbc://{config["Database"]["user"]}:{config["Database"]["password"]}@{config["Database"]["host"]}/{config["Database"]["database"]}?'\
    'driver=SQL+Server' \
    '&TrustServerCertificate=yes' \
    '&authentication=ActiveDirectoryIntegrated'

DJP_URL = config['Djp']['djpUrl']

COMP_CODE = config['Etax']['compCode']
BASE_URL = config['Etax']['baseUrl']
ENDPOINT_LOGIN = config['Etax']['endpointlogin']
ENDPOINT_SCAN1 = config['Etax']['endpointScan1']
USERNAME = config['Etax']['username']
PASSWORD = config['Etax']['password']
