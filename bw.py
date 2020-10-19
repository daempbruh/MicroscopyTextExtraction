import os
import cv2
import glob
from pathlib import Path

for filepath in glob.iglob('C:/Users/Yao Quan/Documents/Python Venv/Photos/*.jpg'):
    image = cv2.imread(filepath)
    image = cv2.resize(image, (720, 540))
    crop_image = image[0:500, 0:720]  # Cropping parameters tweaked to exclude legends

    i = 30
    while i < 255:
        threshed_image = cv2.adaptiveThreshold(cv2.cvtColor(crop_image,cv2.COLOR_BGR2GRAY), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,3,1)
        # ret, threshed_image = cv2.threshold(cv2.cvtColor(crop_image, cv2.COLOR_BGR2GRAY), i, 255, cv2.THRESH_BINARY_INV)
        i = i + 1
        count = cv2.countNonZero(threshed_image)
        if count > 40000:
            print (count, i)
            cv2.imshow("contours", threshed_image)
            output_path = ('C:/Users/Yao Quan/Documents/Python Venv/bwPhotos')
            cv2.imwrite(os.path.join(output_path, 'bw_'+ Path(filepath).stem + '.jpg'), threshed_image)
            break



