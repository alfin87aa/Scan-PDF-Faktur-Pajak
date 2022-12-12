import json
import os
from urllib.parse import urlparse
import xmltodict
import requests

from app.config import DJP_URL

def _getDjp(url):
    response = requests.get(url)
    if response.status_code != 200:
        return _getDjp(url)

    return response.text


def ValidateUrlDjp(url):
    format = DJP_URL

    parsed = urlparse(url)
    if (parsed.netloc == format and (parsed.scheme == "http" or parsed.scheme == "https")):
        return True
    else:
        return False

def _formatingJsonFp(fp, url):
    fp['url'] = url

    fp['formatedNomorFaktur'] = fp['kdJenisTransaksi'] + \
        fp['fgPengganti'] + '.' + fp['nomorFaktur'][0:3] + \
        '-' + fp['nomorFaktur'][3:5] + '.' + \
        fp['nomorFaktur'][5:7] + '.' + fp['nomorFaktur'][-6:]

    fp['formatedNpwpPenjual'] = fp['npwpPenjual'][0:2] + '.' + \
        fp['npwpPenjual'][2:5] + '.' + fp['npwpPenjual'][5:8] + \
        '.' + fp['npwpPenjual'][8:9] + '-' + \
        fp['npwpPenjual'][9:12] + '.' + fp['npwpPenjual'][-3:]

    fp['formatedNpwpLawanTransaksi'] = fp['npwpLawanTransaksi'][0:2] + '.' + \
        fp['npwpLawanTransaksi'][2:5] + '.' + fp['npwpLawanTransaksi'][5:8] + \
        '.' + fp['npwpLawanTransaksi'][8:9] + '-' + \
        fp['npwpLawanTransaksi'][9:12] + '.' + fp['npwpLawanTransaksi'][-3:]
    return json.dumps(fp)

def Service(url):
    fpXml = _getDjp(url)
    data_dict = xmltodict.parse(fpXml)

    json_data = json.dumps(data_dict)
    resp = json.loads(json_data)

    if resp['resValidateFakturPm']['statusApproval'] != 'Faktur tidak Valid, Tidak ditemukan data di DJP':
        return _formatingJsonFp(resp['resValidateFakturPm'], url)
    return ''