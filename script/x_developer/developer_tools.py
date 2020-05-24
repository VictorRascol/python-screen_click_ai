import threading
import random
import os
import time
import smtplib
import socket
from os import walk
from pynput.keyboard import Controller,Key
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from script.x_modules import send_mail
import data.config
import interface
import opencv2
from PIL import ImageGrab
import control
import keyboard
import pyautogui
import pynput
import numpy as np
import cv2
import mss
import numpy
from pynput.keyboard import Controller, Key
from script.x_modules import camera_view
from script.x_modules import server_choose
from script.x_modules import object_detection
from script.x_modules import gps
import getpass
from data import config as cf
from data.script.x_modules import object_detection_config as config
from data.script.x_modules import gps_config as gps_config
from script.x_modules import init

class developer_tools(threading.Thread):

    init = None
    camera = None
    engine = None
    input = None
    config = None
    console = None
    gps = None
    detector = None
    xy = None

    SCRIPT_NAME = "DEVELOPER_TOOLS 0.2v"
    STATUS = True
    FIRST_LOOP = True
    COUNT = 0
    INV_COUNT = 0
    OUTPUT = None


    position = None

    DEV = [

    ]

    def __init__(self):
        threading.Thread.__init__(self)
        self.init = init.init()
        self.camera = camera_view.camera_view
        self.engine = opencv2.opencv2
        self.input = control.control
        self.console = interface.interface
        self.gps = gps.gps
        self.detector = object_detection.object_detection
        self.config = config.object_detection_config

    def run(self):
        #self.getPosition()
        self.testModule()

    def testModule(self):
        pass
        #self.init.startWait()
        #self.camera.cameraUp(self.camera)
        #self.gps.gpsInit(self.gps,gps_config.gps_config.SAPPHIRE_RING_CRAFTING)

    def getPosition(self):
        self.engine.getPosition(self.engine)

    def createBigArray(self):
        for x in range(25):
            if x < 10:
                print("\".\\\\resources\\\\interface\\\\x_modules\\\\server_choose\\\\server\\\\50"+ str(x) +".png\",")
            elif x >= 10:
                print("\".\\\\resources\\\\interface\\\\x_modules\\\\server_choose\\\\server\\\\5"+ str(x) +".png\",")

    def getFileNames(self):
        for (dirpath, dirnames, filenames) in walk(".\\resources\\interface\\x_modules\\server_choose\\server\\"):
            string = str(filenames)
            clearText = string.replace(".png","")
            print(clearText+"\n")
            break

    def getStatus(self):
        print(self.console.TERMINAL_INTERFACE[0]+self.SCRIPT_NAME+self.console.TERMINAL_INTERFACE[4])
        self.start()