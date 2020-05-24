import os
import os.path
import shutil
from data import config
from script.x_modules import server_choose
import interface
import opencv2
import control

class main():

    config = None
    console = None
    engine = None
    input = None

    serverChoose_module = None

    INTERFACE_STATUS = None

    USERNAME = None
    PASSWORD = None

    LOGIN_STATUS = None
    CHOOSE_STATUS = None

    def __init__(self):
        self.config = config
        self.console = interface.interface()
        self.engine = opencv2.opencv2
        self.input = control.control

        self.serverChoose_module = server_choose.server_choose(self.engine)

        self.console.printLogo()
        self.clientInit()
        self.userInit()
        self.login()
        self.startSCA()

    def clientInit(self):
        if os.path.exists(self.config.CLIENT_CONFIGS_PATH[0]):
            if os.path.isfile(self.config.CLIENT_CONFIGS_PATH[0]+"\\settings.properties"):
                pass
            else:
                shutil.copy2(self.config.CLIENT_CONFIGS[0],self.config.CLIENT_CONFIGS_PATH[0]+"\\settings.properties")
        else:
            pass

        self.getInterfaceInformation()
        print(self.console.INTERFACE[0])

    def getInterfaceInformation(self):
        if self.engine.getObject(self.engine,self.config.INTERFACE[0]):
            self.console.printClientProcess(1)
            for index, object in enumerate(self.config.INTERFACE_SPECIAL):
                if self.engine.getObject(self.engine,self.config.INTERFACE_SPECIAL[0]):
                    self.console.printClientType(index)
                    self.INTERFACE_STATUS = True
                    self.serverChoose_module.serverInit(config.ACC_DEFAULT_WORLD)
                else:
                    pass
        else:
            self.console.printClientProcess(0)
            self.INTERFACE_STATUS = False

    def userInit(self):
        if self.INTERFACE_STATUS == True:
            self.USERNAME = input(self.console.TERMINAL_LOGIN[0])
            self.PASSWORD = input(self.console.TERMINAL_LOGIN[1])

    def login(self):
        if self.engine.getObject(self.engine,self.config.INTERFACE[1]):
            xy = self.engine.getSize(self.engine,self.config.INTERFACE[1])
            self.input.moveMouse(self.input,xy[0],xy[1],0.2,1,self.config.INTERFACE[1])
            self.input.typeInfo(self.input,self.USERNAME,self.PASSWORD,0.2)
            if self.engine.getObject(self.engine,self.config.INTERFACE[2]):
                xy = self.engine.getSize(self.engine,self.config.INTERFACE[2])
                self.input.moveMouse(self.input,xy[0],xy[1],0.2,1,self.config.INTERFACE[2],5)
                if self.engine.getObject(self.engine,self.config.INTERFACE[3]):
                    xy = self.engine.getSize(self.engine,self.config.INTERFACE[3])
                    self.input.moveMouse(self,xy[0],xy[1],0.2,1,self.config.INTERFACE[3])
                    self.LOGIN_STATUS = True
                else:
                    self.LOGIN_STATUS = False
            else:
                pass
        else:
            pass

    def interfaceClear(self):
        self.console.clear()
        self.console.printLogo()
        self.console.printSuc()
        print(self.console.INTERFACE[0])
        self.console.start()

    def startSCA(self):
        if self.INTERFACE_STATUS == True:
            if self.LOGIN_STATUS == True:
                self.interfaceClear()
            elif self.LOGIN_STATUS == False:
                self.CHOOSE_STATUS = input(self.console.TERMINAL_INTERFACE[0]+self.console.TERMINAL_LOGIN[2])
                if self.CHOOSE_STATUS == "Yes" or self.CHOOSE_STATUS == "Y" or self.CHOOSE_STATUS == "y":
                    self.interfaceClear()
                else:
                    print(self.console.TERMINAL_INTERFACE[0]+self.console.TERMINAL_COMMAND[0])
                    exit()
            else:
                print(self.console.TERMINAL_INTERFACE[0]+self.config.INTERFACE[1]+self.console.TERMINAL_INTERFACE[1])
                self.CHOOSE_STATUS = input(self.console.TERMINAL_INTERFACE[0]+self.console.TERMINAL_LOGIN[2])
                if self.CHOOSE_STATUS == "Yes" or self.CHOOSE_STATUS == "Y" or self.CHOOSE_STATUS == "y":
                    self.interfaceClear()
                else:
                    exit()
        else:
            self.CHOOSE_STATUS = input(self.console.TERMINAL_INTERFACE[0]+self.console.TERMINAL_LOGIN[4])
            if self.CHOOSE_STATUS == "Yes" or self.CHOOSE_STATUS == "Y" or self.CHOOSE_STATUS == "y":
                self.interfaceClear()
            else:
                print(self.console.TERMINAL_INTERFACE[0]+self.console.TERMINAL_COMMAND[0])
                exit()

sca = main()