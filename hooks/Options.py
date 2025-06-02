# Object classes from AP that represent different types of options that you can create
from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value



####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class TotalCharactersToWinWith(Range):
    """Instead of having to beat the game with all characters, you can limit locations to a subset of character victory locations."""
    display_name = "Number of characters to beat the game with before victory"
    range_start = 10
    range_end = 50
    default = 50

class Crash1Choice(Toggle):
    """
    Enable this setting to include Crash Bandicoot items and locations.
    This implementation is compatible with the N. Sane Trilogy, but none of the content from the remake is considered unless you enable the NST Content option below.
    """
    display_name = "Crash_1"
    default = False

class Crash2Choice(Toggle):
    """
    Enable this setting to include Crash Bandicoot 2: Cortex Strikes Back items and locations.
    This implementation is compatible with the N. Sane Trilogy, but none of the content from the remake is considered unless you enable the NST Content option below.
    """
    display_name = "Crash_2"
    default = False
    
class Crash3Choice(Toggle):
    """
    Enable this setting to include Crash Bandicoot: Warped items and locations.
    This implementation is compatible with the N. Sane Trilogy, but none of the content from the remake is considered unless you enable the NST Content option below.
    """
    display_name = "Crash_3"
    default = False

class CrashNSTContentChoice(Toggle):
    """
    Enable this setting to include the content added from the N. Sane Trilogy in all selected Crash games.
    """
    display_name = "Crash_NST_Content"
    default = False

class Spyro1Choice(TextChoice):
    """
    Enable this setting to include Spyro the Dragon items and locations.
     - PS1: This option is only compatible with the PS1 version of Spyro the Dragon.  
            Levels are unlocked via items of the same name.  Hub worlds are unlocked explicitly.  
            Requires the use of the in-game cheat code that doesn't exist in the Reignited Trilogy.

     - SRT: Intended to be played in the Reignited Trilogy version of Spyro the Dragon.
            Hub worlds are unlocked via an incrementally larger amount of "Progressive Homeworld" items.
            This option can be used on the PS1 version if you prefer this playstyle.
    """
    display_name = "Spyro_1"
    option_ps1 = "PS1"
    option_srt = "SRT"
    default = False

class Spyro2Choice(Toggle):
    """
    Enable this setting to include Spyro 2: Ripto's Rage!/Gateway to Glimmer items and locations.
    This implementation is compatible with the Spyro: Reignited Trilogy version of Spyro 2.
    """
    display_name = "Spyro_2"
    default = False

class Spyro3Choice(Toggle):
    """
    Enable this setting to include Spyro: Year of the Dragon items and locations.
    This implementation is compatible with the Spyro: Reignited Trilogy version of Spyro 3.
    """
    display_name = "Spyro_3"
    default = False

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    options["crash1"] = Crash1Choice
    options["crash2"] = Crash2Choice
    options["crash3"] = Crash3Choice
    options["crashnstcontent"] = CrashNSTContentChoice
    options["spyro1"] = Spyro1Choice
    options["spyro2"] = Spyro2Choice
    options["spyro3"] = Spyro3Choice
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:
    return options