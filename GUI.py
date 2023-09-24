import customtkinter as ctk
import subprocess
import tkinter as tk
import threading

global detection_value
detection_value = 0.49

def start_ab_script():
    global ab_script_process
    global detection_value
    ab_script_process = subprocess.Popen(['.venv/Scripts/python', 'aimbot_Baseline.py', f'{detection_value}'])

# Function to stop the script
def stop_ab_script():
    global ab_script_process
    print('Stopping Aimbot Script')
    if ab_script_process and ab_script_process.poll() is None:
        ab_script_process.terminate()
        ab_script_process.wait()
    
    def tst_end():
        print('END')

def start_nr_script():
    global nr_script_process, nr_output_text
    nr_script_process = subprocess.Popen(['.venv/Scripts/python', 'norecoil.py'])

def stop_nr_script():
    global nr_script_process
    print('Stopping No-recoil Script')
    if nr_script_process and nr_script_process.poll() is None:
        nr_script_process.terminate()
        nr_script_process.wait()

def slider_event(self):
    global detection_value
    detection_value = round(slider.get(),2)
    current_value_label.configure(text=f"Object Detection Parameter: {slider.get():.2f}")

window = ctk.CTk()
window.title('APEX SCRIPT HUB')
window.geometry('700x650')

ctk.set_appearance_mode('dark')

label_ab = ctk.CTkLabel(window, 
                     text='Aimbot', 
                     width=300, 
                     fg_color='#69666A', 
                     text_color='#000000', 
                     font=('Arial', 20),
                     corner_radius=40)

label_nr = ctk.CTkLabel(window, 
                     text='No Recoil', 
                     width=300, 
                     fg_color='#69666A', 
                     text_color='#000000', 
                     font=('Arial', 20),
                     corner_radius=40)

ab_on_button = ctk.CTkButton(window, 
                       text='Aimbot ON',
                       fg_color='#D488ED',
                       text_color='#550F0F',
                       hover_color='#7201F7',
                       corner_radius=40,
                       command=start_ab_script,
                       )

ab_off_button = ctk.CTkButton(window, 
                       text='Aimbot OFF',
                       fg_color='#D488ED',
                       text_color='#550F0F',
                       hover_color='#7201F7',
                       corner_radius=40,
                       command=stop_ab_script)

nr_on_button = ctk.CTkButton(window, 
                       text='No-Recoil ON',
                       fg_color='#A8CFB1',
                       text_color='#0D2A02',
                       hover_color='#125421',
                       corner_radius=40,
                       command=start_nr_script)

nr_off_button = ctk.CTkButton(window, 
                       text='No-Recoil OFF',
                       fg_color='#A8CFB1',
                       text_color='#0D2A02',
                       hover_color='#125421',
                       corner_radius=40,
                       command=stop_nr_script)

slider = ctk.CTkSlider(master=window, from_=0.0, to=0.99, command=slider_event)


current_value_label = ctk.CTkLabel(window, text=f"Object Detection Parameter: {slider.get():.2f}")

# Use grid to arrange elements
label_ab.grid(row=0, column=0, padx=20, pady=20, columnspan=2)
ab_on_button.grid(row=1, column=0, padx=20, pady=10)
ab_off_button.grid(row=1, column=1, padx=20, pady=5)

label_nr.grid(row=0, column=2, padx=20, pady=20, columnspan=2)
nr_on_button.grid(row=1, column=2, padx=20, pady=10)
nr_off_button.grid(row=1, column=3, padx=20, pady=5)

#SLIDER AND VALUES
slider.grid(row=2, column=0, padx=20, pady=20, columnspan=2)
current_value_label.grid(row=3, column=0, columnspan=2)

window.mainloop()
