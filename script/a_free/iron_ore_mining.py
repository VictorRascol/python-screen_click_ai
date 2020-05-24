import threading
import keyboard
import time
import interface
import opencv2
import data.config
import control
from script.x_modules import init
from script.x_modules import camera_view
from data.script.a_free import iron_ore_mining_config as config

class iron_ore_mining(threading.Thread):

    init = None
    camera = None
    engine = None
    input = None
    config = None
    console = None
    xy = None

    STATUS = True
    FIRST_LOOP = True
    OUTPUT = None
    INV_COUNT = 0
    COUNT = 0
    COMMAND = None

    def __init__(self):
        threading.Thread.__init__(self)
        self.init = init.init()
        self.camera = camera_view.camera_view
        self.engine = opencv2.opencv2
        self.input = control.control
        self.config = config.iron_ore_mining
        self.console = interface.interface

    def run(self):
        self.init.startWait()
        self.camera.cameraInit(self.camera,4)
        self.camera.cameraUp(self.camera)
        while self.STATUS == True:
            self.INV_COUNT = 0
            if self.engine.getObject(self.engine,self.config.OBJECT[3]) != True:
                if self.engine.getObject(self.engine,self.config.OBJECT[0]):
                    self.xy = self.engine.getSize(self.engine,self.config.OBJECT[0])
                    self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.OBJECT[0],1.8)
                    if self.engine.getObject(self.engine,self.config.OBJECT[1]):
                        self.xy = self.engine.getSize(self.engine,self.config.OBJECT[1])
                        self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.OBJECT[1],1.8)
                        if self.engine.getObject(self.engine,self.config.OBJECT[2]):
                            self.xy = self.engine.getSize(self.engine,self.config.OBJECT[2])
                            self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.OBJECT[2],1.8)
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            elif self.engine.getObject(self.engine,self.config.OBJECT[3]):
                while self.INV_COUNT <= 28:
                    if self.engine.getObject(self.engine,self.config.ITEM[1]):
                        self.xy = self.engine.getSize(self.engine,self.config.ITEM[1])
                        self.input.moveMouseDrop(self.input,self.xy[0][0],self.xy[1][0],0.01,0.01,self.config.ITEM[1],0)
                        self.INV_COUNT += 1
                    elif self.engine.getObject(self.engine,self.config.ITEM[2]):
                        self.xy = self.engine.getSize(self.engine,self.config.ITEM[2])
                        self.input.moveMouseDrop(self.input,self.xy[0][0],self.xy[1][0],0.01,0.01,self.config.ITEM[2],0)
                        self.INV_COUNT += 1
                    elif self.engine.getObject(self.engine,self.config.ITEM[0]):
                        self.xy = self.engine.getSize(self.engine,self.config.ITEM[0])
                        self.input.moveMouseDrop(self.input,self.xy[0][0],self.xy[1][0],0.01,0.01,self.config.ITEM[0],0)
                        self.INV_COUNT += 1
                    else:
                        self.INV_COUNT += 1
            else:
                print(self.console.TERMINAL_INTERFACE[0]+self.config.OBJECT[3]+ self.console.TERMINAL_INTERFACE[1])

            try:
                if keyboard.is_pressed('c'):
                    self.COMMAND = input(self.console.TERMINAL_INTERFACE[0]+self.console.TERMINAL_INTERFACE[7])
                    if self.COMMAND == "p" or self.COMMAND == "P" or self.COMMAND == "Pause" or self.COMMAND == "PAUSE" or self.COMMAND == "pause":
                        print(self.console.TERMINAL_INTERFACE[0] + self.console.TERMINAL_INTERFACE[5])
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

