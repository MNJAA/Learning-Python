#i made this to afk in GTA V online
import keyboard
from time import sleep,time

# 5 seconds to enter the game
sleep(5)

# this mkae your charchter moves to kill the idling
def alot():
    while True:
        #time() = current time
        Then = time()
        sleep(60)
        Now = time()
        if Now - Then > 60:
            for _ in range(3):
                keyboard.press('a')
                sleep(1)
                keyboard.press('d')
                sleep(1)
                keyboard.press('w')
                sleep(1)
                keyboard.press('s')

def afew():
    while True:
        #time() = current time
        Then = time()
        sleep(60)
        Now = time()
        if Now - Then > 60:
            for _ in range(2):
                keyboard.press('a')
alot()