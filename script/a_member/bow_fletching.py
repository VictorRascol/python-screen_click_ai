import threading
import keyboard
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
from data.script.a_member import bow_fletching as config

class bow_fletching(threading.Thread):

    sca = None
    init = None
    camera = None
    engine = None
    input = None
    config = None
    detector = None
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

    def __init__(self):
        threading.Thread.__init__(self)
        self.sca = logout.logout
        self.init = init.init()
        self.camera = camera_view.camera_view
        self.engine = opencv2.opencv2
        self.input = control.control
        self.config = config.bow_fletching_config
        self.detector = object_detection.object_detection()
        self.console = interface.interface
        self.signal = send_mail.sendmail

    def run(self):
        self.init.startWait()
        self.camera.cameraInit(self.camera,4)
        self.camera.cameraUp(self.camera)
        while self.STATUS_0:
            if self.SCRIPT_PHASE == 0:
                while self.STATUS_1:
                    self.detector.npcDetection()
                    if self.detector.NPC_STATUS_DETECTION:
                        self.SCRIPT_PHASE = 1
                        self.STATUS_1 = False
                    else:
                        pass
            elif self.SCRIPT_PHASE == 1:
                if self.engine.getObject(self.engine,self.config.ITEM[0]):
                    self.xy = self.engine.getSize(self.engine,self.config.ITEM[0])
                    self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.ITEM[0],1)
                else:
                    pass
                if self.engine.getObject(self.engine,self.config.ITEM[1]):
                    self.xy = self.engine.getSize(self.engine,self.config.ITEM[1])
                    self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.ITEM[1],1)
                else:
                    self.SCRIPT_PHASE = 96
                if self.engine.getObject(self.engine,self.config.INTERFACE[0]):
                    self.xy = self.engine.getSize(self.engine,self.config.INTERFACE[0])
                    self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.2,1,self.config.INTERFACE[0],1)
                    self.SCRIPT_PHASE = 2
                else:
                    pass
            elif self.SCRIPT_PHASE == 2:
                if self.engine.getObject(self.engine,self.config.ITEM[2]):
                    self.xy = self.engine.getSize(self.engine,self.config.ITEM[2])
                    self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.ITEM[2],1)
                else:
                    pass
                if self.engine.getObject(self.engine,self.config.ITEM[3]):
                    self.xy = self.engine.getSize(self.engine,self.config.ITEM[3])
                    self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.ITEM[3],1)
                else:
                    self.SCRIPT_PHASE = 96
                if self.engine.getObject(self.engine,self.config.FUNCTION[0]):
                    self.xy = self.engine.getSize(self.engine,self.config.FUNCTION[0])
                    self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.FUNCTION[0],50)
                    self.SCRIPT_PHASE = 3
                else:
                    pass
            elif self.SCRIPT_PHASE == 3:
                while self.STATUS_2:
                    self.detector.npcDetection()
                    if self.detector.NPC_STATUS_DETECTION:
                        self.STATUS_2 = False
                    else:
                        pass
                if self.engine.getObject(self.engine,self.config.INTERFACE[1]):
                    self.xy = self.engine.getSize(self.engine,self.config.INTERFACE[1])
                    self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.INTERFACE[1],1)
                    self.SCRIPT_PHASE = 1
                    self.SUCCESS_COUNT += 1
                    self.STATUS_2 = True
                    self.OUTPUT = "{}{}{}".format(self.console.TERMINAL_INTERFACE[0],self.console.TERMINAL_INTERFACE[3],str(self.SUCCESS_COUNT))
                    print(self.OUTPUT)
                else:
                    pass
            elif self.SCRIPT_PHASE == 96:
                print(self.console.TERMINAL_INTERFACE[0]+self.console.TERMINAL_INTERFACE[6])
                self.signal.mailInit(self.signal,data.config.USERNAME,self.config.SCRIPT_NAME)
                self.sca.logoutInit(self.sca,0)
                exit()

            try:
                if keyboard.is_pressed('c'):
                    self.COMMAND = input(self.console.TERMINAL_INTERFACE[0]+self.console.TERMINAL_INTERFACE[7])
                    if self.COMMAND == "p" or self.COMMAND == "P" or self.COMMAND == "Pause" or self.COMMAND == "PAUSE" or self.COMMAND == "pause":
                        print(self.console.TERMINAL_INTERFACE[0]+self.console.TERMINAL_INTERFACE[5])
                        time.sleep(30)
                    elif self.COMMAND == "e" or self.COMMAND == "E" or self.COMMAND == "Exit" or self.COMMAND == "EXIT" or self.COMMAND == "exit":
                        self.STATUS = False
                        exit()
                else:
                    pass
            except:
                pass

    def getStatus(self):
        print(self.console.TERMINAL_INTERFACE[0]+self.config.SCRIPT_NAME+self.console.TERMINAL_INTERFACE[4])
        self.start()