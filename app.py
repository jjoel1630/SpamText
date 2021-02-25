import pyautogui
import time
import random

print("what do you want to spam?")
text = input()

sleeptime = input("sleep time?\n")

file = open('spamtext.txt', 'r').read()
file_text = file.splitlines()

print("how many times do you wanna spam")
times = input()

print("spam will start in 10 seconds")

time.sleep(10)

# in this below for loop, you can change the commands to whatever using the modul pyautogui

for x in range(0, int(times)):
    pyautogui.typewrite(text)
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(float(sleeptime))

print("spam completed")
