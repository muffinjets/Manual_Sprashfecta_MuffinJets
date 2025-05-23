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


# Load base tables
game_table = ManualFile('game.json', dict).load() #dict
item_table = convert_to_list(ManualFile('items.json', list).load(), 'data') #list
location_table = convert_to_list(ManualFile('locations.json', list).load(), 'data') #list
region_table = ManualFile('regions.json', dict).load() #dict
category_table = ManualFile('categories.json', dict).load() #dict
meta_table = ManualFile('meta.json', dict).load() #dict

# Load Crash 1 data
crash1_items = convert_to_list(ManualFile('data/crash1/items.json', list).load(), 'data')
crash1_locations = convert_to_list(ManualFile('data/crash1/locations.json', list).load(), 'data')
crash1_regions = ManualFile('data/crash1/regions.json', dict).load()
item_table.extend(crash1_items)
location_table.extend(crash1_locations)
region_table.update(crash1_regions)

# Load Crash 2 data
crash2_items = convert_to_list(ManualFile('data/crash2/items.json', list).load(), 'data')
crash2_locations = convert_to_list(ManualFile('data/crash2/locations.json', list).load(), 'data')
crash2_regions = ManualFile('data/crash2/regions.json', dict).load()
item_table.extend(crash2_items)
location_table.extend(crash2_locations)
region_table.update(crash2_regions)

# Load Crash 3 data
crash3_items = convert_to_list(ManualFile('data/crash3/items.json', list).load(), 'data')
crash3_locations = convert_to_list(ManualFile('data/crash3/locations.json', list).load(), 'data')
crash3_regions = ManualFile('data/crash3/regions.json', dict).load()
item_table.extend(crash3_items)
location_table.extend(crash3_locations)
region_table.update(crash3_regions)

# Load NST 1 data
nst1_items = convert_to_list(ManualFile('data/nst1/items.json', list).load(), 'data')
nst1_locations = convert_to_list(ManualFile('data/nst1/locations.json', list).load(), 'data')
nst1_regions = ManualFile('data/nst1/regions.json', dict).load()
item_table.extend(nst1_items)
location_table.extend(nst1_locations)
region_table.update(nst1_regions)

# Load NST 2 data
nst2_items = convert_to_list(ManualFile('data/nst2/items.json', list).load(), 'data')
nst2_locations = convert_to_list(ManualFile('data/nst2/locations.json', list).load(), 'data')
nst2_regions = ManualFile('data/nst2/regions.json', dict).load()
item_table.extend(nst2_items)
location_table.extend(nst2_locations)
region_table.update(nst2_regions)

# Load NST 3 data
nst3_items = convert_to_list(ManualFile('data/nst3/items.json', list).load(), 'data')
nst3_locations = convert_to_list(ManualFile('data/nst3/locations.json', list).load(), 'data')
nst3_regions = ManualFile('data/nst3/regions.json', dict).load()
item_table.extend(nst3_items)
location_table.extend(nst3_locations)
region_table.update(nst3_regions)

# Load Spyro 1 data
spyro1_items = convert_to_list(ManualFile('data/spyro1/items.json', list).load(), 'data')
spyro1_locations = convert_to_list(ManualFile('data/spyro1/locations.json', list).load(), 'data')
spyro1_regions = ManualFile('data/spyro1/regions.json', dict).load()
item_table.extend(spyro1_items)
location_table.extend(spyro1_locations)
region_table.update(spyro1_regions)

# Load Spyro 2 data
spyro2_items = convert_to_list(ManualFile('data/spyro2/items.json', list).load(), 'data')
spyro2_locations = convert_to_list(ManualFile('data/spyro2/locations.json', list).load(), 'data')
spyro2_regions = ManualFile('data/spyro2/regions.json', dict).load()
item_table.extend(spyro2_items)
location_table.extend(spyro2_locations)
region_table.update(spyro2_regions)

# Load Spyro 3 data
spyro3_items = convert_to_list(ManualFile('data/spyro3/items.json', list).load(), 'data')
spyro3_locations = convert_to_list(ManualFile('data/spyro3/locations.json', list).load(), 'data')
spyro3_regions = ManualFile('data/spyro3/regions.json', dict).load()
item_table.extend(spyro3_items)
location_table.extend(spyro3_locations)
region_table.update(spyro3_regions)

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
