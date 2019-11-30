from PIL import Image
import PIL.Image

from pytesseract import image_to_string
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
TESSDATA_PREFIX = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
output = pytesseract.image_to_string(PIL.Image.open('1 (7).jpeg').convert("RGB"), lang='eng')
print (output)

f = open("output2.txt", "a")
print(output, file=f)
f.close()
