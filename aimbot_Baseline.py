from time import time, sleep
# from utils.weapon_recoil_pattern import *
# from windowcapture1920x1080 import WindowCapture
# from windowcapture640x640 import WindowCapture
from roboflow import Roboflow
from pynput import keyboard
from datetime import datetime
from ultralytics import YOLO
import ctypes
from PIL import Image
from mss.windows import MSS as mss
import numpy as np
import cv2 as cv
from pynput import keyboard
import ctypes
import sys
import threading 


def get_results():
    with mss() as sct:
        for num, monitor in enumerate(sct.monitors[1:], 1):
            sct_img = sct.grab(monitor)

            original_image = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
            center_x = (original_image.width - 640) // 2
            center_y = (original_image.height - 640) // 2

            # Define the region to extract
            left = center_x
            top = center_y
            right = center_x + 640
            bottom = center_y + 640

            center_region = original_image.crop((left, top, right, bottom))

            results = model(center_region)

            return results

def update_global_variables(results):
    # global move_x, move_y
    try:
        # THIS ONLY TAKES THE FIRS [0] DETECTED CHARACTER - INCLUDE LOGIC TO TAKE IMAGE CLOSEST TO CROSSHAIR
        x_min = results[0].boxes.xyxy[0][0].item()
        y_min = results[0].boxes.xyxy[0][1].item()
        x_max = results[0].boxes.xyxy[0][2].item()
        y_max = results[0].boxes.xyxy[0][3].item()
        confidence = results[0].boxes.conf.item()
        cls = model.names[int(results[0].boxes.cls)]
        
        print(f"RAW BOX COORDINATES:{x_min, y_min, x_max, y_max}")
        print(f'CLASS DETECTED: {cls}')

        print(f"CONFIDENCE: {confidence}")

        x_center = (x_min + x_max) / 2
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

        return move_x , move_y, confidence, cls
    
    except:
        print("NO DETECTION - skipping")
        move_x = 0
        move_y = 0
        confidence = 0
        cls = None

    return move_x, move_y, confidence, cls

# Global variable to track if the Caps Lock key is held down
caps_lock_pressed = False
delete_key_pressed = False

# Function to handle Caps Lock key press event
def on_caps_lock_press(key):
    global caps_lock_pressed
    if key == keyboard.Key.caps_lock:
        caps_lock_pressed = True

# Function to handle Caps Lock key release event
def on_caps_lock_release(key):
    global caps_lock_pressed
    if key == keyboard.Key.caps_lock:
        caps_lock_pressed = False


def caps_lock_listener_thread():
    caps_lock_listener = keyboard.Listener(
        on_press=on_caps_lock_press,
        on_release=on_caps_lock_release
    )
    caps_lock_listener.start()

def stop_aimbot():
    global running
    running = False

# Create threads for listeners
caps_lock_thread = threading.Thread(target=caps_lock_listener_thread)

# Start the listener threads
caps_lock_thread.start()


if __name__ == '__main__':
    # LOCAL MODEL
    print("//// LOADING MODEL ////")
    model = YOLO('models/200923_best_yolov8n.pt')

    running = True

    while running:  # Run the main loop continuously
        if caps_lock_pressed:
            caps_lock_thread.join()
            # Your code here, only executed when Caps Lock is held down
            start_time = time()
            
            # Assuming you have defined get_results() and update_global_variables() functions
            results = get_results()        
            move_x, move_y, confidence, cls = update_global_variables(results)
            
            if cls == 'avatar':
                if confidence >= 0.42:
                    ctypes.windll.user32.mouse_event(0x0001, int(move_x), int(move_y), 0, 0)
                    elapsed_time = time() - start_time
                    sleep(0.01)
                    print(f"ELAPSED TIME: {elapsed_time}")
            else:
                sleep(0.01)

