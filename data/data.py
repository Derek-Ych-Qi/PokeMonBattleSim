import pandas as pd

moves = pd.read_csv('commonMoves_Gen7USUM.csv').set_index('name')
allMoves = moves.to_dict('index')

typeEffects = pd.read_csv('typeEffect.csv').fillna(1)
