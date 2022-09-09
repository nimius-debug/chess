from turtle import screensize
import cv2
import numpy as np
import pyautogui as pg

#take screen shot
screenshot = pg.screenshot()
#adjust the color
screenshot = cv2.cvtColor(np.array(screenshot),cv2.COLOR_RGB2BGR)

#draw
board = pg.locateOnScreen('board.png')

