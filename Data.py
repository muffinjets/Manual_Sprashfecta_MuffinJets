import json
import logging
import os
import pkgutil

from .DataValidation import DataValidation, ValidationError

from .hooks.Data import \
    after_load_game_file, \
    after_load_item_file, after_load_location_file, \
    after_load_region_file, after_load_category_file, \
    after_load_meta_file


# blatantly copied from the minecraft ap world because why not
def load_data_file(*args) -> dict:
    fname = os.path.join("data", *args)

    try:
        filedata = json.loads(pkgutil.get_data(__name__, fname).decode())
    except:
        filedata = []

    return filedata

def convert_to_list(data, property_name: str) -> list:
    if isinstance(data, dict):
        data = data.get(property_name, [])
    return data


class ManualFile:
    filename: str
    data_type: dict|list
    
    def __init__(self, filename, data_type):
        self.filename = filename
        self.data_type = data_type

    def load(self):
        contents = load_data_file(self.filename)
        
        if not contents and type(contents) != self.data_type:
            return self.data_type()
        
        return contents


game_table = ManualFile('game.json', dict).load() #dict
item_table = [
    item 
    for file in [
        'items.json',
        'crash1/items.json',
        'crash2/items.json',
        'crash3/items.json',
        'nst1/items.json',
        'nst2/items.json',
        'nst3/items.json',
        'spyro1/items.json',
        'spyro2/items.json',
        'spyro3/items.json'
    ] 
    for item in convert_to_list(ManualFile(file, list).load(), 'data')
] #list
location_table = [
    item 
    for file in [
        'locations.json',
        'crash1/locations.json',
        'crash2/locations.json',
        'crash3/locations.json',
        'nst1/locations.json',
        'nst2/locations.json',
        'nst3/locations.json',
        'spyro1/locations.json',
        'spyro2/locations.json',
        'spyro3/locations.json'
    ] 
    for item in convert_to_list(ManualFile(file, list).load(), 'data')
] #list
region_table = {
    key: value
    for file in [
        'regions.json',
        'crash1/regions.json',
        'crash2/regions.json',
        'crash3/regions.json',
        'nst1/regions.json',
        'nst2/regions.json',
        'nst3/regions.json',
        'spyro1/regions.json',
        'spyro2/regions.json',
        'spyro3/regions.json'
    ]
    for key, value in ManualFile(file, dict).load().items()
} #dict
category_table = ManualFile('categories.json', dict).load() #dict
meta_table = ManualFile('meta.json', dict).load() #dict

# Removal of schemas in root of tables
region_table.pop('$schema', '')
category_table.pop('$schema', '')

# hooks
game_table = after_load_game_file(game_table)
item_table = after_load_item_file(item_table)
location_table = after_load_location_file(location_table)
region_table = after_load_region_file(region_table)
category_table = after_load_category_file(category_table)
meta_table = after_load_meta_file(meta_table)

# seed all of the tables for validation
DataValidation.game_table = game_table
DataValidation.item_table = item_table
DataValidation.location_table = location_table
DataValidation.region_table = region_table

validation_errors = []

# check that json files are not just invalid json
try: DataValidation.checkForGameBeingInvalidJSON()
except ValidationError as e: validation_errors.append(e)

try: DataValidation.checkForItemsBeingInvalidJSON()
except ValidationError as e: validation_errors.append(e)

try: DataValidation.checkForLocationsBeingInvalidJSON()
except ValidationError as e: validation_errors.append(e)


############
# If there are any validation errors, display all of them at once
############

if len(validation_errors) > 0:
    logging.error("\nValidationError(s): \n\n%s\n\n" % ("\n".join([' - ' + str(validation_error) for validation_error in validation_errors])))
    print("\n\nYou can close this window.\n")
    keeping_terminal_open = input("If you are running from a terminal, press Ctrl-C followed by ENTER to break execution.")
