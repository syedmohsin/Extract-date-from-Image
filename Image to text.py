from PIL import Image
import PIL.Image
import pandas as pd
from pytesseract import image_to_string
import pytesseract as pya

pya.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
TESSDATA_PREFIX = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
output = pytesseract.image_to_string(PIL.Image.open('1 (7).jpeg').convert("RGB"), lang='eng')
print (output)
