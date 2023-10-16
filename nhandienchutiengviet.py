import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
img = cv2.imread("./1.3.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
textvi = pytesseract.image_to_data(img, lang="vie")
# print(textvi)

with open("dich.txt", "a", encoding="utf-8") as f:
    f.writelines(textvi)