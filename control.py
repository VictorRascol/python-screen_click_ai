import pyautogui
from pynput.mouse import Button,Controller
import random
import time
from PIL import Image

class control():

    MOUSE = None

    IMAGE = None
    W = None
    H = None
    MOUSE_XY = None

    STATUS = True
    SUPER_COORDINATE = 0
    INDEX = None
    OBJECT = None

    KEY_CONTROL = ["w","d","s","a","alt"]
    CAMERA_CONTROL = ["up", "down", "left", "right"]

    def __init__(self):
        pass

    #init Mouse To First Map Object
    def iMTFMO(self,x_axis,y_axis,dur,index_x=1,index_y=1):
        MAP_X = 50
        MAP_Y = 70
        MAP_INDEX_X = 1
        MAP_INDEX_Y = 1

        if index_x == 1:
            pass
        else:
            MAP_INDEX_X = index_x
        if index_y == 1:
            pass
        else:
            MAP_INDEX_Y = index_y

        try:
            pyautogui.moveTo(x_axis+MAP_X*MAP_INDEX_X,y_axis+MAP_Y*MAP_INDEX_Y,dur)
            self.MOUSE_XY = pyautogui.position()
            return self.MOUSE_XY
        except:
            pass

    def mvtD(self,x_axis,y_axis,dur,click_dur,target,pause=0):
        try:
            self.IMAGE = Image.open(target)
            self.W, self.H = self.IMAGE.size
            pyautogui.moveTo(random.randint(x_axis,x_axis+self.W),random.randint(y_axis,y_axis+self.H),dur)
            self.MOUSE_XY = pyautogui.position()
            pyautogui.click(self.MOUSE_XY[0],self.MOUSE_XY[1])
            time.sleep(pause)
        except:
            pass

    def mvtC(self,x_axis,y_axis,dur,click_dur,target,pause=0,status=False,lib=0):
        try:
            self.IMAGE = Image.open(target)
            self.W, self.H = self.IMAGE.size
            if lib == 0:
                if status == False:
                    pyautogui.moveTo(x_axis+self.W/2,y_axis+self.H/2,dur)
                    self.MOUSE_XY = pyautogui.position()
                    pyautogui.rightClick(self.MOUSE_XY[0],self.MOUSE_XY[1],click_dur)
                    time.sleep(pause)
                else:
                    pyautogui.moveTo(x_axis+self.W/2,y_axis+self.H/2,dur)
                    self.MOUSE_XY = pyautogui.position()
                    return self.MOUSE_XY[0]
            elif lib == 1:
                self.MOUSE = Controller()
                if status == False:
                    pyautogui.moveTo(x_axis+self.W/2,y_axis+self.H/2,dur)
                    self.MOUSE.click(Button.right,1)
                    time.sleep(pause)
                else:
                    pyautogui.moveTo(x_axis+self.W/2,y_axis+self.H/2,dur)
                    self.MOUSE_XY = pyautogui.position()
                    return self.MOUSE_XY[0]
            else:
                pass
        except:
            pass

    def moveMouse(self,x_axis,y_axis,dur,click_dur,target,pause=0):
        try:
            self.IMAGE = Image.open(target)
            self.W, self.H = self.IMAGE.size
            pyautogui.moveTo(random.randint(x_axis,x_axis+self.W),random.randint(y_axis,y_axis+self.H),dur)
            self.MOUSE_XY = pyautogui.position()
            pyautogui.click(self.MOUSE_XY[0],self.MOUSE_XY[1],click_dur)
            time.sleep(pause)
        except:
            pass

    def moveMouseDouble(self,x_axis,y_axis,dur,click_dur,target,pause=0):
        try:
            self.IMAGE = Image.open(target)
            self.W, self.H = self.IMAGE.size
            pyautogui.moveTo(random.randint(x_axis,x_axis+self.W),random.randint(y_axis,y_axis+self.H),dur)
            self.MOUSE_XY = pyautogui.position()
            pyautogui.click(self.MOUSE_XY[0],self.MOUSE_XY[1],click_dur)
            time.sleep(1)
            pyautogui.click(self.MOUSE_XY[0],self.MOUSE_XY[1],click_dur)
            time.sleep(pause)
        except:
            pass

    def moveMouseRight(self,x_axis,y_axis,dur,click_dur,target,pause=0):
        try:
            self.IMAGE = Image.open(target)
            self.W, self.H = self.IMAGE.size
            pyautogui.moveTo(random.randint(x_axis,x_axis+self.W),random.randint(y_axis,y_axis+self.H),dur)
            self.MOUSE_XY = pyautogui.position()
            pyautogui.rightClick(self.MOUSE_XY[0],self.MOUSE_XY[1],click_dur)
            time.sleep(pause)
        except:
            pass

    def moveMouseDrop(self,x_axis,y_axis,dur,click_dur,target,pause=0):
        try:
            self.IMAGE = Image.open(target)
            self.W, self.H = self.IMAGE.size
            pyautogui.moveTo(random.randint(x_axis,x_axis+self.W),random.randint(y_axis,y_axis+self.H),dur)
            self.MOUSE_XY = pyautogui.position()
            pyautogui.keyDown('shift')
            pyautogui.click(self.MOUSE_XY[0],self.MOUSE_XY[1],interval=click_dur)
            pyautogui.keyUp('shift')
            time.sleep(pause)
        except:
            pass

    def moveMouseCenter(self,x_axis,y_axis,dur,click_dur,target,pause=0,status=False,lib=0):
        try:
            self.IMAGE = Image.open(target)
            self.W, self.H = self.IMAGE.size
            if lib == 0:
                if status == False:
                    pyautogui.moveTo(x_axis+self.W/2,y_axis+self.H/2,dur)
                    self.MOUSE_XY = pyautogui.position()
                    pyautogui.click(self.MOUSE_XY[0],self.MOUSE_XY[1],click_dur)
                    time.sleep(pause)
                else:
                    pyautogui.moveTo(x_axis+self.W/2,y_axis+self.H/2,dur)
                    self.MOUSE_XY = pyautogui.position()
                    return self.MOUSE_XY[0]
            elif lib == 1:
                self.MOUSE = Controller()
                if status == False:
                    pyautogui.moveTo(x_axis+self.W/2,y_axis+self.H/2,dur)
                    self.MOUSE.click(Button.left,1)
                    time.sleep(pause)
                else:
                    pyautogui.moveTo(x_axis+self.W/2,y_axis+self.H/2,dur)
                    self.MOUSE_XY = pyautogui.position()
                    return self.MOUSE_XY[0]
            else:
                pass
        except:
            pass

    def moveMouseToCoordinate(self,coordinate,options,choose,pause=0):
        try:
            self.STATUS = True
            self.SUPER_COORDINATE = 0
            self.INDEX = 0
            self.OBJECT = 0
            for self.INDEX, self.OBJECT in enumerate(options):
                if self.STATUS:
                    if self.INDEX != choose:
                        self.SUPER_COORDINATE = self.SUPER_COORDINATE+self.OBJECT
                    elif self.INDEX == choose:
                        self.STATUS = False
                        self.SUPER_COORDINATE = self.SUPER_COORDINATE+self.OBJECT
                        time.sleep(pause)
                        pyautogui.moveTo(coordinate+self.SUPER_COORDINATE)
                        time.sleep(pause)
                        pyautogui.click()
                else:
                    pass
        except:
            pass

    def cameraAngle(self,key,duration):
        try:
            if self.CAMERA_CONTROL[0] == key:
                pyautogui.keyDown("up")
                time.sleep(duration)
                pyautogui.keyUp("up")
            elif self.CAMERA_CONTROL[1] == key:
                pyautogui.keyDown("down")
                time.sleep(duration)
                pyautogui.keyUp("down")
            elif self.CAMERA_CONTROL[2] == key:
                pyautogui.keyDown("left")
                time.sleep(duration)
                pyautogui.keyUp("left")
            elif self.CAMERA_CONTROL[3] == key:
                pyautogui.keyDown("right")
                time.sleep(duration)
                pyautogui.keyUp("rigth")
            else:
                pass
        except:
            pass

    def playerController(self,key,duration):
        try:
            if self.KEY_CONTROL[0] == key:
                pyautogui.keyDown("w")
                time.sleep(duration)
                pyautogui.keyUp("w")
            elif self.KEY_CONTROL[1] == key:
                pyautogui.keyDown("d")
                time.sleep(duration)
                pyautogui.keyUp("d")
            elif self.KEY_CONTROL[2] == key:
                pyautogui.keyDown("s")
                time.sleep(duration)
                pyautogui.keyUp("s")
            elif self.KEY_CONTROL[3] == key:
                pyautogui.keyDown("a")
                time.sleep(duration)
                pyautogui.keyUp("a")
            elif self.KEY_CONTROL[4] == key:
                pyautogui.keyDown("alt")
                time.sleep(duration)
                pyautogui.keyUp("alt")
            else:
                pass
        except:
            pass

    def typeInfo(self,username,password,dur):
        try:
            pyautogui.typewrite(username,dur)
            pyautogui.press("tab")
            pyautogui.typewrite(password,dur)
        except:
            pass

    def guzzle(self,x_axis,y_axis,dur,click_dur,target,pause=0):
        try:
            self.IMAGE = Image.open(target)
            self.W, self.H = self.IMAGE.size
            pyautogui.moveTo(x_axis+self.W/2,y_axis+self.H/2,dur)
            self.MOUSE_XY = pyautogui.position()
            pyautogui.rightClick(self.MOUSE_XY[0],self.MOUSE_XY[1],click_dur)
            time.sleep(pause)
        except:
            pass