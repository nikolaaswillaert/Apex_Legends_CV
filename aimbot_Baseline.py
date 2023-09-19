from time import time, sleep
from weapon_recoil_pattern import *
# from windowcapture1920x1080 import WindowCapture
from windowcapture640x640 import WindowCapture
from roboflow import Roboflow
from pynput import keyboard
from datetime import datetime
from ultralytics import YOLO
import ctypes


# get screenshot
wincap = WindowCapture('Apex Legends')

# LOCAL MODEL
# model = torch.hub.load('C:/Users/User/Desktop/python/no_recoil_apex/yolov5workspace/yolov5','custom', path='C:/Users/User/Desktop/python/no_recoil_apex/no_recoil_apex/models/best640x640.pt', force_reload=True,source='local')
print("//// LOADING MODEL ////")
model = YOLO('models/yolov8n_best.pt')

running = True


def get_results():
    screenshot = wincap.get_screenshot()
    # img2 = screenshot.copy()
    # cv.imwrite(f'{datetime.now()}.jpg', img2)
    results = model(screenshot)
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
        print(f"RAW BOX COORDINATES:{x_min, y_min, x_max, y_max}")

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

        return move_x , move_y, confidence
    
    except:
        print("NO DETECTION - skipping")
        move_x = 0
        move_y = 0
        confidence = 0

    return move_x, move_y, confidence

def on_delete_key(key):
    global running
    if key == keyboard.Key.delete:
        print("Delete key pressed. Stopping Script.")
        running = False
        return False

# # Start the delete key listener thread
delete_listener = keyboard.Listener(on_press=on_delete_key)
delete_listener.start()

while running:
    start_time = time()
    # TIMING: GET RESULTS TAKES ABOUT 0.16 - 0.20 seconds
    results = get_results()
    
    # TIMING: 0.001 seconds update global variables
    move_x , move_y, confidence = update_global_variables(results)  

    if confidence >= 0.83:
    # TIMING: Pydirecinput takes about 0.10 - 0.11 seconds
        # pydirectinput.move(int(move_x), int(move_y), relative=True)
        ctypes.windll.user32.mouse_event(0x0001, int(move_x),int(move_y),0,0)
        sleep(0.001)

        elapsed_time = time() - start_time
        print(f"ELAPSED TIME: {elapsed_time}")


# Stop the delete key listener thread
delete_listener.stop()
