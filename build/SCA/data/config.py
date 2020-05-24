import socket
import getpass

#SCA HOST CONFIG
USERNAME = socket.gethostname()

#SCA CLIENT CONFIG FILE
CLIENT_AUTHOR = "SUIRDNA"
CLIENT_VERSION = 0.25
CLIENT_TECHNOLOGY = "RUNELITE"
PATH_OBJECT = ".\\capture"
CAPTURE_OBJECT = ".\\capture\\generation.png"
CLIENT_LICENSE = None

#OSRS CLIENT CONFIG
CLIENT_CONFIGS = [
    ".\\data\\settings.properties"
]

CLIENT_CONFIGS_PATH = [
    "C:\\Users\\{}\\.runelite".format(getpass.getuser()),
]

#SCA USER CONFIG
ACC_USERNAME = None
ACC_PASSWORD = None
ACC_DEFAULT_WORLD = 302

#SCA INTERFACE CONFIG
INTERFACE = [
    ".\\resources\\interface\\login\\logo.png",
    ".\\resources\\interface\\login\\button\\existing_user.png",
    ".\\resources\\interface\\login\\button\\login.png",
    ".\\resources\\interface\\login\\button\\click_here.png",
]

INTERFACE_SPECIAL = [
    ".\\resources\\interface\\login\\runelite.png",
    ".\\resources\\interface\\login\\osbuddy.png",
    ".\\resources\\interface\\login\\osrs.png",
]


