import cv2 as cv
import numpy as np
import PIL
from pytesseract import image_to_string, pytesseract

class OCRService:

    user_id = 0
    img_path = "" 
    img = ""
    pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'


    def __init__(self, user_id, img_path):
        self.user_id = user_id
        self.img_path = img_path
        
    def run(self, digital=True):
        self.img = cv.imread(self.img_path)
        if(digital):
            self.digital_pre_processing()
        self.read_image()
        self.test()

    def digital_pre_processing(self):
        print("Preprocessing Image")
        # Colour reduction
        #gray_img = cv.bilateralFilter(cv.cvtColor(self.img, cv.COLOR_BGR2GRAY),11, 17, 17)
        gray_img = cv.cvtColor(self.img, cv.COLOR_BGR2HSV)
        # Edge Detection
        edged_img = cv.Canny(gray_img, 30, 50)

        self.img = edged_img

    def read_image(self):
        print("Reading image with tesseract")
        otsu_thresh_image = PIL.Image.fromarray(self.img)
        print(image_to_string(otsu_thresh_image, lang="letsgodigital"))

    # Show image in display window for manual testing
    def test(self):
        cv.imshow("Display Window", self.img)
        cv.waitKey(0)

service = OCRService(111, "./main/images/digital_1.jpg")
service.run()