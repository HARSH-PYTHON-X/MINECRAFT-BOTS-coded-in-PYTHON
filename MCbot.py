# TO USE 

# press [ j ] to auto jump and place block
# press [ x ] and [ w ] to auto walk with auto jump
# press [ x ] and [ m ] to auto strip mine # MAKE SURE YOU ARE POINTING CURSOR AT BLOCK 
# press [ x ] and [ j ] to auto build a tower 10 blocks high
# press [ x ] and [ z ] to auto walk with placing blocks under feets

# threshold [ +, -, to reset [*] ]
# second_threshold [ tp, tm, t0 ]

# press [ q ] to break loop and end programme

# FOR FUN - press [ x ] , [ s ] and [ u ] to sucide while facing under the feet


from time import sleep
import pyautogui as pg
import pydirectinput as pd
import keyboard 
import controlmod as cd
import MCAB_QT as mcqt

print()
print('DYNAMIX CORPORATION - CYBERDEX / MCAB ...')
print()

print('--- LOGS ---')
print()

sleep(3)
print('simualation started ...')
print()

print('first threshold for [ x, z ] axis')
print('second threshold for [ y ] axis')

print()

print('-----------------------------------------')

threshold = 1
second_threshold = 1

while True :
    if keyboard.is_pressed('+') :
        sleep(0.1)
        threshold = threshold + 1
        print('threshold [x, z] axis >', threshold)

    elif keyboard.is_pressed('t') and keyboard.is_pressed('p') :
        sleep(0.1)
        second_threshold = second_threshold + 1
        print('second threshold [y] axis >', second_threshold)
        
    elif keyboard.is_pressed('-') :
        sleep(0.1)
        threshold = threshold - 1
        print('threshold [x, z] axis >', threshold)

    elif keyboard.is_pressed('t') and keyboard.is_pressed('m') :
        sleep(0.1)
        second_threshold = second_threshold - 1
        print('second threshold [y] axis >', second_threshold)

    elif keyboard.is_pressed('*') :
        sleep(0.1)
        threshold = 1
        print('threshold [x, z] axis >', threshold)

    elif keyboard.is_pressed('t') and keyboard.is_pressed('0') :
        sleep(0.1)
        second_threshold = 1
        print('second threshold [y] axis >', second_threshold)
        
    elif keyboard.is_pressed('p') and keyboard.is_pressed('t') :
        sleep(0.1)
        print('threshold >', threshold)
        print('second threshold [y] axis >', second_threshold)

###############################################3

    elif keyboard.is_pressed('j') :
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
        print(f'suciding from [{second_threshold}] blocks ...')
        for x in range (second_threshold) :
            cd.jump_block()
            cd.walk_w(0.5)
        print('!! sucide successful ...')

    elif keyboard.is_pressed('x') and keyboard.is_pressed('z') :
        sleep(1)
        print('auto jump block walk started ...')
        pd.keyDown('w')
        for x in range (15) :
            cd.jump_block()
        pd.keyUp('w')
        print('auto jump block completed ...')

    elif keyboard.is_pressed('x') and keyboard.is_pressed('p') :
        sleep(1)
        print('auto front block placer started ...')
        for x in range (15) :
            cd.place()
            cd.place()
            cd.place()
            cd.walk_w(0.05)
        print('auto front block placer completed ...')

    elif keyboard.is_pressed('x') and keyboard.is_pressed('y') :
        mcqt.show_window_for_building_shelter()
        print('auto shelter builder started :')

    # BUILDERS USING THRESHOLD

    elif keyboard.is_pressed('b') and keyboard.is_pressed('w') :
        sleep(1)
        print(f'auto wall builder started for [length >{threshold} and height >{second_threshold}]...')
        for x in range (threshold) :
            for y in range(second_threshold) :
                cd.jump() 
                sleep(0.1)
                cd.place()
            cd.walk_w(0.5)
            sleep(0.5)
            cd.walk_s(1)
            print(f'{x} pillar completed ...')
        print('auto wall builder completed ...')   
 
    elif keyboard.is_pressed('e') : # AUTCLICKER 
        pd.leftClick() 

    # -------------------------------

    elif keyboard.is_pressed('q') :
        print()
        print('automation terminated ...')
        print() 
        break 
