# :hotsprings: Apex Legends Aimbot / No Recoil
This project was made to learn and understand computer vision in detail. I started this project when following an intensive AI-bootcamp at @Becode (Belgium). This was not part of the curriculum, but I decided to follow this path pure out of interest. I managed to train a custom model to detect the apex legends characters and write an aimbot and no recoil script based on these detections.

The ***aimbot script*** detects apex legends enemies and moves the mouse automatically towards the head of the enemies. Once the aimbot is activated in the GUI, hold down the shift key to start detecting.

The ***no-recoil script*** detects what weapon is selected, everytime the user changes weapons, this will be detected and a new recoil pattern will be loaded in (to activate the no-recoil both left-click and right-click should be held down)


** :loudspeaker: Important note:** This project has not been tested and should **not** be used on populated (online) servers and will only work on the training grounds of the game.

## :wrench: Installation

Make sure you are using Python3 to execute the application <br>

    pip install -r requirements.txt

This code will start the Graphical User interface where the user can interact with a couple of parameters (confidence + enable / disable aimbot) <br>

    python3 GUI.py

![Alt text](GUI.jpg)

Make sure the Apex Legends application is called 'Apex Legends' (this should be the default application name when launched) <br>
<br>

## Demo
<video src="Apex%20Legends%202023-10-03%2017-42-00.mp4" controls title="Title"></video>