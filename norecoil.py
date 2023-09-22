from pynput import mouse, keyboard
import threading
from time import time, sleep
import pydirectinput
import random
from utils.weapon_recoil_pattern import *
from utils.windowcapture1920x1080 import WindowCapture
from utils.imagedetect import detect_what_weapon

# in game Sensitivity = 1.61

# Global variables  
global detected_weapon
detected_weapon = detect_what_weapon()

wincap = WindowCapture()
mouse_buttons_pressed = set()  # Use a set to track pressed mouse buttons
exit_flag = threading.Event()  # Event to signal the thread to exit
weapon_lock = threading.Lock()

# Function to continuously check mouse buttons and move the cursor down
def move_mouse_down(t):
    global detected_weapon
    # detected_weapon = detect_what_weapon()
    while not exit_flag.is_set():
        if len(mouse_buttons_pressed) == 2: # Check if both left and right buttons are pressed
            if detected_weapon == 'R301':
                print("WEAPON SET TO R301")
                weapon_r301(t)
            if detected_weapon == 'R99': 
                print("WEAPON SET TO R99")
                weapon_r99(t)
            if detected_weapon == 'HAVOC':
                print("WEAPON SET TO HAVOC")
                weapon_havoc(t)
            if detected_weapon == 'FLATLINE':
                print("WEAPON SET TO FLATLINE")
                weapon_flatline(t)
            if detected_weapon == 'ALTERNATOR':
                print("WEAPON SET TO ALTERNATOR")
                weapon_alternator(t)
            if detected_weapon == 'VOLT':
                print("WEAPON SET TO VOLT")
                weapon_volt(t)
            if detected_weapon == 'CAR':
                print("WEAPON SET TO CAR")
                weapon_car(t)
            if detected_weapon == 'DEVOTION':
                print("WEAPON SET TO DEVOTION")
                weapon_devotion(t)
            if detected_weapon == 'LSTAR':
               print("WEAPON SET TO LSTAR")
               weapon_lstar(t)
            if detected_weapon == 'SPITFIRE':
                print("WEAPON SET TO SPITFIRE")
                weapon_spitfire(t)
            if detected_weapon == 'RAMPAGE':
                print("WEAPON SET TO RAMPAGE")
                weapon_rampage(t)
            if detected_weapon == 'RE45':
                print("WEAPON SET TO RE45")
                weapon_re45(t)
        random_time = random.uniform(0.001, 0.005)
        sleep(random_time)  # Add a small delay to prevent excessive loop iterations
    
        # reset timer if one mouse isnot pressed
        if len(mouse_buttons_pressed) < 2:
            t = time()

def on_scroll(x, y, dx, dy):
    global detected_weapon
    thread = threading.Thread(target=update_detected_weapon)
    thread.start()

# Function to handle mouse button press events
def on_click(x, y, button, pressed):
    global mouse_buttons_pressed
    if pressed:
        mouse_buttons_pressed.add(button)
    else:
        mouse_buttons_pressed.discard(button)

# Function to handle keyboard key press events
def on_key_release(key):
    global detected_weapon
    if key == keyboard.Key.delete:
        exit_flag.set()  # Set the exit flag to stop the script
        return False  # Stop the keyboard listener
    try:
        if key.char == '1' or key.char == '2':
            # detected_weapon = detect_what_weapon()
            thread = threading.Thread(target=update_detected_weapon)
            thread.start()
    except AttributeError:
        pass

def update_detected_weapon():
    global detected_weapon  # Reference the global detected_weapon variable

    new_weapon = detect_what_weapon()  # Call the detection function
    with weapon_lock:  # Use a lock to ensure thread safety
        detected_weapon = new_weapon

        
# Create and start the mouse listener thread
mouse_listener = mouse.Listener(on_click=on_click, on_scroll=on_scroll)
mouse_listener.start()

# Create and start the keyboard listener thread
keyboard_listener = keyboard.Listener(on_release=on_key_release)
keyboard_listener.start()

current_time = time()
mouse_movement_thread = threading.Thread(target=move_mouse_down, args=(current_time,))
mouse_movement_thread.start()

# Wait for the keyboard listener thread to finish
keyboard_listener.join()

# Set the exit flag to stop the mouse movement tread
exit_flag.set()

# Wait for the mouse movement thread to finish
mouse_movement_thread.join()

# Stop the mouse listener
mouse_listener.stop()
