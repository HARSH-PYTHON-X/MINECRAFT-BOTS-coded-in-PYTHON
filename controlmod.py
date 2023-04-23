from time import sleep
import pyautogui as pg
import pydirectinput as pd

# WALKERS

def walk_w (duration) :
    pd.keyDown('w')
    sleep(duration)
    pd.keyUp('w')

def walk_s (duration) :
    pd.keyDown('s')
    sleep(duration)
    pd.keyUp('s')

def walk_a (duration) :
    pd.keyDown('a')
    sleep(duration)
    pd.keyUp('a')

def walk_d (duration) :
    pd.keyDown('d')
    sleep(duration)
    pd.keyUp('d')

# JUMPERS, CROUCHERS, PLACERS and DESTROYERS

def jump () :
    pd.press('Space')

def crouch (key = 'c') :
    pd.press(key)

def place (key = 'left click') :
    if key == 'left click' :
        pd.leftClick()

    elif key == 'right click' :
        pd.rightClick()

    else :
        pd.press(key)

def destroy (duration = 0.5, key = 'left click') :
    if key == 'left click' :
        pd.leftClick()

    elif key == 'right click' :
        pd.rightClick()

    else :
        pd.keyDown(key)
        sleep(duration)
        pd.keyUp(key)

# EXTRA

def jump_block () :
    jump()
    sleep(0.1)
    place()