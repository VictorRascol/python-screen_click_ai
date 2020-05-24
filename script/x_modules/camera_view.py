import opencv2
import data.config
import control
from data.script.x_modules import camera_view_config as config

class camera_view():

    engine = opencv2.opencv2
    input = control.control
    config = config.camera_view_config
    xy = None

    def __init__(self):
        pass

    def cameraInit(self,choose):
        if self.engine.getObject(self.engine,self.config.SPECIAL_OBJECT[0]):
            self.xy = self.engine.getSize(self.engine,self.config.SPECIAL_OBJECT[0])
            self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.SPECIAL_OBJECT[0],0.3)
            if self.engine.getObject(self.engine,self.config.SPECIAL_OBJECT[1]):
                self.xy = self.engine.getSize(self.engine,self.config.SPECIAL_OBJECT[1])
                self.input.moveMouseToCoordinate(
                    self.input,
                    self.input.moveMouseCenter(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.SPECIAL_OBJECT[1],0.3,True),
                    self.config.COORDINATE_OPTIONS,
                    choose,
                    1
                )
                if self.engine.getObject(self.engine,self.config.SPECIAL_OBJECT[2]):
                    self.xy = self.engine.getSize(self.engine,self.config.SPECIAL_OBJECT[2])
                    self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.SPECIAL_OBJECT[2],0.3)
                else:
                    pass
            else:
                pass
        else:
            pass

    def cameraUp(self):
        if self.engine.getObject(self.engine,self.config.SPECIAL_OBJECT[2]):
            self.xy = self.engine.getSize(self.engine,self.config.SPECIAL_OBJECT[2])
            self.input.moveMouse(self.input,self.xy[0][0],self.xy[1][0],0.1,1,self.config.SPECIAL_OBJECT[2],0.3)
            self.input.cameraAngle(self.input,"up",4)