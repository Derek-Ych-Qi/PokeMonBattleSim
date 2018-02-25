import numpy as np
import pandas as pd
from collections import OrderedDict
import pdb

PokeDex = pd.read_csv('./data/PokeDex_Gen7USUM.csv')

_baseNames = ['hp', 'atk', 'def', 'spa', 'spd', 'spe']

class PokeMon(object):
    @classmethod
    def _getType(cls, name):
        types = PokeDex.query('species == @name')[['type_1', 'type_2']].tolist()
        return types

    @classmethod
    def _getBase(cls, name):
        # pdb.set_trace()
        bv = PokeDex.query('species == @name')[_baseNames].values.reshape(-1,)
        return dict(zip(_baseNames, bv))

    @classmethod
    def _parseCharacter(cls, character):
        pass

    def __init__(self, name=None):
        self.name = name
        self.lv = 50
        self.type = self._getType(name)
        self.base = self._getBase(name)
        self.iv = {'hp': 31, 'atk': 31, 'def':31, 'spa':31, 'spd':31, 'spe':31}
        self.ev = {'hp': 0, 'atk': 0, 'def':0, 'spa':0, 'spd':0, 'spe':0}
        self.character = {'atk': 1, 'def':1, 'spa':1, 'spd':1, 'spe':1}
        self.ability = None
        self.moves = None
        self.item = None

    def abilityCalc(self, ability):
        if ability == 'hp':
            return ((self.base[ability]*2 + self.iv[ability] + self.ev[ability]//4) * self.lv) // 100 + 10 + self.lv
        else:
            return int( (((self.base[ability]*2 + self.iv[ability] + self.ev[ability]//4) * self.lv) // 100 + 5) * self.character[ability] )

    def genPanel(self):
        self.panel = OrderedDict()
        for ability in _baseNames:
            self.panel[ability] = self.abilityCalc(ability)
        print(self.panel)

if __name__ == "__main__":
    kingdra = PokeMon('Kingdra')
    kingdra.genPanel()
    
    