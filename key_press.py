import time
import pynput
from pynput.keyboard import Key, Controller

time.sleep(10)
keyboard = Controller()
keyboard.press(Key.enter)
keyboard.press('b')
keyboard.press('c')