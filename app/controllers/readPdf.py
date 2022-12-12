import os
from pathlib import Path
import uuid

from .djp import ValidateUrlDjp, Service
from .scanQr import scanQR
from app.config import FOLDER_OUTBOX, COMP_CODE
from ..models import LogScanPDF
from pdf2image import convert_from_path
from ..database import session as db
import shutil
import numpy as np

async def fakturPajak(pathFile):
    file = Path(pathFile)
    
    pages = convert_from_path(
        file, poppler_path=os.getcwd() + r'\poppler-22.12.0\Library\bin')  # Covert PDF To Image
    img = np.array(pages[-1])  # Get last page
    
    destination = FOLDER_OUTBOX + "\\" + \
                str(uuid.uuid4()) + '.' + file.name.split(".")[-1]
    shutil.move(file, destination)

    logScanPDF = LogScanPDF(
        full_path = destination,
        file_name = file.name,
        company_code = COMP_CODE
    )

    qr = scanQR(img)

    if not qr and ValidateUrlDjp(qr) == False:
        logScanPDF.status = 'error'
        logScanPDF.notes = 'QR Code Faktur Pajak Not Found!'
        db.add(logScanPDF)
        db.commit()
        return

    fp = Service(qr)

    if not fp:
        logScanPDF.status = 'error'
        logScanPDF.notes = 'Faktur tidak Valid, Tidak ditemukan data di DJP'
        db.add(logScanPDF)
        db.commit()
        return
    
    logScanPDF.status = 'success'
    logScanPDF.notes = fp
    db.add(logScanPDF)
    db.commit()
