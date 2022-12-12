from qreader import QReader
import cv2
from pyzbar.pyzbar import decode

def _scanMethod1(image):
    value = ''
    decoder = cv2.QRCodeDetector()  # Declare QR Detector
    data, points, _ = decoder.detectAndDecode(image)

    if data:
        value = data

    elif points is not None:
        points = points[0]
        for i in range(len(points)):
            pt1 = [int(val) for val in points[1]]
            pt2 = [int(val) for val in points[3]]

        crop_image = image[pt1[1]:pt2[1], pt2[0]:pt1[0]]
        value = decode(crop_image)[0].data.decode("utf-8")

    return value


def _scanMethod2(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 0)
    thresh = cv2.threshold(
        blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Morph close
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

    # Find contours and filter for QR code
    cnts = cv2.findContours(close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
        x, y, w, h = cv2.boundingRect(approx)
        area = cv2.contourArea(c)
        ar = w / float(h)
        if len(approx) == 4 and area > 1000 and (ar > .85 and ar < 1.3):
            cv2.rectangle(image, (x, y), (x + w, y + h), (36, 255, 12), 3)
            ROI = image[y:y+h, x:x+w]

    value = decode(ROI)
    if len(value) > 0:
        return value[0].data.decode("utf-8")

    return ''

def scanQR(image):
    # Create a QReader instance
    qreader = QReader()
    value = qreader.detect_and_decode(image=image)

    if not value:
        value = _scanMethod1(image)

    if not value:
        value = _scanMethod2(image)

    return value