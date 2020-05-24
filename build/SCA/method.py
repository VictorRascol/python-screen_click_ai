from script.x_developer import developer_tools
from script.a_free import combat_fighter
from script.a_member import nz_training
from script.a_free import iron_ore_mining
from script.a_member import fish_cooking
from script.a_member import bow_fletching
from script.a_member import herb_cleaning
from script.a_member import marrentill_tar
from script.a_free import sapphire_ring_crafting
from script.p_farm import death_rune_buy
from data import method_config as config

class method():

    config = None

    OBJECT_LIBRARY = []
    CURRENT_SCRIPT = None

    def __init__(self):
        self.config = config.method_config
        self.OBJECT_LIBRARY.append(developer_tools.developer_tools())
        self.OBJECT_LIBRARY.append(combat_fighter.combat_fighter())
        self.OBJECT_LIBRARY.append(nz_training.nz_training())
        self.OBJECT_LIBRARY.append(iron_ore_mining.iron_ore_mining())
        self.OBJECT_LIBRARY.append(fish_cooking.fish_cooking())
        self.OBJECT_LIBRARY.append(bow_fletching.bow_fletching())
        self.OBJECT_LIBRARY.append(herb_cleaning.herb_cleaning())
        self.OBJECT_LIBRARY.append(marrentill_tar.marrentill_tar())
        self.OBJECT_LIBRARY.append(sapphire_ring_crafting.sapphire_ring_crafting())
        self.OBJECT_LIBRARY.append(death_rune_buy.death_rune_buy())

    def getScript(self,object1,object2):
        if object1 != None:
            for SCRIPT in self.config.SCRIPT_LIBRARY:
                if SCRIPT == object1:
                    return SCRIPT
                else:
                    pass
        elif object2 != None:
            for INDEX,SCRIPT in enumerate(self.config.SCRIPT_LIBRARY):
                if INDEX == object2:
                    return INDEX
                else:
                    pass

    def setScript(self,name,name2):
        if name != None:
            for INDEX,SCRIPT in enumerate(self.config.SCRIPT_LIBRARY):
                if SCRIPT == name:
                    self.startScript(INDEX)
        elif name2 != None:
            for INDEX,SCRIPT in enumerate(self.config.SCRIPT_LIBRARY):
                if INDEX == name2:
                    self.startScript(INDEX)

    def startScript(self,index):
        self.CURRENT_SCRIPT = self.OBJECT_LIBRARY[index]
        self.CURRENT_SCRIPT.getStatus()

    def printNameScript(self):
        for index,string in enumerate(self.config.SCRIPT_LIBRARY):
            print("{}. {} --> {} ".format(index,string,self.config.ABOUT_SCRIPT[index]))