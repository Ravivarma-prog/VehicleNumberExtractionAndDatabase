import pytesseract
from PIL import Image
import cv2
import os

pytesseract.pytesseract.tesseract_cmd = r'C:/Users/Admin/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

directory  = r'F:/PythonProject/images'

def extractText(img):
    try:
        plateNumber = pytesseract.image_to_string(img)
    except:
        plateNumber = "Error in pytesseract"
    
    return plateNumber


def openImg(imageNo): 
    print('Opening image no : ' + str(imageNo) + ' and ', end = ' ')
    try:
        img = cv2.imread(directory+'/'+ str(imageNo) +'.png')
        # cv2.imshow('Plate',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        s = extractText(img)
        number = ""
        for c in s:
            if(ord(c) >= 48 and ord(c) <= 57):
                number = number+c
            if(ord(c) >= 65 and ord(c) <= 90):
                number = number+c

        print('plate number is : ' + number)  
        print()      

    except:
        print("Error in opening")

def start():
    numberOfImages = len(os.listdir(directory))
    for i in range(1,numberOfImages+1):
        openImg(i)

def extract(path):
    print('Opening image : ' + path)
    try:
        img = cv2.imread(path)
        # cv2.imshow('Plate',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        s = extractText(img)
        number = ""
        for c in s:
            if(ord(c) >= 48 and ord(c) <= 57):
                number = number+c
            if(ord(c) >= 65 and ord(c) <= 90):
                number = number+c

        print('plate number is : ' + number)  
        print()      

    except:
        print("Error in opening")
    
    return number