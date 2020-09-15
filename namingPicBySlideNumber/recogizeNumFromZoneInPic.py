# coding=utf-8
"""
Problem: The downloaded pic filename are named by nonsense string, and i need to view this pics by the order which defined by the number in bottom-right corner of every pic.
WhatToDo: recognize the page number and name the files with the page number.
Problem Sample:
    pic filename example:
    chg to:          20-08eStatement_1599540611065.pdf
Base Logic:
    No open pdf file to OpenCV the numbers, the year and month are decided by eStatement file download time which is 'mtime' of the file.
Keyword arguments:
    dir: the directory of the pic files stored
Return: nothing
"""

import os, sys, time
import pytesseract
from PIL import Image, ImageGrab
import psutil


def grab():
    img = ImageGrab.grab([800, 220, 840, 239])
    out = img.resize((80, 38), Image.ANTIALIAS)
    # train for num recognize
    text = pytesseract.image_to_string(out, lang='num')
    return text


def grab2():
    img = ImageGrab.grab([500, 225, 660, 248])
    out = img.resize((348, 55), Image.ANTIALIAS)
    # train for chinese character recognize
    # source db, wait for training
    text = pytesseract.image_to_string(out, lang='chi_sim')
    # replace empty row and space
    new_text = text.replace(' ', '').replace("\n", "")
    return new_text

# for close image which has been showed by Image.show() method
proc_list = []
def get_proc_list():
    global proc_list
    proc_list = []
    proc_list = list( psutil.process_iter() )

def kill_new_proc():
    global proc_list
    for proc in psutil.process_iter():
        if proc not in proc_list:
            if proc.name() == 'Microsoft.Photos.exe':
                proc.kill()


def main():

    dir = r'D:\download\Imageye - __IT______165___________-CSDN__'
    files = os.listdir(dir)

    idx = 1
    for file in files:
        fullpath = os.path.join(dir, file)
        img = Image.open(fullpath)

        get_proc_list()

        img.show()

        imgGrabFullScreen = ImageGrab.grab()
        print(imgGrabFullScreen.size)
        imgGrabFullScreen.save(str(idx).zfill(3) + '_FullScreen_' + '.png')

        # pic resolution: 1080x809
        # Grab Pic Area: top-left: (981, 746); size: (35x19)
        # Grab Screen Area: top-left: (2967, 2007); size: (82x47)
        # top-left: (2854, 1935); size: (78x41)
        imgGrabed = ImageGrab.grab(bbox=(2966, 2006, 2967+84, 2007+49))
        imgGrabed.save(str(idx).zfill(3) + '_GrabedArea_' +  '.png')

        # prepare tesseract env
        pytesseract.pytesseract.tesseract_cmd = r'C:\Users\leiwn\AppData\Local\Tesseract-OCR\tesseract.exe'
        tessdata_dir_config = r'--tessdata-dir "C:\Users\leiwn\AppData\Local\Tesseract-OCR\tessdata"'

        # recognize
        text = pytesseract.image_to_string(imgGrabed, config=tessdata_dir_config)
        print(text)

        kill_new_proc()

        img.close()

        idx += 1
        if idx == 9:
            sys.exit(0)

if __name__ == '__main__':
    main()