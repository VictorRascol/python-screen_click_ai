import threading
from data import config
import method
from script.x_developer import developer_tools

class interface(threading.Thread):

    scriptLibrary = None
    developerTools = None

    SCA = [
        "ONLINE",
        "OFFLINE",
    ]

    TERMINAL_COMMAND = [
        "sca.exit",
        "run.script",
        "run.developer",
        "sca.library",
        "run",
    ]

    TERMINAL_INTERFACE = [
        "SCA: ",
        " (NOT FOUND)",
        " SCRIPT LOOP BREAK",
        "STARTING LOOP | ",
        ": ONLINE",
        "SCRIPT PAUSED, NEW START IN 30 SEC",
        "TASK IS DONE",
        "PRESS[e] TO EXIT SCA, PRESS[p] TO PAUSE THE SCRIPT: ",
        "SCRIPT PAUSES, NEW START AFTER [{}] SECONDS",
    ]

    TERMINAL_LOGIN = [
        "USERNAME: ",
        "PASSWORD: ",
        "USER NOT DETECTED, IF YOU WANT RUN SCRIPT WITHOUT LOGIN, PRESS[y] AND ENTER: ",
        "CLIENT NOT DETECTED, IF YOU WANT RUN SCRIPT WITHOUT LOGIN, PRESS[y] AND ENTER: ",
        "CLIENT TYPE NOT DETECTED, IF YOU WANT RUN SCRIPT WITHOUT LOGIN, PRESS[y] AND ENTER: ",
    ]

    CLIENT_PROCESS = [
        "- | OSRS: NOT FOUND",
        "+ | OSRS: DETECTED",
    ]

    CLIENT_TYPE = [
        "+ | RUNELITE: DETECTED",
        "+ | OSBUDDY: DETECTED",
        "+ | OSRS: DETECTED",
    ]

    ENGINE_INTERFACE = [
        "(DEV) ",
        "(DEV)(P): ",
    ]

    ENGINE_INPUT = [
        "HOT MUCH TIME GET POSITION COORDINATES: ",
    ]

    OBJECT_DETECTION = [
        "WRITE TARGET: ",
        "TO START SCRIPT WRITE 'start'",
        "ADDED --> ",
        "KILL COUNT --> ",
        "+ | SYSTEM READY, STARTING SCRIPT@",
        "AMES DETECTED[FAILSAFE]@",
    ]

    MODULE = [
        "INITIALIZING SCRIPT...",
        "SCRIPT STARTING AT: ",
        "SCRIPT START!",
    ]

    SCRIPT = [
        "CHOOSE SHOP(Varrock: 1)(Falador: 2)(PestControl: 3)(Yanille: 4): "
    ]

    INTERFACE = [
        "----------------------------------------------------------------------------------",
    ]

    LOOP = 0
    STATUS = True
    COMMAND = None
    COMMAND2 = None
    COMMAND_ARRAY = None

    def __init__(self):
        self.scriptLibrary = method.method()
        self.developerTools = developer_tools.developer_tools()
        threading.Thread.__init__(self)

    def run(self):
        while self.STATUS:
            self.terminal()

    def printLogo(self):
        print(" ____   ____ ____  _____ _____ _   _     ____ _     ___ ____ _  __       _    ___ ")
        print("/ ___| / ___|  _ \| ____| ____| \ | |   / ___| |   |_ _/ ___| |/ /      / \  |_ _| ")
        print("\___ \| |   | |_) |  _| |  _| |  \| |  | |   | |    | | |   | ' /      / _ \  | |")
        print(" ___) | |___|  _ <| |___| |___| |\  |  | |___| |___ | | |___| . \     / ___ \ | | ")
        print("|____/ \____|_| \_\_____|_____|_| \_|___\____|_____|___\____|_|\_\___/_/   \_\___|")
        print("                                   |_____|                      |_____|           \n")
        print("                           POWERED BY " + config.CLIENT_TECHNOLOGY + " | WRITTED BY " + config.CLIENT_AUTHOR + " | VERSION " + str(config.CLIENT_VERSION) + "\n\n")

    def printClientProcess(self,value):
        print("{}".format(self.CLIENT_PROCESS[value]))

    def printClientType(self,value):
        print("{}".format(self.CLIENT_TYPE[value]))

    def printSuc(self):
        print(self.TERMINAL_INTERFACE[0]+self.SCA[0])

    def clear(self):
        self.LOOP = 0
        while self.LOOP <= 20:
            print("\n")
            self.LOOP += 1

    def terminal(self):
        self.COMMAND = input(self.TERMINAL_INTERFACE[0])
        self.COMMAND_ARRAY = self.COMMAND.split(".")
        if self.COMMAND == self.TERMINAL_COMMAND[0]:
            quit()
        elif self.COMMAND == self.TERMINAL_COMMAND[1]:
            self.COMMAND = input(self.TERMINAL_INTERFACE[0]+"run.script --> ")
            if self.COMMAND == self.scriptLibrary.getScript(self.COMMAND,None):
                self.scriptLibrary.setScript(self.COMMAND,None)
                self.STATUS = False
            else:
                pass
        elif self.COMMAND == self.TERMINAL_COMMAND[4]:
            self.COMMAND2 = int(input(self.TERMINAL_INTERFACE[0]+"run.script --> "))
            if self.COMMAND2 == self.scriptLibrary.getScript(None,self.COMMAND2):
                self.scriptLibrary.setScript(None,self.COMMAND2)
                self.STATUS = False
            else:
                pass
        elif self.COMMAND == self.TERMINAL_COMMAND[3]:
            self.scriptLibrary.printNameScript()
        elif self.COMMAND == self.TERMINAL_COMMAND[2]:
            self.developerTools.getPosition()
        elif len(self.COMMAND_ARRAY) != 1:
            if self.COMMAND == self.TERMINAL_COMMAND[1]+"."+self.COMMAND_ARRAY[2]:
                self.scriptLibrary.setScript(self.COMMAND_ARRAY[2],None)
                self.STATUS = False
            else:
                pass
        else:
            pass