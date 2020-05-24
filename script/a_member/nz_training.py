import threading
import keyboard
import time
import random
import interface
import opencv2
import data.config
import control
from script.x_modules import init
from script.x_modules import logout
from script.x_modules import camera_view
from script.x_modules import send_mail
from data.script.a_member import nz_training_config as config

class nz_training(threading.Thread):

    sca = None
    init = None
    camera = None
    engine = None
    input = None
    config = None
    console = None
    signal = None
    xy = None

    STATUS = True
    FIRST_LOOP = True
    OUTPUT = None
    INV_COUNT = 0
    COUNT = 0
    COMMAND = None

    LOOP = 0

    def __init__(self):
        threading.Thread.__init__(self)
        self.sca = logout.logout
        self.init = init.init()
        self.camera = camera_view.camera_view
        self.engine = opencv2.opencv2
        self.input = control.control
        self.config = config.nz_training_config
        self.console = interface.interface
        self.signal = send_mail.sendmail

    def run(self):
        self.init.startWait()
        self.camera.cameraInit(self.camera,2)
        self.camera.cameraUp(self.camera)
        while self.STATUS:
            if self.COUNT <= 24:
                if self.engine.getObject(self.engine,self.config.ITEM[0]):
                    self.xy = self.engine.getSize(self.engine,self.config.ITEM[0])
                    self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.ITEM[0],0.3)
                    self.COUNT += 1
                elif self.engine.getObject(self.engine,self.config.ITEM[1]):
                    self.xy = self.engine.getSize(self.engine,self.config.ITEM[1])
                    self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.ITEM[1],0.3)
                    self.COUNT += 1
                elif self.engine.getObject(self.engine,self.config.ITEM[2]):
                    self.xy = self.engine.getSize(self.engine,self.config.ITEM[2])
                    self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.ITEM[2],0.3)
                    self.COUNT += 1
                elif self.engine.getObject(self.engine,self.config.ITEM[3]):
                    self.xy = self.engine.getSize(self.engine,self.config.ITEM[3])
                    self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.ITEM[3],0.3)
                    self.COUNT += 1
                else:
                    pass
            elif self.COUNT == 24:
                if self.engine.getObject(self.engine,self.config.ITEM[4]):
                    self.xy = self.engine.getSize(self.engine,self.config.ITEM[4])
                    self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.ITEM[4],0.3)
                    self.COUNT += 1
                elif self.engine.getObject(self.engine,self.config.ITEM[5]):
                    self.xy = self.engine.getSize(self.engine,self.config.ITEM[5])
                    self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.ITEM[5],0.3)
                    self.COUNT += 1
                elif self.engine.getObject(self.engine,self.config.ITEM[6]):
                    self.xy = self.engine.getSize(self.engine,self.config.ITEM[6])
                    self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.ITEM[6],0.3)
                    self.COUNT += 1
                elif self.engine.getObject(self.engine,self.config.ITEM[7]):
                    self.xy = self.engine.getSize(self.engine,self.config.ITEM[7])
                    self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.ITEM[7],0.3)
                    self.COUNT += 1
                else:
                    pass
            elif self.COUNT == 25:
                while self.INV_COUNT <= 27:
                    if self.engine.getObject(self.engine,self.config.ITEM[8]):
                        self.xy = self.engine.getSize(self.engine,self.config.ITEM[8])
                        self.input.guzzle(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.ITEM[8],0.01)
                        if self.engine.getObject(self.engine,self.config.FUNCTION[0]):
                            self.xy = self.engine.getSize(self.engine,self.config.FUNCTION[0])
                            self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.FUNCTION[0],0.01)
                            self.INV_COUNT += 1
                        else:
                            print(self.console.TERMINAL_INTERFACE[0]+self.config.FUNCTION[0]+self.console.TERMINAL_INTERFACE[1])
                    else:
                        print(self.console.TERMINAL_INTERFACE[0]+self.config.ITEM[8]+self.console.TERMINAL_INTERFACE[1])
                self.COUNT += 1
                self.INV_COUNT = 0
            elif self.COUNT == 26:
                while self.FIRST_LOOP:
                    if self.engine.getObject(self.engine,self.config.INTERFACE[2]):
                        self.xy = self.engine.getSize(self.engine,self.config.INTERFACE[2])
                        self.input.moveMouseDouble(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.INTERFACE[2],0.02)
                    else:
                        pass
                    if self.engine.getObject(self.engine,self.config.INTERFACE[1]) != True:
                        if self.engine.getObject(self.engine,self.config.ITEM[7]):
                            self.xy = self.engine.getSize(self.engine,self.config.ITEM[7])
                            self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.ITEM[7],0.3)
                        else:
                            pass
                    else:
                        pass
                    if self.engine.getObject(self.engine,self.config.INTERFACE[0]):
                        while self.INV_COUNT <= 2:
                            if self.engine.getObject(self.engine,self.config.ITEM[3]):
                                self.xy = self.engine.getSize(self.engine,self.config.ITEM[3])
                                self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.ITEM[3],0.3)
                                self.INV_COUNT += 1
                            elif self.engine.getObject(self.engine,self.config.ITEM[2]):
                                self.xy = self.engine.getSize(self.engine,self.config.ITEM[2])
                                self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.ITEM[2],0.3)
                                self.INV_COUNT += 1
                            elif self.engine.getObject(self.engine,self.config.ITEM[1]):
                                self.xy = self.engine.getSize(self.engine,self.config.ITEM[1])
                                self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.ITEM[1],0.3)
                                self.INV_COUNT += 1
                            elif self.engine.getObject(self.engine,self.config.ITEM[0]):
                                self.xy = self.engine.getSize(self.engine,self.config.ITEM[0])
                                self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.ITEM[0],0.3)
                                self.INV_COUNT += 1
                            else:
                                pass
                        self.INV_COUNT = 0
                    else:
                        pass
                    if self.engine.getObject(self.engine,self.config.OBJECT[0]):
                        self.STATUS = False
                        self.FIRST_LOOP = False
                        self.signal.mailInit(self.signal,data.config.USERNAME,self.config.SCRIPT_NAME)
                        self.sca.shutdownHost(self.sca)
                        exit()
                    else:
                        pass
                    time.sleep(random.randint(1,50))

                    try:
                        if keyboard.is_pressed('c'):
                            self.COMMAND = input(
                                self.console.TERMINAL_INTERFACE[0]+self.console.TERMINAL_INTERFACE[7])
                            if self.COMMAND == "p" or self.COMMAND == "P" or self.COMMAND == "Pause" or self.COMMAND == "PAUSE" or self.COMMAND == "pause":
                                print(self.console.TERMINAL_INTERFACE[0] + self.console.TERMINAL_INTERFACE[5])
                                time.sleep(30)
                            elif self.COMMAND == "e" or self.COMMAND == "E" or self.COMMAND == "Exit" or self.COMMAND == "EXIT" or self.COMMAND == "exit":
                                self.STATUS = False
                                self.FIRST_LOOP = False
                                exit()
                        else:
                            pass
                    except:
                        pass


    def getStatus(self):
        print(self.console.TERMINAL_INTERFACE[0]+self.config.SCRIPT_NAME+self.console.TERMINAL_INTERFACE[4])
        self.start()