from PIL import Image
import PIL.Image
import pandas as pd
from pytesseract import pytesseract as pytesser
from pytesseract import image_to_string 

pytesser.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
TESSDATA_PREFIX = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
output = image_to_string(PIL.Image.open('1 (12).jpeg').convert("RGB"), lang='eng')
print (output)
