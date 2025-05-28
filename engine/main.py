import win32gui
import win32con
import os
import time
from modules import Object
from typing import List
from modules.components.transform import Transform
from varTypes.Vector2 import Vector2

# Text dimensions (characters)
TEXT_WIDTH = 100
TEXT_HEIGHT = 10

# Approximate pixels per character (you might need to adjust these based on your font)
CHAR_WIDTH = 12.6  # pixels per character
CHAR_HEIGHT = 30  # pixels per line

# Calculate window size to fit the text
WINDOW_WIDTH = int(TEXT_WIDTH * CHAR_WIDTH)  # adding some padding
WINDOW_HEIGHT = TEXT_HEIGHT * CHAR_HEIGHT  # adding some padding

BUFFER = [[' ' for _ in range(TEXT_WIDTH)] for _ in range(TEXT_HEIGHT)]
gameObjects: List[Object] = []

def set_window_size():
    # Get the console window handle
    hwnd = win32gui.GetForegroundWindow()
    
    # Get the current window position
    x, y, _, _ = win32gui.GetWindowRect(hwnd)
    
    # Set the window size and position
    win32gui.MoveWindow(hwnd, x, y, WINDOW_WIDTH, WINDOW_HEIGHT, True)

# Set console text dimensions
os.system(f'mode con: cols={TEXT_WIDTH} lines={TEXT_HEIGHT}')

# Wait a moment and then set the window size
time.sleep(0.1)
set_window_size()


def set_buffer():
    global BUFFER, gameObjects

    have_transform = False

    for obj in gameObjects:
        for component in obj.components:
            if type(component) == Transform:
                have_transform = True
                break

    if not have_transform:
        return
    

    BUFFER = [[' ' for _ in range(TEXT_WIDTH)] for _ in range(TEXT_HEIGHT)]

    for obj in gameObjects:
        for component in obj.components:
            if type(component) == Transform:
                BUFFER[component.position.y][component.position.x] = obj.sprite

def render():
    global BUFFER
    set_buffer() 
    os.system('cls')
    for i in BUFFER:
        print(''.join(i))

    

obj = Object('Player', 1)
tar = Transform()
tar.position = Vector2(1, 1)
obj.components.append(tar)

while True:
    time.sleep(0.1)
    gameObjects.append(obj)
    render()
