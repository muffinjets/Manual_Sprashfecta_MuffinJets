from .Utils import ManualFile, convert_to_list

# Load all the base tables
game_table = ManualFile('game.json', dict).load() #dict
item_table = convert_to_list(ManualFile('items.json', list).load(), 'data') #list
location_table = convert_to_list(ManualFile('locations.json', list).load(), 'data') #list
region_table = ManualFile('regions.json', dict).load() #dict
category_table = ManualFile('categories.json', dict).load() #dict
meta_table = ManualFile('meta.json', dict).load() #dict

# Removal of schemas in root of tables
region_table.pop('$schema', '')
category_table.pop('$schema', '') 