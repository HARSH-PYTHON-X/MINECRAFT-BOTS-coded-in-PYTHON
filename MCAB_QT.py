from time import sleep
from tkinter import *
from tkinter.ttk import Combobox

import pyautogui as pg
import pydirectinput as pd
import keyboard
import controlmod as cd

import pyttsx3
import speech_recognition as sr
import webbrowser
import subprocess

# MAIN WINDOW

window = Tk()
window.title('// DYNAMIX - CYBERDEX // MCAB - BOT // MENU')

# MAIN BUTTONS AND WIDGET

label_1 = Label(text = 'TASK FOR BOT >')
label_1.pack()

task_for_bot_input = Combobox(values = ['build wall', 'build pillar', 'autoclicker key', 'strip mine'])
task_for_bot_input.pack()

# MORE DEFINITONS

# BUILD WALL INITIATIVE

def build_wall_initiative () :
    label_2 = Label(window, text = 'wall length >')
    label_2.pack()

    length_of_wall_input = Entry(window)
    length_of_wall_input.pack()

    label_3 = Label(window, text = 'height of wall >')
    label_3.pack()

    height_of_wall_input = Entry(window)
    height_of_wall_input.pack()

    label_4 = Label(window, text = 'inventory slot for blocks >')
    label_4.pack()

    inventory_slot_for_blocks_input_1 = Entry(window)
    inventory_slot_for_blocks_input_1.pack()

    label_5 = Label(window, text = 'inventory slot for blocks >')
    label_5.pack()

    inventory_slot_for_blocks_input_2 = Entry(window)
    inventory_slot_for_blocks_input_2.pack()

    def run_build_wall () :
        wall_length = int(length_of_wall_input.get())
        wall_height = int(height_of_wall_input.get())

        inventory_slot_for_blocks_1 = inventory_slot_for_blocks_input_1.get()
        inventory_slot_for_blocks_2 = inventory_slot_for_blocks_input_2.get()

        print('starting wall building in 5 seconds ...')
        sleep(5)
        print(f'wall building started for length [{wall_length} blocks] and height [{wall_height} blocks]...')

        pd.press(inventory_slot_for_blocks_1)        

        for wall_pillars in range (wall_length) :
            for wall_pillars_height in range (wall_height) :
                cd.jump()
                sleep(0.1)
                cd.place()
            cd.walk_w(0.5)
            sleep(0.5)
            cd.walk_s(1)
            print(f'{wall_pillars} pillars completed ...')
        print('wall successfully builded ...')

    build_wall_btn = Button(window, text = 'BUILD WALL', fg = 'green', command = run_build_wall)
    build_wall_btn.pack()

# BUILD PILLAR INITIATIVE

def build_pillar_initiative () :
    label_6 = Label(window, text = 'height of pillar >')
    label_6.pack()

    height_of_pillar_input = Entry(window)
    height_of_pillar_input.pack()

    label_7 = Label(window, text = 'inventory slot for blocks >')
    label_7.pack()

    inventory_slot_for_blocks_1_input = Entry(window)
    inventory_slot_for_blocks_1_input.pack()

    label_8 = Label(window, text = 'inventory slot for blocks >')
    label_8.pack()

    inventory_slot_for_blocks_2_input = Entry(window)
    inventory_slot_for_blocks_2_input.pack()

    def run_build_pillar () :
        height_of_pillar = int(height_of_pillar_input.get())

        inventory_slot_for_blocks_1 = inventory_slot_for_blocks_1_input.get()
        inventory_slot_for_blocks_2 = inventory_slot_for_blocks_2_input.get()

        print('starting building pillar in 5 seconds ...')
        sleep(5)
        print(f'building pillar for height [{height_of_pillar} blocks] ...')

        pd.press(inventory_slot_for_blocks_1)

        for x in range (height_of_pillar) :
            cd.jump()
            sleep(0.1)
            cd.place()
            print(f'blocks used > {x}')
        print('pillar successfully builded ...')

    build_pillar_btn = Button(window, text = 'BUILD PILLAR', fg = 'green', command = run_build_pillar)
    build_pillar_btn.pack()

# AUTOCLICKER KEY INITIATIVE

def auto_clicker_key_initiative () :
    label_9 = Label(window, text = 'key to autoclick >')
    label_9.pack()

    key_to_autoclick_input = Combobox(window, values = ['left mouse', 'right mouse'])
    key_to_autoclick_input.pack()

    label_11 = Label(window, text = 'key to start autoclicking >')
    label_11.pack()

    key_to_start_autoclicking_input = Entry(window)
    key_to_start_autoclicking_input.pack()

    label_10 = Label(window, text = 'key to invoke >')
    label_10.pack()

    key_to_invoke_input = Entry(window)
    key_to_invoke_input.pack()

    def run_autoclick_key () :
        key_to_autoclick = str(key_to_autoclick_input.get())
        key_to_invoke = str(key_to_invoke_input.get())

        key_to_start_autoclicking = str(key_to_start_autoclicking_input.get())

        if key_to_autoclick == 'left mouse' :
            while True :
                if keyboard.is_pressed(key_to_start_autoclicking) :
                    pd.leftClick()

                elif keyboard.is_pressed(key_to_invoke) :
                    break

        elif key_to_autoclick == 'right mouse' :
            while True :
                if keyboard.is_pressed(key_to_start_autoclicking) :
                    pd.rightClick()

                elif keyboard.is_pressed(key_to_invoke) :
                    break

        else :
            while True :
                if keyboard.is_pressed(key_to_start_autoclicking) :
                    pd.keyDown(key_to_autoclick)

                elif keyboard.is_pressed(key_to_invoke) :
                    break

                else :
                    pd.keyUp(key_to_autoclick)

    run_autoclick_btn = Button(window, text = 'RUN KEY AUTOCLICKER', fg = 'green', command = run_autoclick_key)
    run_autoclick_btn.pack()
 
# STRIP MINE INITIATIVE

def strip_mine_initiative () :
    label_12 = Label(window, text = 'key to mine >')
    label_12.pack()

    key_to_mine_input = Combobox(window, values = ['left mouse', 'right mouse'])
    key_to_mine_input.pack()

    label_13 = Label(window, text = 'length of strip mine >')
    label_13.pack()

    length_of_strip_mine_input = Entry(window)
    length_of_strip_mine_input.pack()

    def run_strip_mine () :
        key_to_mine = key_to_mine_input.get()
        length_of_strip_mine = int(length_of_strip_mine_input.get())

        if key_to_mine == 'left mouse' :
            print('strip mining starting in 5 seconds ...')
            sleep(5)
            print(f'strip mining started for [{length_of_strip_mine} blocks] ...')

            for x in range (length_of_strip_mine) :
                cd.walk_w(0.5)
                pd.leftClick()
                pd.leftClick()
            print('strip mining completed ...')

        elif key_to_mine == 'right mouse' :
            print('strip mining starting in 5 seconds ...')
            sleep(5)
            print(f'strip mining started for [{length_of_strip_mine} blocks] ...')

            for x in range (length_of_strip_mine) :
                cd.walk_w(0.5)
                pd.rightClick()
                pd.rightClick()
            print('strip mining completed ...')

        else :
            print('strip mining starting in 5 seconds ...')
            sleep(5)
            print(f'strip mining started for [{length_of_strip_mine} blocks] ...')

            for x in range (length_of_strip_mine) :
                cd.walk_w(0.5)
                pd.press(key_to_mine)
                pd.press(key_to_mine)
            print('strip mining completed ...')

    run_strip_mine_btn = Button(window, text = 'START STRIP MINE', fg = 'green', command = run_strip_mine)
    run_strip_mine_btn.pack()

# TASK ALGORITHM

def run () :
    task_for_bot = task_for_bot_input.get()

    if task_for_bot == 'build wall' :
        build_wall_initiative()

    elif task_for_bot == 'build pillar' :
        build_pillar_initiative()

    elif task_for_bot == 'autoclicker key' :
        auto_clicker_key_initiative()

    elif task_for_bot == 'strip mine' :
        strip_mine_initiative()

    else :
        print('please choose a valid option')

run_btn = Button(window, text = 'RUN',command = run)
run_btn.pack()

# MAINLOOP

window.mainloop()