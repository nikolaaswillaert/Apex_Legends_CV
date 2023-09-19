import cv2 as cv
from time import sleep, time
import pygetwindow
import pyautogui
from windowcapture1920x1080 import WindowCapture 
import os 


def detect_what_weapon():
    sleep(0.4)
    global detected_weapon
    #window_names = WindowCapture.list_window_names()
    wincap = WindowCapture('Apex Legends')
    screenshot = wincap.get_screenshot()

    weapons = [file for file in os.listdir('templates') if file.lower().endswith('.jpg')]
    
    for weapon in weapons:
        template = cv.imread(f'templates/{weapon}', cv.IMREAD_COLOR)

        method = cv.TM_CCOEFF_NORMED

        h, w, _ = template.shape

        img2 = screenshot.copy()

        result = cv.matchTemplate(img2, template, method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        if max_val > 0.98:
            detected_weapon = str(weapon).split('.jpg')[0]
            print(detected_weapon)
            return detected_weapon
        else:
            print('===============')
            print('not detected')
