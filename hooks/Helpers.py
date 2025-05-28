from typing import Optional
from BaseClasses import MultiWorld
from ..Locations import ManualLocation
from ..Items import ManualItem

# Flag to track if we've printed the options
_options_printed = False

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    global _options_printed
    # Get game options from the multiworld
    crash_1_enabled = multiworld.Crash_1[player].value
    crash_2_enabled = multiworld.Crash_2[player].value
    crash_3_enabled = multiworld.Crash_3[player].value
    crash_nst_enabled = multiworld.Crash_NST_Content[player].value
    spyro_1_enabled = multiworld.Spyro_1[player].value
    spyro_2_enabled = multiworld.Spyro_2[player].value
    spyro_3_enabled = multiworld.Spyro_3[player].value

    # Print selected options only once
    if not _options_printed:
        print(f"\nSelected YAML Options for Player {player}:")
        print(f"Crash 1: {crash_1_enabled}")
        print(f"Crash 2: {crash_2_enabled}")
        print(f"Crash 3: {crash_3_enabled}")
        print(f"Crash NST Content: {crash_nst_enabled}")
        print(f"Spyro 1: {spyro_1_enabled}")
        print(f"Spyro 2: {spyro_2_enabled}")
        print(f"Spyro 3: {spyro_3_enabled}\n")
        _options_printed = True

    # Check if NST content should be enabled (only if at least one Crash game is enabled)
    crash_nst_enabled = crash_nst_enabled and (crash_1_enabled or crash_2_enabled or crash_3_enabled)

    # Check if the category belongs to an enabled game
    if category_name == "Crash 1":
        return crash_1_enabled
    elif category_name == "Crash 2":
        return crash_2_enabled
    elif category_name == "Crash 3":
        return crash_3_enabled
    elif category_name == "Crash NST Content":
        return crash_nst_enabled
    elif category_name == "Spyro 1":
        return spyro_1_enabled
    elif category_name == "Spyro 2":
        return spyro_2_enabled
    elif category_name == "Spyro 3":
        return spyro_3_enabled
    
    return True

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the item, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item: ManualItem) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location: ManualLocation) -> Optional[bool]:
    return None