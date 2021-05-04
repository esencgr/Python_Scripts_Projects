import cv2
import os
import numpy as np
import pytesseract

# # -------- resize for easy --------
def re_size(img):        
    h, w, c = img.shape
    scale_percent = 40 # percent of original size
    width = int(w * scale_percent / 100)
    height = int(h * scale_percent / 100)
    dim = (width, height)
    img = cv2.resize(img, dim)
    return img

# # -------- optical character recognition --------
def img_to_string_data(img):
    return pytesseract.image_to_data(img, output_type = pytesseract.Output.STRING)

def img_to_dict_data(img):
    return pytesseract.image_to_data(img, output_type = pytesseract.Output.DICT)

def img_to_str(img):
    return pytesseract.image_to_string(img, output_type = pytesseract.Output.STRING)

def rectangle_each_word(img):
    d = img_to_dict_data(img)
    # # print(d.keys())
    n_boxes = len(d['text'])

    for i in range(n_boxes):
        if  int(d["conf"][i]) > 60:
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            img_rect = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    return img_rect

# def print_all_rectangle_each_word(img):
#     d = img_to_dict_data(img)
#     # n_boxes = len(d['text'])
#     # word = word.upper().replace("-","")
#     print(d['line_num'])
#     lines = d['line_num']
#     for line in lines:
#         if  line == 0:
#             print(d['text'][line])

#     # for i in d['text']:
#     #     print(i)

if __name__ == "__main__":
    os.environ['DISPLAY'] = ':0'

    # #-------- reading image --------
    img = cv2.imread('/home/cgr/PYTHON/Task/images/img.png')
    cv2.imshow("Original Image", img)
    
    # res = img_to_string_data(img)
    # print(res)

    res = img_to_dict_data(img)
    print(res)

    for value in res.values():
        print(value)
        print()

    # res = img_to_str(img)
    # print(res)

    # res = img_to_list(img)
    # print(res)

    # res = line_of_finded_word(img, "invoice")
    # print(res)

    # res = rectangle_each_word(img)
    # cv2.imshow("rect",res)

    # res = print_all_rectangle_each_word(img)
    # print(res)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()



# d = pytesseract.image_to_data(img, output_type = pytesseract.Output.DICT)
# # print(d.keys())
# n_boxes = len(d['text'])

# for i in range(n_boxes):
#     find_word = str(d['text'][i].upper().replace('-', ''))
#     if  "invoice".upper() in find_word:
#         (x, y, w, h) = (0, d['top'][i]-5, img.shape[1], d['height'][i]+5)
#         # print(x,y,w,h)
#         img_rect = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#         img_crop = img_rect [y : y + h, x : x + w ]
#         cv2.imshow('cropped', img_crop)


# img_rect_wr = cv2.imwrite("/home/cgr/PYTHON/Task/images/page5_rect.jpg",img_rect)
# img_crop_wr = cv2.imwrite("/home/cgr/PYTHON/Task/images/page5_crop.jpg",img_crop)

# ------------------------------------------------------------
# for i in range(n_boxes):
#     if  int(d["conf"][i]) > 90:
#         # find_word = str(d['text'][i].upper().replace('-', ''))
#
    
# cv2.imshow('rect', img_rect)         # if  "subtotal".upper() in find_word:
#         (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#         # (x, y, w, h) = (0, d['top'][i]-3, img.shape[1], d['height'][i]+3)
#         img_rect = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#         # img_crop = img_rect [y : y + h, x : x + w ]
#         # cv2.imshow('cropped', img_crop)
#         # extract = pytesseract.image_to_string(img_crop)
#         # print(extract)




    # for i in range(n_boxes):
    #     print(d['text'][i])
        # if  word in find_word:
        #     (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        #     # (x, y, w, h) = (0, d['top'][i]-3, img.shape[1], d['height'][i]+3)
        #     img_rect = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # # img_crop = img_rect [y : y + h, x : x + w ]
        # # cv2.imshow('cropped', img_crop)
        # # extract = pytesseract.image_to_string(img_crop)
        # # print(extract)
