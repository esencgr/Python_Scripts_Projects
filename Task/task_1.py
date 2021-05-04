import cv2
import os
import pytesseract
import time
# os.environ['DISPLAY'] = ':0'

for i in range(1,7):
    img = cv2.imread('/home/cgr/PYTHON/Task/images/page' + str(i) + '.ppm')
    # cv2.imshow('img', img)

    text = pytesseract.image_to_string(img, output_type = pytesseract.Output.STRING)
    print(text)
    # d = pytesseract.image_to_data(img, output_type = pytesseract.Output.DICT)

    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(d['conf'][i]) > 60:
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    img_rect = cv2.imwrite("/home/cgr/PYTHON/Task/page5_rect.jpg",img)


# d = pytesseract.image_to_data(img, output_type = pytesseract.Output.DICT)
# # print(d.keys())
# n_boxes = len(d['text'])

# for i in range(n_boxes):
#     find_word = str(d['text'][i].upper().replace('-', ''))
#     if  "invoice".upper() in find_word:
#         # (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#         (x, y, w, h) = (0, d['top'][i]-5, img.shape[1], d['height'][i]+5)
#         # print(x,y,w,h)
#         img_rect = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#         img_crop = img_rect [y : y + h, x : x + w ]
#         cv2.imshow('cropped', img_crop)


# img_rect_wr = cv2.imwrite("/home/cgr/PYTHON/Task/images/page5_rect.jpg",img_rect)
# img_crop_wr = cv2.imwrite("/home/cgr/PYTHON/Task/images/page5_crop.jpg",img_crop)
# extract = pytesseract.image_to_string(img_crop, output_type= pytesseract.Output.DICT)
# print(extract)


    # number_of_invoice = text.count("INVOICE")
    # number_of_subtotal = text.count("SUBTOTAL")
    # index_of_invoice = text.find("INVOICE")
    # index_of_subtotal = text.find("SUBTOTAL")
    
    # print(f"PAGE-{i}")
    # print(f"Number of invoice : {number_of_invoice} \nIndex of invoice: {index_of_invoice}")
    # print(f"\nNumber_of_subtotal : {number_of_subtotal} \nIndex of subtotal: {index_of_subtotal}")
    # print("-" * 20)

    # time.sleep(1)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
