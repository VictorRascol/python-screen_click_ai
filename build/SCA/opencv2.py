import pyautogui
import time
import cv2
import numpy
import ctypes
from PIL import ImageGrab
from data import config
import interface
import control

class opencv2():

    control = control.control
    config = config

    USER32 = None
    MONITOR = None
    DATA = None

    STATUS_0 = True

    OBJECT_INTERFACE = None
    OBJECT_INTERFACE_GRAY = None
    TEMPLATE = None
    MATCHES = None
    LOCATION = None
    XY = None

    COUNT = 0

    POSITION_OPTION = 0
    POSITION_START = 0
    POSITION_COORDINATE = 0

    def __init__(self):
        pass

    def screenInit(self):
        self.USER32 = ctypes.windll.user32
        self.MONITOR = (0,0,self.USER32.GetSystemMetrics(0), self.USER32.GetSystemMetrics(1))

    def getVideoCapture(self,target,matches=0.8):
        self.STATUS_0 = True
        while self.STATUS_0:
            IMAGE = numpy.asarray(ImageGrab.grab(bbox=self.MONITOR))
            self.OBJECT_INTERFACE_GRAY = cv2.cvtColor(IMAGE,cv2.COLOR_BGR2GRAY)
            self.TEMPLATE = cv2.imread(target,cv2.IMREAD_GRAYSCALE)
            self.MATCHES = cv2.matchTemplate(self.OBJECT_INTERFACE_GRAY,self.TEMPLATE,cv2.TM_CCOEFF_NORMED)
            self.LOCATION = numpy.where(self.MATCHES >= matches)
            if self.LOCATION[0].size != 0 and self.LOCATION[1][0] != 0:
                self.STATUS_0 = False
                self.DATA = [self.LOCATION[1],self.LOCATION[0],self.LOCATION[0].size]
                return self.DATA
            else:
                return False

    def getObject(self,target,matches=0.8):
        self.generation(self)
        self.OBJECT_INTERFACE_GRAY = cv2.cvtColor(self.OBJECT_INTERFACE,cv2.COLOR_BGR2GRAY)
        self.TEMPLATE = cv2.imread(target,cv2.IMREAD_GRAYSCALE)
        self.MATCHES = cv2.matchTemplate(self.OBJECT_INTERFACE_GRAY,self.TEMPLATE,cv2.TM_CCOEFF_NORMED)
        self.LOCATION = numpy.where(self.MATCHES >= matches)
        if self.LOCATION[0].size != 0 and self.LOCATION[1][0] != 0:
            return True
        else:
            return False

    def getObjects(self,target,index,matches=0.8):
        self.generation(self)
        while self.COUNT <= index:
            self.OBJECT_INTERFACE_GRAY = cv2.cvtColor(self.OBJECT_INTERFACE,cv2.COLOR_BGR2GRAY)
            self.TEMPLATE = cv2.imread(target,cv2.IMREAD_GRAYSCALE)
            self.MATCHES = cv2.matchTemplate(self.OBJECT_INTERFACE_GRAY,self.TEMPLATE,cv2.TM_CCOEFF_NORMED)
            self.LOCATION = numpy.where(self.MATCHES >= matches)
            if self.LOCATION[0][index].size != 0 and self.LOCATION[1][index] != 0:
                self.XY = [self.LOCATION[1][index],self.LOCATION[0][index]]
                return self.XY
            else:
                pass
            self.COUNT += 1

    def getObjectCount(self,target,matches=0.8):
        self.generation(self)
        self.OBJECT_INTERFACE_GRAY = cv2.cvtColor(self.OBJECT_INTERFACE,cv2.COLOR_BGR2GRAY)
        self.TEMPLATE = cv2.imread(target,cv2.IMREAD_GRAYSCALE)
        self.MATCHES = cv2.matchTemplate(self.OBJECT_INTERFACE_GRAY,self.TEMPLATE,cv2.TM_CCOEFF_NORMED)
        self.LOCATION = numpy.where(self.MATCHES >= matches)
        if self.LOCATION[0].size != 0 and self.LOCATION[1][0] != 0:
            return self.LOCATION[0].size
        else:
            return False

    def getSize(self,target,matches=0.8):
        self.generation(self)
        self.OBJECT_INTERFACE_GRAY = cv2.cvtColor(self.OBJECT_INTERFACE,cv2.COLOR_BGR2GRAY)
        self.TEMPLATE = cv2.imread(target,cv2.IMREAD_GRAYSCALE)
        self.MATCHES = cv2.matchTemplate(self.OBJECT_INTERFACE_GRAY,self.TEMPLATE,cv2.TM_CCOEFF_NORMED)
        self.LOCATION = numpy.where(self.MATCHES >= matches)
        if self.LOCATION[0].size != 0 and self.LOCATION[1][0] != 0:
            self.XY = [self.LOCATION[1],self.LOCATION[0]]
            return self.XY
        else:
            pass

    def getPosition(self):
        self.generation(self)
        self.POSITION_OPTION = input(interface.interface.ENGINE_INTERFACE[0]+interface.interface.ENGINE_INPUT[0])
        while int(self.POSITION_OPTION) > self.POSITION_START:
            time.sleep(2)
            self.POSITION_COORDINATE = pyautogui.position()
            print("{}{}".format(interface.interface.ENGINE_INTERFACE[1],self.POSITION_COORDINATE))
            self.POSITION_START += 1

    def generation(self):
        self.OBJECT_INTERFACE = numpy.asarray(ImageGrab.grab(bbox=self.MONITOR))