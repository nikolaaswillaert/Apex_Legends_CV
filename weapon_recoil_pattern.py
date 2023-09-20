from time import time
import pydirectinput
import random

def weapon_r301(t):
    print(f"TIME: {time()}")
    time_elapsed = time() - t
    print(f"TIME ELAPSED: {time()}")
    if time_elapsed < 0.55:
        random_number_x = random.uniform(-4, -3)
        random_number_y = random.uniform(21,22)
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')
        t = time()

    if 0.55 < time_elapsed <= 0.8:
        random_number_x = random.uniform(-10, -11)
        random_number_y = random.uniform(2,3)
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    if 0.8 < time_elapsed < 1.3:
        random_number_x = random.uniform(13, 14)
        random_number_y = random.uniform(12,11)
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    if time_elapsed >= 1.3:
        random_number_x = random.uniform(-11, -12)
        random_number_y = random.uniform(5,6)
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    print(f'END TIME ELAPSED: {time_elapsed}')
    print(f'TYPE WEAPON: R301')
    pydirectinput.move(int(random_number_x), int(random_number_y), relative=True)

def weapon_r99(t):
    time_elapsed = time() - t
    if time_elapsed < 0.5:
        random_number_x = random.uniform(-5, -4)
        random_number_y = random.uniform(35,36)
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')
    if 0.5 <= time_elapsed <= 0.89:  # Check if 1.5 seconds have passed
        random_number_x = random.uniform(-1, -3)
        random_number_y = random.uniform(25, 30)  # Change the x-axis movement to 8
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')
    if time_elapsed >= 0.89:
        random_number_x = random.uniform(15, 16)
        random_number_y = random.uniform(8,9)
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    print(f'END TIME ELAPSED: {time_elapsed}')
    print(f'TYPE WEAPON: R99')
    pydirectinput.move(int(random_number_x), int(random_number_y), relative=True)


def weapon_havoc(t):
    time_elapsed = time() - t
    if time_elapsed < 0.6:
        random_number_x = 0
        random_number_y = 0
        time_elapsed = 0

    if 0.0 < time_elapsed < 0.25:
        random_number_x = random.uniform(-7, -6)
        random_number_y = random.uniform(25,26)
        print(f'TIME ELAPSED: {time_elapsed}')

    if 0.25 < time_elapsed < 0.90:
        random_number_x = random.uniform(1, 2)
        random_number_y = random.uniform(25,26)
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    if 0.90 < time_elapsed < 1.10:
        random_number_x = random.uniform(-30, -31)
        random_number_y = random.uniform(0,2)
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    if 1.10 < time_elapsed < 1.25:
        random_number_x = random.uniform(5, 6)
        random_number_y = random.uniform(20,21)
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    if 1.25 < time_elapsed < 1.75:
        random_number_x = random.uniform(5,6)
        random_number_y = random.uniform(1,2)
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    if 1.75 < time_elapsed < 2.3:
        random_number_x = random.uniform(1,2)
        random_number_y = random.uniform(15,16)
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    if time_elapsed > 2.3:
        random_number_x = random.uniform(7,8)
        random_number_y = random.uniform(15,16)
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    print(f'TYPE WEAPON: HAVOC')
    print(f'END TIME ELAPSED: {time_elapsed}')
    print(f'TYPE WEAPON: HAVOC')
    pydirectinput.move(int(random_number_x), int(random_number_y), relative=True)

def weapon_flatline(t):
    time_elapsed = time() - t
    if time_elapsed < 0.3:
        random_number_x = random.uniform(1, 3)
        random_number_y = random.uniform(15,16)
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    if 0.3 < time_elapsed < 0.75:
        random_number_x = random.uniform(8,9)
        random_number_y = random.uniform(15,16)
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    if 0.75 <= time_elapsed < 1.1:  # Check if 1.5 seconds have passed
        random_number_x = random.uniform(-15,-16)
        random_number_y = random.uniform(0,0)  # Change the x-axis movement to 8
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    if 1.1 <= time_elapsed < 1.3:  # Check if 1.5 seconds have passed
        random_number_x = random.uniform(1,2)
        random_number_y = random.uniform(15,16)  # Change the x-axis movement to 8
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    if 1.3 <= time_elapsed < 1.6:
        random_number_x = random.uniform(19,20)
        random_number_y = random.uniform(5,6)  # Change the x-axis movement to 8
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')
    
    if 1.6 <= time_elapsed < 1.85:
        random_number_x = random.uniform(1,2)
        random_number_y = random.uniform(15,16)  # Change the x-axis movement to 8
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    if 1.85 <= time_elapsed < 2.1:
        random_number_x = random.uniform(20,21)
        random_number_y = random.uniform(7,8)  # Change the x-axis movement to 8
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    if time_elapsed >= 2.1:
        random_number_x = random.uniform(-15,-16)
        random_number_y = random.uniform(7,8)  # Change the x-axis movement to 8
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    print(f'END TIME ELAPSED: {time_elapsed}')
    print(f'TYPE WEAPON: FLATLINE')
    pydirectinput.move(int(random_number_x), int(random_number_y), relative=True)

def weapon_alternator(t):
    time_elapsed = time() - t
    if time_elapsed <= 0.40:
        random_number_x = random.uniform(3, 2)
        random_number_y = random.uniform(25,26)
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    if 0.40 < time_elapsed <= 0.85:
        random_number_x = random.uniform(-3, -2)
        random_number_y = random.uniform(23,24)
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    if 0.85 < time_elapsed <= 1.4:
        random_number_x = random.uniform(-5, -6)
        random_number_y = random.uniform(13,14)
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    if 1.4 < time_elapsed <= 1.6:
        random_number_x = random.uniform(7, 8)
        random_number_y = random.uniform(12,13)
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    if 1.6 < time_elapsed:
        random_number_x = random.uniform(7, 8)
        random_number_y = random.uniform(8,9)
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    print(f'END TIME ELAPSED: {time_elapsed}')
    print(f'TYPE WEAPON: ALTERNATOR')
    pydirectinput.move(int(random_number_x), int(random_number_y), relative=True)

def weapon_volt(t):
    time_elapsed = time() - t
    if time_elapsed <= 0.80:
        random_number_x = random.uniform(-5, -6)
        random_number_y = random.uniform(29,30)
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    if 0.80 < time_elapsed <= 1.30:
        random_number_x = random.uniform(10, 12)
        random_number_y = random.uniform(9,8)
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    if 1.30 < time_elapsed <= 1.40:
        random_number_x = random.uniform(-10, -11)
        random_number_y = random.uniform(2,3)
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    if 1.40 < time_elapsed <= 1.60:
        random_number_x = random.uniform(10, 11)
        random_number_y = random.uniform(8,9)
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    if time_elapsed > 1.60:
        random_number_x = random.uniform(1, 2)
        random_number_y = random.uniform(2,3)
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    print(f'END TIME ELAPSED: {time_elapsed}')
    print(f'TYPE WEAPON: VOLT')
    pydirectinput.move(int(random_number_x), int(random_number_y), relative=True)

def weapon_car(t):
    time_elapsed = time() - t
    if time_elapsed <= 0.50:
        random_number_x = random.uniform(7, 8)
        random_number_y = random.uniform(33,34)
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')
    
    if 0.50 < time_elapsed <= 0.75:
        random_number_x = -3
        random_number_y = 33
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')
    
    if 0.75 < time_elapsed <= 0.88:
        random_number_x = -19
        random_number_y = 2
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    if 0.88 < time_elapsed <= 1.0:
        random_number_x = 0
        random_number_y = 11
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    if 1.0 < time_elapsed:
        random_number_x = 0
        random_number_y = 8
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')
    
    print(f'END TIME ELAPSED: {time_elapsed}')
    print(f'TYPE WEAPON: C.A.R.')
    pydirectinput.move(int(random_number_x), int(random_number_y), relative=True)

def weapon_devotion(t):
    time_elapsed = time() - t
    if time_elapsed <= 0.75:
        random_number_x = 2
        random_number_y = 42
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    if 0.75 < time_elapsed <= 1.1:
        random_number_x = 22
        random_number_y = 20
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')
    
    if 1.1 < time_elapsed <= 1.3:
        random_number_x = 9
        random_number_y = 0
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')
    
    if 1.3 < time_elapsed <= 1.6:
        random_number_x = 0
        random_number_y = 9
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')
    
    if 1.6 < time_elapsed <= 1.9:
        random_number_x = -15
        random_number_y = 15
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    print(f'END TIME ELAPSED: {time_elapsed}')
    print(f'TYPE WEAPON: DEVOTION')
    pydirectinput.move(int(random_number_x), int(random_number_y), relative=True)

def weapon_lstar(t):
    time_elapsed = time() - t
    if time_elapsed <= 0.3:
        random_number_x = 19
        random_number_y = 15
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')
    
    if 0.3 < time_elapsed <= 1.0:
        random_number_x = -6
        random_number_y = 26
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')
    
    if 1.0 < time_elapsed:
        random_number_x = -3
        random_number_y = 19
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')
    
    print(f'END TIME ELAPSED: {time_elapsed}')
    print(f'TYPE WEAPON: LSTAR')
    pydirectinput.move(int(random_number_x), int(random_number_y), relative=True)

def weapon_spitfire(t):
    time_elapsed = time() - t
    if time_elapsed <= 0.7:
        random_number_x = 3
        random_number_y = 13
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')
    
    if 0.7 < time_elapsed <= 0.9:
        random_number_x = -5
        random_number_y = -2
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    if 0.9 < time_elapsed <= 1.2:
        random_number_x = -1
        random_number_y = 5
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')
    
    if 1.2 < time_elapsed <= 1.4:
        random_number_x = -1
        random_number_y = 5
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')
    
    if 1.4 < time_elapsed <= 1.6:
        random_number_x = 13
        random_number_y = 9
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    if 1.6 < time_elapsed <= 2.0:
        random_number_x = 3
        random_number_y = 6
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    if 2.0 < time_elapsed <= 2.2:
        random_number_x = 5
        random_number_y = 6
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')
    
    if 2.2 < time_elapsed <= 3.6:
        random_number_x = -4
        random_number_y = 3
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')
    
    if 3.6 < time_elapsed <= 5:
        random_number_x = 4
        random_number_y = 5
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')
    
    if 5.0 < time_elapsed:
        random_number_x = -4
        random_number_y = 5
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    print(f'END TIME ELAPSED: {time_elapsed}')
    print(f'TYPE WEAPON: SPITFIRE')
    pydirectinput.move(int(random_number_x), int(random_number_y), relative=True)

def weapon_rampage(t):
    time_elapsed = time() - t
    print(time_elapsed)
    if time_elapsed <= 0.2:
        random_number_x = -1
        random_number_y = 13
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    if 0.2 < time_elapsed <= 0.4:
        random_number_x = 8
        random_number_y = 11
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    if 0.4 < time_elapsed <= 0.6:
        random_number_x = -5
        random_number_y = 11
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')
    
    if 0.6 < time_elapsed <= 1.8:
        random_number_x = -4
        random_number_y = 10
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')
    
    if 1.8 < time_elapsed <= 2.6:
        random_number_x = 7
        random_number_y = 5
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')
    
    if 2.6 < time_elapsed <= 5.2:
        random_number_x = 1
        random_number_y = 4
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')
    
    if 5.2 < time_elapsed:
        random_number_x = 1
        random_number_y = 8
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    print(f'END TIME ELAPSED: {time_elapsed}')
    print(f'TYPE WEAPON: RAMPAGE')
    pydirectinput.move(int(random_number_x), int(random_number_y), relative=True)

def weapon_re45(t):
    time_elapsed = time() - t
    if time_elapsed <= 0.2:
        random_number_x = -6
        random_number_y = 26
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')
    
    if 0.2 < time_elapsed <= 0.4:
        random_number_x = -9
        random_number_y = 26
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')
    
    if 0.4 < time_elapsed <= 0.8:
        random_number_x = -19
        random_number_y = 15
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    if 0.8 < time_elapsed <= 1.2:
        random_number_x = -5
        random_number_y = 17
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')
    
    if 1.2 < time_elapsed:
        random_number_x = -9
        random_number_y = 10
        print(f'TIME ELAPSED: {time_elapsed}')
        print(f'RANDO X, Y: {random_number_x, random_number_y}')

    print(f'END TIME ELAPSED: {time_elapsed}')
    print(f'TYPE WEAPON: RE45')
    pydirectinput.move(int(random_number_x), int(random_number_y), relative=True)