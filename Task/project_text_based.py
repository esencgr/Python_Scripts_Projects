import cv2
import os
import numpy as np
import pytesseract
# # -------- resize for easy --------
def re_size(img):        
    h, w, c = img.shape
    img = cv2.resize(img, (w//2, h//2))
    return img

# # -------- optical character recognition --------
def img_to_data(img):
    return pytesseract.image_to_data(img, output_type = pytesseract.Output.DICT)

def img_to_str(img):
    return pytesseract.image_to_string(img, output_type = pytesseract.Output.STRING)

def img_to_list(img):
    list_of_list = list()
    text = img_to_str(img)
    text = text.upper()
    for line in text.splitlines():
        lst = line.split()  
        list_of_list .append(lst)
    return list_of_list

def line_of_finded_word(img, word:str):
    lst = img_to_list(img)
    word = word.upper()
    for line in lst:
        if word in "".join(line).replace("-",""):
            return line

def word_counter(text : str, word : str):
    text = text.upper()
    word = word.upper()
    number_of_word = text.count(word)
    index_of_word = text.find(word)   
    print(f"\nNumber_of_word : {number_of_word} \nIndex of word: {index_of_word}")


if __name__ == "__main__":
    os.environ['DISPLAY'] = ':0'

    # #-------- reading image --------
    img = cv2.imread('/home/cgr/Python/Task/images/page.jpg')
    cv2.imshow("Original Image", img)
    
    # resized_image = re_size(img)
    # res = img_to_data(img)
    # print(res)

    # res = img_to_str(img)
    # print(res)

    # word_counter(res, "item")

    # res = img_to_list(img)
    # print(res)
    #     
    # res = line_of_finded_word(img, "item")
    # print(res)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

