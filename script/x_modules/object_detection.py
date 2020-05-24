import threading
import time
import datetime
import opencv2
import control
import interface
from data.script.x_modules import object_detection_config as config

class object_detection(threading.Thread):

    engine = opencv2.opencv2
    input = control.control
    config = None
    console = None
    xy = None

    CHOOSE = None
    ACTIVE_STATUS = True
    SET_OBJECT = None
    SIZE = None
    TARGET = []
    TIME = 1
    CAMERA = None
    XY_MUL = None
    DATA = None
    RANDOMIZER = 0
    FAILSAFE = 20
    OBJECT_INDEX = 0
    DATE = 0
    DATE_NOW = 0

    STATUS_1 = True
    STATUS_2 = True
    STATUS_3 = True
    STATUS_4 = False
    AMES_STATUS_DETECTION = False
    NPC_STATUS_DETECTION = False
    COUNT = 0
    INV_COUNT = 0
    SUCCESS_COUNT = 0
    OUTPUT = None

    def __init__(self):
        threading.Thread.__init__(self)
        self.config = config.object_detection_config
        self.console = interface.interface

    def run(self):
        if self.CHOOSE == 0:
            self.amesDetection()
        elif self.CHOOSE == 1:
            self.npcDetection()
        elif self.CHOOSE == 2:
            self.enemyDetection()
        else:
            pass

    def amesDetection(self):
        if self.CAMERA == 1:
            self.XY_MUL = 20
        elif self.CAMERA == 2:
            self.XY_MUL = 15
        elif self.CAMERA == 3:
            self.XY_MUL = 10
        elif self.CAMERA == 4:
            self.XY_MUL = 5
        else:
            pass
        while self.STATUS_1:
            time.sleep(2)
            for INDEX,OBJECT in enumerate(self.config.AMES_OBJECT):
                if self.engine.getVideoCapture(self.engine,self.config.AMES_OBJECT[INDEX]) != False:
                    self.STATUS_2 = True
                    self.DATA = self.engine.getVideoCapture(self.engine,self.config.AMES_OBJECT[INDEX])
                    self.input.mvtC(self.input,self.DATA[0][0],self.DATA[1][0]+self.XY_MUL,0.1,1,self.config.AMES_OBJECT[INDEX],self.TIME)
                    while self.STATUS_2:
                        if self.engine.getVideoCapture(self.engine,self.config.FUNCTION[1]) != False:
                            if self.engine.getVideoCapture(self.engine,self.config.FUNCTION[1]) != False:
                                self.DATA = self.engine.getVideoCapture(self.engine,self.config.FUNCTION[1])
                                self.input.mvtD(self.input,self.DATA[0][0],self.DATA[1][0],0.1,1,self.config.FUNCTION[1],self.TIME)
                                time.sleep(2)
                                if self.engine.getVideoCapture(self.engine,self.config.FUNCTION[2]) != False:
                                    print(self.console.TERMINAL_INTERFACE[0]+self.console.OBJECT_DETECTION[5])
                                    time.sleep(self.FAILSAFE)
                                else:
                                    pass
                            else:
                                self.STATUS_2 = False
                        else:
                            self.STATUS_2 = False
                else:
                    pass

    def npcDetection(self):
        if self.CAMERA == 1:
            self.XY_MUL = 20
        elif self.CAMERA == 2:
            self.XY_MUL = 15
        elif self.CAMERA == 3:
            self.XY_MUL = 10
        elif self.CAMERA == 4:
            self.XY_MUL = 5
        else:
            pass
        while self.STATUS_1:
            while self.STATUS_2:
                if self.engine.getVideoCapture(self.engine,self.config.NPC_OBJECT[self.OBJECT_INDEX][0]) != False:
                    try:
                        self.DATA = self.engine.getVideoCapture(self.engine,self.config.NPC_OBJECT[self.OBJECT_INDEX][0])
                        self.input.moveMouseCenter(self.input,self.DATA[0][0],self.DATA[1][0]+self.XY_MUL,0.1,1,self.config.NPC_OBJECT[self.OBJECT_INDEX][0],2)
                        self.STATUS_4 = True
                    except:
                        pass
                else:
                    pass

    def enemyDetection(self):
        print(self.console.TERMINAL_INTERFACE[0]+self.console.OBJECT_DETECTION[1])
        print(self.console.INTERFACE[0])
        while self.ACTIVE_STATUS:
            if self.SET_OBJECT != self.config.SET:
                self.SET_OBJECT = input(self.console.TERMINAL_INTERFACE[0] + self.console.OBJECT_DETECTION[0])
                for INDEX,OBJECT in enumerate(self.config.ENEMY_OBJECT):
                    if self.config.ENEMY_OBJECT[INDEX][1] == self.SET_OBJECT:
                        self.config.ENEMY_OBJECT_ACTIVE.append(self.config.ENEMY_OBJECT[INDEX])
                        print(self.console.TERMINAL_INTERFACE[0]+self.console.OBJECT_DETECTION[2]+self.SET_OBJECT)
                        print(self.console.INTERFACE[0])
                    else:
                        pass
            elif self.SET_OBJECT == self.config.SET:
                print(self.console.INTERFACE[0])
                print(self.console.TERMINAL_INTERFACE[0]+self.console.OBJECT_DETECTION[4])
                self.ACTIVE_STATUS = False
                if self.CAMERA == 1:
                    self.XY_MUL = 20
                elif self.CAMERA == 2:
                    self.XY_MUL = 15
                elif self.CAMERA == 3:
                    self.XY_MUL = 10
                elif self.CAMERA == 4:
                    self.XY_MUL = 5
                else:
                    pass
            else:
                pass
        while self.STATUS_1:
            for INDEX, OBJECT in enumerate(self.config.ENEMY_OBJECT_ACTIVE):
                if self.engine.getVideoCapture(self.engine,self.config.ENEMY_OBJECT_ACTIVE[INDEX][0]) != False:
                    self.STATUS_2 = True
                    self.STATUS_3 = True
                    try:
                        self.DATA = self.engine.getVideoCapture(self.engine,self.config.ENEMY_OBJECT_ACTIVE[INDEX][0])
                        self.input.mvtC(self.input,self.DATA[0][0],self.DATA[1][0]+self.XY_MUL,0.1,1,self.config.ENEMY_OBJECT_ACTIVE[INDEX][0],self.TIME)
                        while self.STATUS_2:
                            if self.engine.getVideoCapture(self.engine,self.config.FUNCTION[0]) != False:
                                try:
                                    self.DATA = self.engine.getVideoCapture(self.engine,self.config.FUNCTION[0])
                                    self.input.mvtD(self.input,self.DATA[0][0],self.DATA[1][0],0.1,1,self.config.FUNCTION[0],self.TIME)
                                    while self.STATUS_3:
                                        if self.engine.getVideoCapture(self.engine,self.config.ENEMY_OBJECT_ACTIVE[INDEX][2],0.99) != False:
                                            self.STATUS_3 = False
                                            self.SUCCESS_COUNT += 1
                                            self.OUTPUT = "{}{}{}".format(self.console.TERMINAL_INTERFACE[0],self.console.OBJECT_DETECTION[3],str(self.SUCCESS_COUNT))
                                            print(self.OUTPUT)
                                            self.STATUS_4 = False
                                            time.sleep(self.TIME*2)
                                        else:
                                            time.sleep(1)
                                            if self.STATUS_4 == False:
                                                x = datetime.datetime.now()
                                                self.DATE = int(x.strftime("%M"))+1
                                                self.STATUS_4 = True
                                            elif self.STATUS_4 == True:
                                                x = datetime.datetime.now()
                                                self.DATE_NOW = int(x.strftime("%M"))
                                                if self.DATE_NOW >= self.DATE:
                                                    self.STATUS_3 = False
                                                    self.STATUS_4 = False
                                                else:
                                                    pass
                                except:
                                    pass
                            else:
                                self.STATUS_2 = False
                    except:
                        pass
                else:
                    pass

    def getStatus(self,choose,camera=0,objectIndex=0):
        if choose == 0:
            self.CHOOSE = 0
            self.CAMERA = camera
        elif choose == 1:
            self.CHOOSE = 1
            self.CAMERA = camera
            self.OBJECT_INDEX = objectIndex
        elif choose == 2:
            self.CHOOSE = 2
            self.CAMERA = camera
        else:
            pass

        if choose != 1 and choose != 2:
            print(self.console.INTERFACE[0])
            print(self.console.TERMINAL_INTERFACE[0] + self.config.SCRIPT_NAME + ": ONLINE")
        else:
            pass
        self.start()