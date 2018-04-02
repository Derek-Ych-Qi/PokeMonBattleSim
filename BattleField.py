from PokeMon import PokeMon
from data.data import allMoves, typeEffects

class DamageCalc(object):
    def __init__(self, attacker=None, defender=None):
        self.weather = None
        self.terrain = None
        self.trickRoom = False

    def _weatherAdj(self, move):
        if self.weather == 'Sunny':
            if move['type'] == 'Fire': return 1.5
            elif move['type'] == 'Water': return 0.5
        if self.weather == 'Rain':
            if move['type'] == 'Water': return 1.5
            elif move['type'] == 'Fire': return 0.5
        if self.weather == 

    def _calcDamage(self, attacker, defender, move):
        if move['category'] == 'Physical':
            atkStr, defStr = 'atk', 'def'
        elif move['category'] == 'Special':
            atkStr, defStr = 'spa', 'spd'
        _atk = attacker.panel[atkStr]
        _def = defender.panel[defStr]



if __name__ == "__main__":
    attacker = PokeMon('Kingdra', moves=['Surf', 'Ice Beam', 'Draco Meteor'])
    defender = PokeMon('Snorlax', moves=['Return', 'Earthquake'])