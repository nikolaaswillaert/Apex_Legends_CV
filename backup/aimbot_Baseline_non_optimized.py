from time import time, sleep
import cv2 as cv
from utils.weapon_recoil_pattern import *
# from windowcapture1920x1080 import WindowCapture
from utils.windowcapture640x640 import WindowCapture
from roboflow import Roboflow
import pydirectinput
import pyautogui
import numpy as np
import torch
import datetime
from pynput import keyboard, mouse
import sys
import threading

# get screenshot
wincap = WindowCapture('Apex Legends')

# LOCAL MODEL
model = torch.hub.load('C:/Users/User/Desktop/python/no_recoil_apex/yolov5workspace/yolov5','custom', path='C:/Users/User/Desktop/python/no_recoil_apex/no_recoil_apex/models/best640x640.pt', force_reload=True,source='local')

running = True

def get_results():
    screenshot = wincap.get_screenshot()
    img2 = screenshot.copy()
    results = model(img2)
    return results

def update_global_variables(results):
    global move_x, move_y
    try:
        x_min = results.xyxy[0][0][0].item()
        x_max = results.xyxy[0][0][2].item()
        y_min = results.xyxy[0][0][1].item()
        y_max = results.xyxy[0][0][3].item()
        confidence = results.xyxy[0][0][4].item()
        print(x_min, y_min, x_max, y_max)
        print(f"CONFIDENCE: {confidence}")

        x_center = (x_min + x_max) / 2
        # y_center = (y_min + y_max) / 2w
        y_center = y_min + 0.2 * (y_max - y_min)
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

    except IndexError:
        print("NO DETECTION - skipping")
        move_x = 0
        move_y = 0
        confidence = 0

    return move_x, move_y, confidence


def on_delete_key_press(key):
    global running
    if key == keyboard.Key.delete:
        print("Delete key pressed. Stopping threads.")
        running = False
        return False

delete_listener = keyboard.Listener(on_press=on_delete_key_press)
delete_listener.start()


while running:
    results = get_results()
    move_x, move_y, confidence = update_global_variables(results)
    if confidence >= 0.85:
        print(f"GLOBAL VARIABLES: {move_x}, {move_y}")

        pydirectinput.move(int(move_x), int(move_y), relative=True)
        sleep(0.1)

delete_listener.stop()