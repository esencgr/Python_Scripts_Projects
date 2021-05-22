from PIL import Image 
import os
import pytesseract
import re

def img_to_str(img):
    return pytesseract.image_to_string(img, output_type = pytesseract.Output.STRING)

if __name__ == "__main__":
    os.environ['DISPLAY'] = ':0'   
    # creating a object 
    img = Image.open("/home/cgr/Python_Scripts_Projects/Task/images/ocr.png") 
    img.show()

    # text_data = pytesseract.image_to_string(img.convert('RGB'), lang='eng')
    text_data = img_to_str(img)
    print(text_data)

