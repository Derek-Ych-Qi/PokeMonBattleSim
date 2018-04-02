__all_types__ = ['Grass', 'Fire', 'Water', 'Bug', 'Normal', 'Dark', 'Poison', 'Electric', 'Ground', 'Ice', 'Fairy', 'Fighting', 'Psychic', 'Rock', 'Ghost', 'Dragon', 'Steel', 'Flying']

_type_effects = {
    'Grass': {'Flying':0.5, 'Poison':0.5, 'Ground':2, 'Rock':2, 'Bug':0.5, 'Steel':0.5, 'Fire':0.5, 'Water':2, 'Grass':0.5, 'Dragon':0.5},
    'Fire': {'Rock':0.5, 'Bug':2, 'Steel':2, 'Fire':0.5, 'Water':0.5, 'Grass':2, 'Ice':2, 'Dragon':0.5},
    'Water': {'Ground':2, 'Rock':2, 'Fire':2, 'Water':0.5, 'Grass':0.5, 'Dragon':0.5},
    'Bug': {'Fighting':0.5, 'Flying':0.5, 'Poison':0.5, 'Ghost':0.5, 'Steel':0.5, 'Fire':0.5, 'Grass':2, 'Psychic':2, 'Dark':2, 'Fairy':0.5},
    'Normal': {'Rock':0.5, 'Steel':0.5},
    'Dark': {'Fighting':0.5, 'Ghost':2, 'Psychic':2, 'Dark':0.5, 'Fairy':0.5},
    'Poison': {'Poison':0.5, 'Ground':0.5, 'Rock':0.5, 'Ghost':0.5, 'Steel':0, 'Grass':2, 'Fairy':2},
    'Electric': {'Flying':2, 'Ground':0, 'Water':2, 'Grass':0.5, 'Electric':0.5, 'Dragon':0.5},
    'Ground': {'Flying':0, 'Poison':2, 'Rock':2, 'Bug':0.5, 'Steel':2, 'Fire':2, 'Grass':0.5, 'Electric':2},
    'Ice': {'Flying':2, 'Ground':2, 'Steel':0.5, 'Fire':0.5, 'Water':0.5, 'Grass':2, 'Ice':0.5, 'Dragon':2},
    'Fairy': {'Fighting':2, 'Poison':0.5, 'Steel':0.5, 'Fire':0.5, 'Dragon':2, 'Dark':2},
    'Fighting': {'Normal':2, 'Flying':0.5, 'Poison':0.5, 'Rock':2, 'Bug':0.5, 'Steel':2, 'Psychic':0.5, 'Ice':2, 'Dark':2, 'Fairy':0.5},
    'Psychic': {'Fighting':2, 'Poison':2, 'Steel':0.5, 'Psychic':0.5, 'Dark':0},
    'Rock': {'Fighting':0.5, 'Flying':2, 'Ground':0.5, 'Bug':2, 'Steel':0.5, 'Fire':2, 'Ice':2},
    'Ghost': {'Normal':0, 'Ghost':2, 'Psychic':2, 'Dark':0.5},
    'Dragon': {'Steel':0.5, 'Dragon':2, 'Fairy':0},
    'Steel': {'Rock':2, 'Steel':0.5, 'Fire':0.5, 'Electric':0.5, 'Water':0.5, 'Ice':2, 'Fairy':2},
    'Flying': {'Fighting':2, 'Rock':0.5, 'Bug':2, 'Steel':0.5, 'Grass':2, 'Electric':0.5}
}

def type_effects(attack, defend):
    return _type_effects[attack].get(defend, 1)

    