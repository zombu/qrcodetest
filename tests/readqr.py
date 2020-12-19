import cv2
import qrcode
from PIL import Image
import numpy as np

detector = cv2.QRCodeDetector()

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, img = cam.read()
    if not ret:
        print("failed to grab img")
        break
    cv2.imshow("test", img)

    #fileName="code.png"
    #cv2.imwrite(fileName, frame)
    #im = cv.imread(fileName)

    data, bbox, _ = detector.detectAndDecode(img)
    if data:
        print("QR Code detected-->", data)    

        # nrOfPoints = len(bbox)
        # for i in range(nrOfPoints):
        #     nextPointIndex = (i+1) % nrOfPoints
        #     cv2.line(image, tuple(bbox[i][0]), tuple(bbox[nextPointIndex][0]), (255,0,0), 5)
        break

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()