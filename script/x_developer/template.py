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
from data.script.x_developer import template_config as config

class template(threading.Thread):

    sca = None
    init = None
    camera = None
    engine = None
    input = None
    config = None
    detector_ames = None
    detector_npc = None
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

    CAMERA = 0

    def __init__(self):
        threading.Thread.__init__(self)
        self.sca = logout.logout
        self.init = init.init()
        self.camera = camera_view.camera_view
        self.engine = opencv2.opencv2
        self.input = control.control
        self.config = config.template
        self.detector_ames = object_detection.object_detection()
        self.detector_npc = object_detection.object_detection()
        self.console = interface.interface
        self.signal = send_mail.sendmail

    def run(self):
        self.init.startWait()
        self.camera.cameraInit(self.camera,self.CAMERA)
        self.detector_ames.getStatus(0,self.CAMERA)
        while self.STATUS_0:
            if self.SCRIPT_PHASE == 0:
                pass
            elif self.SCRIPT_PHASE == 1:
                pass
            else:
                pass

    def getStatus(self):
        print(self.console.TERMINAL_INTERFACE[0]+self.config.SCRIPT_NAME+self.console.TERMINAL_INTERFACE[4])
        self.start()