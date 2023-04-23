# TO USE 

# press [ j ] to auto jump and place block
# press [ x ] and [ w ] to auto walk with auto jump
# press [ x ] and [ m ] to auto strip mine # MAKE SURE YOU ARE POINTING CURSOR AT BLOCK 
# press [ x ] and [ j ] to auto build a tower 10 blocks high
# press [ x ] and [ z ] to auto walk with placing blocks under feets

# press [ q ] to break loop and end programme

# FOR FUN - press [ x ] , [ s ] and [ u ] to sucide while facing under the feet

from time import sleep
import pyautogui as pg
import pydirectinput as pd
import keyboard 
import controlmod as cd

print()
print('--- LOGS ---')
print()

sleep(3)
print('simualation started ...')
print()

while True :
    if keyboard.is_pressed('j') :
        print('auto block jumped ...')
        cd.jump_block()

    elif keyboard.is_pressed('x') and keyboard.is_pressed('w') :
        sleep(1)
        print('auto walk started ...')
        pd.keyDown('w')
        for x in range(30) :
            cd.jump()
        pd.keyUp('w')
        print('auto walk completed ...')

    elif keyboard.is_pressed('x') and keyboard.is_pressed('m') :
        sleep(1)
        print('auto mined [10 blocks] started ...')
        for x in range (10) :
            cd.walk_w(0.3)
            cd.destroy(0.1)
            cd.destroy(0.1)
        print('auto mined [10 blocks] completed ...')

    elif keyboard.is_pressed('x') and keyboard.is_pressed('j') :
        sleep(1)
        print('auto jump block [10 blocks] started ...')
        for x in range (10) :
            cd.jump_block()
        print('auto jump block [10 blocks] completed ...')

    elif keyboard.is_pressed('x') and keyboard.is_pressed('s') and keyboard.is_pressed('u') :
        sleep(1)
        print('suciding from [15 blocks]')
        for x in range (15) :
            cd.jump_block()
        cd.walk_w(0.5)
        print('sucide successfull')

    elif keyboard.is_pressed('x') and keyboard.is_pressed('z') :
        sleep(1)
        print('auto jump block walk started ...')
        pd.keyDown('w')
        for x in range (15) :
            cd.jump_block()
        pd.keyUp('w')
        print('auto jump block completed ...')

    # -------------------------------

    elif keyboard.is_pressed('q') :
        print()
        print('automation terminated ...')
        print()
        break
