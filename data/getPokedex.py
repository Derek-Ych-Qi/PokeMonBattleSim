import requests
import pandas as pd
from collections import OrderedDict

datadir = 'https://raw.githubusercontent.com/Zarel/Pokemon-Showdown/master/data/pokedex.js'
def _extractContent(text, key, endStr=',\\n\\t'):
    try:
        start = text.index(key) + len(key)
        end = text.index(endStr, start)
        s = text[start:end]
        return s
    except:
        return '""'

def _parseType(typeList):
    type1 = typeList[0]
    try: type2 = typeList[1]
    except:
        type2 = ''
    return type1, type2

def _parseBaseValue(text):
    res = OrderedDict()
    res['hp']  = eval(_extractContent(text, 'hp: ', ', '))
    res['atk'] = eval(_extractContent(text, 'atk: ', ', '))
    res['def'] = eval(_extractContent(text, 'def: ', ', '))
    res['spa'] = eval(_extractContent(text, 'spa: ', ', '))
    res['spd'] = eval(_extractContent(text, 'spd: ', ', '))
    res['spe'] = eval(_extractContent(text, 'spe: ', '},'))
    return res

def _parseAbility(text):
    tmp = _extractContent(text, 'abilities: ')
    tmp = tmp.replace('H', '2')
    tmp = tmp.replace('S', '1') # for greninja
    tmp = eval(tmp)
    res = OrderedDict()
    res['ability_1'] = tmp.get(0, '')
    res['ability_2'] = tmp.get(1, '')
    res['ability_h'] = tmp.get(2, '')
    return res

def parseLine(line):
    dfRow = OrderedDict()
    dfRow['numNational'] = eval(_extractContent(line, 'num: '))
    if dfRow['numNational'] <= 0: return None # don't know what ghost is in it
    dfRow['species'] = eval(_extractContent(line, 'species: '))
    dfRow['baseSpecies'] = eval(_extractContent(line, 'baseSpecies: '))
    dfRow['type_1'], dfRow['type_2'] = _parseType( eval(_extractContent(line, 'types: ')) )
    dfRow.update(_parseBaseValue(line))
    dfRow.update(_parseAbility(line))
    return dfRow

def main():
    s = requests.get(datadir)
    s = str(s.content)
    s = s[s.find('{'):]
    allPms = s.split('\\n\\t},')[:-1]
    dfRows = []
    for pm in allPms:
        dfRow = parseLine(pm)
        if not dfRow: continue
        dfRows.append(dfRow)
        
    df = pd.DataFrame(dfRows)
    df.to_csv('PokeDex_Gen7USUM.csv')

if __name__ == "__main__":
    main()