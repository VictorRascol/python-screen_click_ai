import time
import interface

class init():

    console = None
    TIMER = 5

    def __init__(self):
        self.console = interface.interface

    def startWait(self):
        print("{}{}".format(self.console.TERMINAL_INTERFACE[0],self.console.MODULE[0]))
        time.sleep(1)
        print("{}{}{}".format(self.console.TERMINAL_INTERFACE[0],self.console.MODULE[1],self.TIMER))
        time.sleep(1)
        print("{}{}{}".format(self.console.TERMINAL_INTERFACE[0],self.console.MODULE[1],self.TIMER-1))
        time.sleep(1)
        print("{}{}{}".format(self.console.TERMINAL_INTERFACE[0],self.console.MODULE[1],self.TIMER-2))
        time.sleep(1)
        print("{}{}{}".format(self.console.TERMINAL_INTERFACE[0],self.console.MODULE[1],self.TIMER-3))
        time.sleep(1)
        print("{}{}{}".format(self.console.TERMINAL_INTERFACE[0],self.console.MODULE[1],self.TIMER-4))
        time.sleep(1)
        print("{}{}".format(self.console.TERMINAL_INTERFACE[0],self.console.MODULE[2]))
