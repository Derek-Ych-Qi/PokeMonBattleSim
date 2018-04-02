import pdb
from collections import OrderedDict

import numpy as np
import pandas as pd

PokeDex = pd.read_csv('./data/PokeDex_Gen7USUM.csv')

_baseNames = ['hp', 'atk', 'def', 'spa', 'spd', 'spe']

class PokeMon(object):
    @classmethod
    def _getType(cls, name):
        types = PokeDex.query('species == @name')[['type_1', 'type_2']].values.reshape(-1)
        return types

    @classmethod
    def _getBase(cls, name):
        # pdb.set_trace()
        bv = PokeDex.query('species == @name')[_baseNames].values.reshape(-1,)
        return dict(zip(_baseNames, bv))

    @classmethod
    def _parseNature(cls, character):
        pass

    def __init__(self, name=None, **kwargs):
        self.name = name
        self.lv = 50
        self.type = self._getType(name)
        self.base = self._getBase(name)
        self.iv = {'hp':31, 'atk':31, 'def':31, 'spa':31, 'spd':31, 'spe':31}
        self.ev = {'hp':0, 'atk':0, 'def':0, 'spa':0, 'spd':0, 'spe':0}
        self.nature = {'atk':1, 'def':1, 'spa':1, 'spd':1, 'spe':1}
        self.statusBoost = {'atk':0, 'def':0, 'spa':0, 'spd':0, 'spe':0, 'acc':0, 'crt':0, 'eva':0}
        self.ability = kwargs.get('ability' or None)
        self.moves = kwargs.get('moves' or ['Blank'])
        self.item = kwargs.get('item' or None)

        self.genPanel()

    def _abilityCalc(self, ability):
        if ability == 'hp':
            return ((self.base[ability]*2 + self.iv[ability] + self.ev[ability]//4) * self.lv) // 100 + 10 + self.lv
        else:
            return int( (((self.base[ability]*2 + self.iv[ability] + self.ev[ability]//4) * self.lv) // 100 + 5) * self.nature[ability] )

    def genPanel(self):
        self.panel = OrderedDict()
        for ability in _baseNames:
            self.panel[ability] = self._abilityCalc(ability)
        print(self.panel)

    def boostAdj(self):
        for ability in _baseNames:
            if ability == 'hp':continue
            if self.statusBoost[ability] > 0: self.panel[ability] *= (2 + self.statusBoost[ability])/2
            else: self.panel[ability] *= 2 / (2 + self.statusBoost[ability])
    
    def itemAdj(self):
        if self.item == 'Choice Scarf': self.panel['spd'] *= 1.5
        if self.item == 'Choice Band': self.panel['atk'] *= 1.5
        if self.item == 'Choice Specs': self.panel['spa'] *= 1.5
        if self.item == 'Assault Vest': self.panel['spd'] *= 1.5

    def abilityAdj(self):
        if self.ability == 'Huge Power': self.panel['atk'] *= 2

    def adjustPanel(self):
        self.boostAdj()
        self.itemAdj()
        self.abilityAdj()

    def rawDamage(self):
        for move in self.moves:
            move['stab'] = 1.5 if move['type'] in self.type else 1
            move['abilityAdj'] = 1
            move['itemAdj'] = 1
            move['adjPower'] = move['basePower'] * move['stab'] * move['abilityAdj'] * move['itemAdj']

if __name__ == "__main__":
    kingdra = PokeMon('Kingdra')
