import cv2 as cv
import pytesseract


class OCRService:

    user_id = 0
    img_path = "" 
    img = ""
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'


    def __init__(self, user_id, img_path):
        self.user_id = user_id
        self.img_path = img_path
        
    def run(self):
        self.img = cv.imread(self.img_path)
        self.pre_processing()
        self.read_image()
        self.test()

    def pre_processing(self):
        print("Preprocessing Image")
        # Grayscale
        grey_img = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        # Edge Detection
        self.img = cv.Canny(grey_img, 80, 80)

    def read_image(self):
        print("Reading image with tesseract")
        print(pytesseract.image_to_string(self.img))

    # Show image in display window for manual testing
    def test(self):
        cv.imshow("Display Window", self.img)
        cv.waitKey(0)

service = OCRService(111, "./main/images/one-rate_2.jpg")
service.run()