import os
import opencv2
import data.config
import control
from data.script.x_modules import logout_config as config

class logout():

    engine = opencv2.opencv2
    input = control.control
    config = config.logout_config
    xy = None

    def __init__(self):
        pass

    def logoutInit(self,option=0):
        if self.engine.getObject(self.engine,self.config.SPECIAL_OBJECT[0]):
            self.xy = self.engine.getSize(self.engine,self.config.SPECIAL_OBJECT[0])
            self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.2,1,self.config.SPECIAL_OBJECT[0],1)
            if self.engine.getObject(self.engine,self.config.SPECIAL_OBJECT[1]):
                self.xy = self.engine.getSize(self.engine,self.config.SPECIAL_OBJECT[1])
                self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.2,1,self.config.SPECIAL_OBJECT[1],1)
                if option == 1:
                    os.system("shutdown -s")
            else:
                pass
        else:
            pass

    def shutdownHost(self):
        os.system("shutdown -s")