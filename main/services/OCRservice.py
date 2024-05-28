import cv2 as cv

class OCRService:

    user_id = 0
    img_path = ""
    img = ""

    def __init__(self, user_id, img_path):
        self.user_id = user_id
        self.img_path = img_path
        
    def run(self):
        self.img = cv.imread(self.img_path)
        self.pre_processing()
        self.test()

    def pre_processing(self):
        # Pre process edit image
        # Grayscale
        grey_img = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        # Edge Detection
        self.img = cv.Canny(grey_img, 80, 80)

    # Show image in display window for manual testing
    def test(self):
        cv.imshow("Display Window", self.img)
        cv.waitKey(0)

service = OCRService(111, "./main/images/two-rate_2.jpg")
service.run()