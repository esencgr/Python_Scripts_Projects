import cv2
import os
import numpy as np
import pytesseract

os.environ['DISPLAY'] = ':0'


def rectangle_all_word (img):
    d 
# -------- reading image --------
img = cv2.imread('/home/cgr/PYTHON/Task/images/ocr.png')

d = pytesseract.image_to_data(img, output_type = pytesseract.Output.DICT)
# print(d.keys())

n_boxes = len(d['text'])

for i in range(n_boxes):
    if  int(d["conf"][i]) > 90:
        # find_word = str(d['text'][i].upper().replace('-', ''))
        # if  "subtotal".upper() in find_word:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        # (x, y, w, h) = (0, d['top'][i]-3, img.shape[1], d['height'][i]+3)
        img_rect = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # img_crop = img_rect [y : y + h, x : x + w ]
        # cv2.imshow('cropped', img_crop)
        # extract = pytesseract.image_to_string(img_crop)
        # print(extract)
    
cv2.imshow('rect', img_rect)

# img_rect_wr = cv2.imwrite("/home/cgr/PYTHON/Task/images/page5_rect.jpg",img_rect)
# img_crop_wr = cv2.imwrite("/home/cgr/PYTHON/Task/images/page5_crop.jpg",img_crop)

# for window
cv2.waitKey(0)
cv2.destroyAllWindows()
