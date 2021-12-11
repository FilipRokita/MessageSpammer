#MessageSpammer
#Filip Rokita
#www.filiprokita.com

import pyautogui
import keyboard
import time

startButton = input("START BUTTON: ")
stopButton = input("STOP BUTTON: ")
file = input("FILE: ")

while True:
    if keyboard.is_pressed(startButton) == True:
        print("STARTED")
        f = open(file)
        if keyboard.is_pressed(stopButton) == False:
            for line in f:
                pyautogui.write(line)
                print("PRINTED: "+line)
        else:
            f.close()
            print("STOPPED")