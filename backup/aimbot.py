from time import time, sleep
import cv2 as cv
from weapon_recoil_pattern import *
# from windowcapture1920x1080 import WindowCapture
from windowcapture640x640 import WindowCapture
from roboflow import Roboflow
import pydirectinput
import pyautogui
import numpy as np
import torch
import datetime
from pynput import mouse, keyboard
import sys
import threading

# get screenshot
wincap = WindowCapture('Apex Legends')

# current_datetime = datetime.datetime.now()
# formatted_datetime = current_datetime.strftime('%Y%m%d%H%M%S')
# cv.imwrite(f'img_{formatted_datetime}.jpg', img2)

# LOCAL MODEL
model = torch.hub.load('C:/Users/User/Desktop/python/no_recoil_apex/yolov5workspace/yolov5','custom', path='C:/Users/User/Desktop/python/no_recoil_apex/no_recoil_apex/640x640.pt', force_reload=True,source='local')

def get_xy_fullimage():
    screenshot = wincap.get_screenshot()
    img2 = screenshot.copy()
    results = model(img2)
    # results.show()
    results.print()
    # xmin    ymin    xmax   ymax  confidence  class    name
    try:
        x_min = results.xyxy[0][0][0].item()
        x_max = results.xyxy[0][0][2].item()
        y_min = results.xyxy[0][0][1].item()
        y_max = results.xyxy[0][0][3].item()
        confidence = results.xyxy[0][0][4].item()
        print(x_min, y_min, x_max, y_max)

        x_center = (x_min + x_max) / 2
        y_center = (y_min + y_max) / 2
        box_center = (x_center, y_center)
        print(f"Center of box coordinates on 640 x 640 image:{box_center}")
            # Calculate scaling factors
        scale_x = 1920 / 640
        scale_y = 1080 / 640

        # Translate to coordinates on the 1920x1080 image
        x_center_1920x1080 = x_center * scale_x
        y_center_1920x1080 = y_center * scale_y

        move_x = (x_center_1920x1080 - 960) / 1.61
        move_y = (y_center_1920x1080 - 540) / 1.61

        return move_x, move_y

    except IndexError:
        print("NO DETECTION - skipping")
        x_center = 0
        y_center = 0
        return x_center, y_center
    
def keyboard_check():
    while True:
        if keyboard.is_pressed('shift'):
            move_x, move_y = get_xy_fullimage()
            pydirectinput.move(int(move_x), int(move_y), relative=True)
            sleep(0.1)
        elif keyboard.is_pressed('delete'):
            sys.exit()
