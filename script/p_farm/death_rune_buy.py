import threading
import time
import interface
import opencv2
import data.config
import control
from script.x_modules import init
from script.x_modules import camera_view
from script.x_modules import object_detection
from script.x_modules import send_mail
from script.x_modules import logout
from data.script.p_farm import death_rune_buy_config as config

class death_rune_buy(threading.Thread):

    sca = None
    init = None
    camera = None
    engine = None
    input = None
    config = None
    detector_ames = None
    detector_npc = None
    console = None
    signal = None
    xy = None

    STATUS_0 = True
    STATUS_1 = True
    STATUS_2 = True
    STATUS_3 = True
    SCRIPT_PHASE = 0
    INVENTORY_COUNT = 0
    SUCCESS_COUNT = 0
    OUTPUT = None
    COMMAND = None
    CHOOSE = 0
    TIMER = 60*4

    CAMERA = 2

    def __init__(self):
        threading.Thread.__init__(self)
        self.sca = logout.logout
        self.init = init.init()
        self.camera = camera_view.camera_view
        self.engine = opencv2.opencv2
        self.input = control.control
        self.config = config.death_rune_buy_config
        self.detector_ames = object_detection.object_detection()
        self.detector_npc = object_detection.object_detection()
        self.console = interface.interface
        self.signal = send_mail.sendmail

    def run(self):
        self.detector_ames.getStatus(0,self.CAMERA)
        while self.STATUS_0:
            self.COMMAND = input(self.console.TERMINAL_INTERFACE[0] + self.console.SCRIPT[0])
            if int(self.COMMAND) == 1:
                self.CHOOSE = 2
                self.STATUS_0 = False
            elif int(self.COMMAND) == 2:
                self.CHOOSE = 3
                self.STATUS_0 = False
            elif int(self.COMMAND) == 3:
                self.CHOOSE = 4
                self.CAMERA = 3
                self.STATUS_0 = False
            elif int(self.COMMAND) == 4:
                self.CHOOSE = 5
                self.CAMERA = 2
                self.STATUS_0 = False
            else:
                pass
        self.init.startWait()
        self.camera.cameraInit(self.camera,self.CAMERA)
        self.camera.cameraUp(self.camera)
        self.detector_npc.getStatus(1,self.CAMERA,self.CHOOSE)
        while self.STATUS_1:
            if self.SCRIPT_PHASE == 0:
                if self.detector_npc.STATUS_2 == True:
                    if self.detector_npc.STATUS_4 == True:
                        self.detector_npc.STATUS_2 = False
                        self.SCRIPT_PHASE = 1
                else:
                    pass
            elif self.SCRIPT_PHASE == 1:
                self.INVENTORY_COUNT = 0
                time.sleep(2)
                while self.INVENTORY_COUNT <= 4:
                    if self.engine.getObject(self.engine,self.config.ITEM[0]):
                        self.xy = self.engine.getSize(self.engine,self.config.ITEM[0])
                        self.input.moveMouseRight(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.ITEM[0],0.3)
                        if self.engine.getObject(self.engine,self.config.FUNCTION[0]):
                            self.xy = self.engine.getSize(self.engine,self.config.FUNCTION[0])
                            self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.FUNCTION[0],0.4)
                            self.INVENTORY_COUNT += 1
                            if self.engine.getObject(self.engine,self.config.CHATBOX[0]):
                                self.INVENTORY_COUNT = 5
                                self.SCRIPT_PHASE = 2
                            else:
                                pass
                        else:
                            self.INVENTORY_COUNT = 5
                            self.SCRIPT_PHASE = 0
                    else:
                        pass
                self.SCRIPT_PHASE = 2
            elif self.SCRIPT_PHASE == 2:
                if self.engine.getObject(self.engine,self.config.INTERFACE[0]):
                    self.xy = self.engine.getSize(self.engine,self.config.INTERFACE[0])
                    self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.INTERFACE[0],1)
                    self.SCRIPT_PHASE = 3
                else:
                    pass
            elif self.SCRIPT_PHASE == 3:
                if self.SUCCESS_COUNT == 0:
                    if self.engine.getObject(self.engine,self.config.INTERFACE[2]) and self.STATUS_2 == True:
                        self.xy = self.engine.getSize(self.engine,self.config.INTERFACE[2])
                        self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.INTERFACE[2],1)
                        self.SCRIPT_PHASE = 4
                    elif self.STATUS_2 == False:
                        self.SCRIPT_PHASE = 4
                    else:
                        pass
                else:
                    self.SCRIPT_PHASE = 4
            elif self.SCRIPT_PHASE == 4:
                if self.engine.getObject(self.engine,self.config.INTERFACE[1]):
                    self.xy = self.engine.getSize(self.engine,self.config.INTERFACE[1])
                    self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.INTERFACE[1],4)
                    self.SCRIPT_PHASE = 5
                else:
                    self.SCRIPT_PHASE = 5
            elif self.SCRIPT_PHASE == 5:
                if self.engine.getObject(self.engine,self.config.SERVER[self.SUCCESS_COUNT]):
                    self.xy = self.engine.getSize(self.engine,self.config.SERVER[self.SUCCESS_COUNT])
                    self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.SERVER[self.SUCCESS_COUNT],1)
                    self.SUCCESS_COUNT += 1
                    self.SCRIPT_PHASE = 0
                    self.INVENTORY_COUNT = 0
                    self.OUTPUT = "{}{}{}".format(self.console.TERMINAL_INTERFACE[0],self.console.TERMINAL_INTERFACE[3],str(self.SUCCESS_COUNT))
                    print(self.OUTPUT)
                    time.sleep(6)
                    self.detector_npc.STATUS_2 = True
                    self.detector_npc.STATUS_4 = False
                    if self.SUCCESS_COUNT == 12:
                        self.SCRIPT_PHASE = 6
                    else:
                        pass
                else:
                    pass
            elif self.SCRIPT_PHASE == 6:
                self.SCRIPT_PHASE = 7
                self.detector_npc.STATUS_2 = False
                self.detector_npc.STATUS_4 = True
                print(self.console.TERMINAL_INTERFACE[0]+self.console.TERMINAL_INTERFACE[8].format(self.TIMER))
                time.sleep(self.TIMER)
            elif self.SCRIPT_PHASE == 7:
                self.SUCCESS_COUNT = 0
                self.SCRIPT_PHASE = 0
                self.INVENTORY_COUNT = 0
                self.SUCCESS_COUNT = 0
                self.STATUS_2 = False
                self.detector_npc.STATUS_2 = True
                self.detector_npc.STATUS_4 = False
            else:
                pass

    def getStatus(self):
        print(self.console.TERMINAL_INTERFACE[0]+self.config.SCRIPT_NAME+self.console.TERMINAL_INTERFACE[4])
        self.start()