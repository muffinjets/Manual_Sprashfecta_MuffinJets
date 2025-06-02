from typing import Optional
from BaseClasses import MultiWorld
from ..Locations import ManualLocation
from ..Items import ManualItem

# Flag to track if we've printed the options
_options_printed = False
_nst_item_debug = False
_nst_location_debug = False

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    # global _options_printed
    # # Get game options from the multiworld
    # crash_1_enabled = multiworld.Crash_1[player].value
    # crash_2_enabled = multiworld.Crash_2[player].value
    # crash_3_enabled = multiworld.Crash_3[player].value
    # crash_nst_enabled = multiworld.Crash_NST_Content[player].value
    # spyro_1_enabled = multiworld.Spyro_1[player].value
    # spyro_2_enabled = multiworld.Spyro_2[player].value
    # spyro_3_enabled = multiworld.Spyro_3[player].value

    # # Print selected options only once
    # if not _options_printed:
    #     print(f"\nSelected YAML Options for Player {player}:")
    #     print(f"Crash 1: {crash_1_enabled}")
    #     print(f"Crash 2: {crash_2_enabled}")
    #     print(f"Crash 3: {crash_3_enabled}")
    #     print(f"Crash NST Content: {crash_nst_enabled}")
    #     print(f"Spyro 1: {spyro_1_enabled}")
    #     print(f"Spyro 2: {spyro_2_enabled}")
    #     print(f"Spyro 3: {spyro_3_enabled}\n")
    #     _options_printed = True

    # # Check if NST content should be enabled (only if at least one Crash game is enabled)
    # crash_nst_enabled = crash_nst_enabled and (crash_1_enabled or crash_2_enabled or crash_3_enabled)

    # # Check if the category belongs to an enabled game
    # if category_name == "Crash 1":
    #     return crash_1_enabled
    # elif category_name == "Crash 2":
    #     return crash_2_enabled
    # elif category_name == "Crash 3":
    #     return crash_3_enabled
    # elif category_name == "Crash NST Content":
    #     return crash_nst_enabled
    # elif category_name == "Spyro 1":
    #     return spyro_1_enabled
    # elif category_name == "Spyro 2":
    #     return spyro_2_enabled
    # elif category_name == "Spyro 3":
    #     return spyro_3_enabled
    
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the item, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item: ManualItem) -> Optional[bool]:
    
    options = multiworld.worlds[player].options
    global _nst_item_debug


    # Scan through the entire loaded item list.  If <game> is not enabled, remove the item from consideration.

    # "if Crash 1 is not enabled and the item being considered has Crash 1 in the category, remove that item."
    if not options.crash1 and "Crash 1" in item["category"]:
        return False
    # "if Crash 2 is not enabled and the item being considered has Crash 2 in the category, remove that item."
    elif not options.crash2 and "Crash 2" in item["category"]:
        return False
    # "if Crash 3 is not enabled and the item being considered has Crash 3 in the category, remove that item."
    elif not options.crash3 and "Crash 3" in item["category"]:
        return False
    # "if Crash NST Content is not enabled and the item being considered has Crash NST Content in the category, remove that item."
    elif not options.crashnstcontent and "Crash NST Content" in item["category"]:
        return False
    # "if the NST option is turned on and a Crash game is not selected, and the item has NST in the category, remove that item."
    elif options.crashnstcontent and not (options.crash1 or options.crash2 or options.crash3) and "Crash NST Content" in item["category"]:
        if not _nst_item_debug:
            _nst_item_debug = True
            print("NST selected with no Crash game also selected! Removed NST items.")
        return False
    
    elif options.spyro1 == "PS1":   # If PS1 is selected...
        if "SRT 1" in item["category"]:    # ... and if the item has SRT 1 in the category...
            return False                   # ... then remove the item.
    elif options.spyro1 == "SRT":   # If SRT is selected...
        if "SRT 1" not in item["category"]:# ... and if SRT 1 is not one of its categories...
            return False                   # ... then remove the item.
    elif options.spyro1 == False:   # If Spyro 1 is set to False...
        if "Spyro 1" in item["category"]:  # ... and if the item has Spyro 1 as one of it's categories...
            return False                   # ... remove the item.

    # "if Spyro 2 is not enabled and the item being considered has Spyro 2 in the category, remove that item."
    elif not options.spyro2 and "Spyro 2" in item["category"]:
        return False
    # "if Spyro 3 is not enabled and the item being considered has Spyro 3 in the category, remove that item."
    elif not options.spyro3 and "Spyro 3" in item["category"]:
        return False
    # if all else fails, return None to use the default behavior
    return None


# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location: ManualLocation) -> Optional[bool]:
    options = multiworld.worlds[player].options
    global _nst_location_debug

    # Scan through the entire loaded location list. If <game> is not enabled, remove the location from consideration.

    # "if Crash 1 is not enabled and the location being considered has Crash 1 in the category, remove that location."
    if not options.crash1 and "Crash 1" in location["category"]:
        return False
    # "if Crash 2 is not enabled and the location being considered has Crash 2 in the category, remove that location."
    elif not options.crash2 and "Crash 2" in location["category"]:
        return False
    # "if Crash 3 is not enabled and the location being considered has Crash 3 in the category, remove that location."
    elif not options.crash3 and "Crash 3" in location["category"]:
        return False
    # "if Crash NST Content is not enabled and the location being considered has Crash NST Content in the category, remove that location."
    elif not options.crashnstcontent and "Crash NST Content" in location["category"]:
        return False
    # "if the NST option is turned on and a Crash game is not selected, and the location has NST in the category, remove that location."
    elif options.crashnstcontent and not (options.crash1 or options.crash2 or options.crash3) and "Crash NST Content" in location["category"]:
        if not _nst_location_debug:
            _nst_location_debug = True
            print("NST selected with no Crash game also selected! Removed NST locations.")
        return False
    
    elif options.spyro1 == "PS1":   # If PS1 is selected...
        if "SRT 1" in location["category"]:    # ... and if the location has SRT 1 in the category...
            return False                   # ... then remove the location.
    elif options.spyro1 == "SRT":   # If SRT is selected...
        if "SRT 1" not in location["category"]:# ... and if SRT 1 is not one of its categories...
            return False                   # ... then remove the location.
    elif options.spyro1 == False:   # If Spyro 1 is set to False...
        if "Spyro 1" in location["category"]:  # ... and if the location has Spyro 1 as one of it's categories...
            return False                   # ... remove the location.

    # "if Spyro 2 is not enabled and the location being considered has Spyro 2 in the category, remove that location."
    elif not options.spyro2 and "Spyro 2" in location["category"]:
        return False
    # "if Spyro 3 is not enabled and the location being considered has Spyro 3 in the category, remove that location."
    elif not options.spyro3 and "Spyro 3" in location["category"]:
        return False
    # if all else fails, return None to use the default behavior
    return None