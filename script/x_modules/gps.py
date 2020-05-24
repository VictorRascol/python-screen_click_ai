import time
import opencv2
import control
from data import config as cf
from data.script.x_modules import gps_config as config

class gps():

    engine = opencv2.opencv2
    input = control.control
    config = config.gps_config
    xy = None
    X = 1
    Y = 1

    MAP_DATA = None

    STATUS_0 = False
    CHOOSE = 0

    def __init__(self):
        pass

    def gpsInit(self,mapDATA):
        if self.engine.getObject(self.engine,cf.INTERFACE_SPECIAL[0]) != False:
            self.xy = self.engine.getSize(self.engine,cf.INTERFACE_SPECIAL[0])
            self.input.iMTFMO(self.engine,self.xy[0][0],self.xy[1][0],0.1)
        else:
            pass

        self.gpdMove(self,9,1)
        time.sleep(6)
        self.gpdMove(self, 9, 2)
        time.sleep(6)
        self.gpdMove(self, 9, 2)
        time.sleep(6)
        self.gpdMove(self, 9, 3)
        if mapDATA != None:
            self.MAP_DATA = mapDATA
        else:
            pass

        while self.STATUS_0:
            if self.CHOOSE == 0:
                for INDEX_X, DATA in enumerate(self.MAP_DATA[0]):
                    if self.engine.getVideoCapture(self.engine,self.MAP_DATA[0][INDEX_X],0.99) != False:
                        pass
                    else:
                        pass
            elif self.CHOOSE == 1:
                for INDEX_X, DATA in enumerate(self.MAP_DATA[1]):
                    if self.engine.getVideoCapture(self.engine,self.MAP_DATA[1][INDEX_X],0.99) != False:
                        pass
                    else:
                        pass
            elif self.CHOOSE == 2:
                for INDEX_X, DATA in enumerate(self.MAP_DATA[1]):
                    if self.engine.getVideoCapture(self.engine,self.MAP_DATA[2][INDEX_X],0.99) != False:
                        pass
                    else:
                        pass
            elif self.CHOOSE == 3:
                for INDEX_X, DATA in enumerate(self.MAP_DATA[1]):
                    if self.engine.getVideoCapture(self.engine,self.MAP_DATA[3][INDEX_X],0.99) != False:
                        pass
                    else:
                        pass
            elif self.CHOOSE == 4:
                for INDEX_X, DATA in enumerate(self.MAP_DATA[1]):
                    if self.engine.getVideoCapture(self.engine,self.MAP_DATA[4][INDEX_X],0.99) != False:
                        pass
                    else:
                        pass
            elif self.CHOOSE == 5:
                for INDEX_X, DATA in enumerate(self.MAP_DATA[1]):
                    if self.engine.getVideoCapture(self.engine,self.MAP_DATA[5][INDEX_X],0.99) != False:
                        pass
                    else:
                        pass
            else:
                pass

    def gpdMove(self,X,Y):
        self.input.iMTFMO(self.engine,self.xy[0][0],self.xy[1][0],0.1,X,Y)

