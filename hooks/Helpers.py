from typing import Optional
from BaseClasses import MultiWorld
from ..Locations import ManualLocation
from ..Items import ManualItem


def get_option_value(multiworld: MultiWorld, player: int, option_name: str) -> bool:
    """Get the value of a game option."""
    return getattr(multiworld, option_name)[player].value

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the item, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item: ManualItem) -> Optional[bool]:
    if not item:
        return None

    # Check Crash 1 items
    if item.name.lower().startswith('crash1'):
        return get_option_value(multiworld, player, 'Crash_1')

    # Check Crash 1 NST items
    if item.name.lower().startswith('nst1'):
        return get_option_value(multiworld, player, 'Crash_1')

    # Check Crash 2 items
    if item.name.lower().startswith('crash2'):
        return get_option_value(multiworld, player, 'Crash_2')

    # Check Crash 2 NST items
    if item.name.lower().startswith('nst2'):
        return get_option_value(multiworld, player, 'Crash_2')

    # Check Crash 3 items
    if item.name.lower().startswith('crash3'):
        return get_option_value(multiworld, player, 'Crash_3')

    # Check Crash 3 NST items
    if item.name.lower().startswith('nst3'):
        return get_option_value(multiworld, player, 'Crash_3')

    # Check Spyro 1 items
    if item.name.lower().startswith('spyro1'):
        return get_option_value(multiworld, player, 'Spyro_1')

    # Check Spyro 2 items
    if item.name.lower().startswith('spyro2'):
        return get_option_value(multiworld, player, 'Spyro_2')

    # Check Spyro 3 items
    if item.name.lower().startswith('spyro3'):
        return get_option_value(multiworld, player, 'Spyro_3')

    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location: ManualLocation) -> Optional[bool]:
    if not location:
        return None

    # Check Crash 1 locations
    if location.name.lower().startswith('crash1'):
        return get_option_value(multiworld, player, 'Crash_1')
    if hasattr(location, 'parent_region') and location.parent_region and location.parent_region.name.lower().startswith('crash1'):
        return get_option_value(multiworld, player, 'Crash_1')

    # Check Crash 1 NST locations
    if location.name.lower().startswith('nst1'):
        return get_option_value(multiworld, player, 'Crash_1')
    if hasattr(location, 'parent_region') and location.parent_region and location.parent_region.name.lower().startswith('nst1'):
        return get_option_value(multiworld, player, 'Crash_1')

    # Check Crash 2 locations
    if location.name.lower().startswith('crash2'):
        return get_option_value(multiworld, player, 'Crash_2')
    if hasattr(location, 'parent_region') and location.parent_region and location.parent_region.name.lower().startswith('crash2'):
        return get_option_value(multiworld, player, 'Crash_2')

    # Check Crash 2 NST locations
    if location.name.lower().startswith('nst2'):
        return get_option_value(multiworld, player, 'Crash_2')
    if hasattr(location, 'parent_region') and location.parent_region and location.parent_region.name.lower().startswith('nst2'):
        return get_option_value(multiworld, player, 'Crash_2')

    # Check Crash 3 locations
    if location.name.lower().startswith('crash3'):
        return get_option_value(multiworld, player, 'Crash_3')
    if hasattr(location, 'parent_region') and location.parent_region and location.parent_region.name.lower().startswith('crash3'):
        return get_option_value(multiworld, player, 'Crash_3')

    # Check Crash 3 NST locations
    if location.name.lower().startswith('nst3'):
        return get_option_value(multiworld, player, 'Crash_3')
    if hasattr(location, 'parent_region') and location.parent_region and location.parent_region.name.lower().startswith('nst3'):
        return get_option_value(multiworld, player, 'Crash_3')

    # Check Spyro 1 locations
    if location.name.lower().startswith('spyro1'):
        return get_option_value(multiworld, player, 'Spyro_1')
    if hasattr(location, 'parent_region') and location.parent_region and location.parent_region.name.lower().startswith('spyro1'):
        return get_option_value(multiworld, player, 'Spyro_1')

    # Check Spyro 2 locations
    if location.name.lower().startswith('spyro2'):
        return get_option_value(multiworld, player, 'Spyro_2')
    if hasattr(location, 'parent_region') and location.parent_region and location.parent_region.name.lower().startswith('spyro2'):
        return get_option_value(multiworld, player, 'Spyro_2')

    # Check Spyro 3 locations
    if location.name.lower().startswith('spyro3'):
        return get_option_value(multiworld, player, 'Spyro_3')
    if hasattr(location, 'parent_region') and location.parent_region and location.parent_region.name.lower().startswith('spyro3'):
        return get_option_value(multiworld, player, 'Spyro_3')

    return None
