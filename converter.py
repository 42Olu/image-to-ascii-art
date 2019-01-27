from PIL import Image
import sys
import numpy as np
import random

'''
constants
'''
max_size = (128, 128)


def convert(pixel_val):
    pixel_val = 255 - pixel_val

    char_list = [(".", "'", "´", ","), (":", ";", '"', "-", "~", "_"), ("<", ">", "+", "*", "i", "/", "\\", "(", ")"),
                 ("o", "a", "e", "5", "p", "d"), ("&", "%", "#", "§", "8", "ß")]

    if(pixel_val < 10):
        return " "
    else:
        idx = pixel_val//(int((255-10)/len(char_list)))
        if idx > len(char_list) - 1:
            idx = len(char_list) - 1
        return random.choice(char_list[idx])

def convert_row(row):
    ascii_row = ""
    for i in range(row.shape[0]):
        ascii_row += convert(row[i])

    return ascii_row


if __name__== '__main__':
    if(len(sys.argv) == 2):
        [_,image_path]=sys.argv
        resolution = None
    else:
        [_,image_path, resolution]=sys.argv
        resolution = float(resolution)


    img = Image.open(image_path)
    size = img.size

    if(not resolution is None):
        resolution = resolution/100
        max_size = (int(size[0]*resolution), int(size[1]*resolution))


    resize_ratio = min(max_size[0]/size[0], max_size[1]/size[1])
    img = img.resize((int(size[0]*resize_ratio * 1.37), int(size[1]*resize_ratio*0.63)))

    img = img.convert("L")
    arr = np.array(img)

    with open('ascii_art.txt', 'w') as f:
        for i in range(arr.shape[0]):
            row = convert_row(arr[i, :])
            f.write(row + '\n')