import data.config
import control
from data.script.x_modules import server_choose_config as config

class server_choose():

    engine = None
    input = control.control
    config = config.server_choose_config
    xy = None
    range = None

    def __init__(self,engine):
        self.engine = engine

    def serverInit(self,choose):
        if self.engine.getObject(self.engine,self.config.SPECIAL_OBJECT[0]):
            self.xy = self.engine.getSize(self.engine,self.config.SPECIAL_OBJECT[0])
            self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.SPECIAL_OBJECT[0],2)
            self.chooseInit(choose)
        else:
            pass

    def chooseInit(self,choose):
        for index, server in enumerate(self.config.SPECIAL_INDEX):
            if int(self.config.SPECIAL_INDEX[index]) == int(choose):
                self.chooseServer(index)
            else:
                pass

    def chooseServer(self,choose):
        if self.engine.getObject(self.engine,self.config.SPECIAL_ARRAY[choose],0.9):
            self.xy = self.engine.getSize(self.engine,self.config.SPECIAL_ARRAY[choose],0.9)
            self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.SPECIAL_ARRAY[choose],1)
        else:
            pass