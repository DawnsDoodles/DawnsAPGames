from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle


class Goal(Choice):
    """
    What is required to beat the game
    School Secret: Beat the Jabberwock Boss in Hope's Peak Academy
    Arena of Despair: Complete the Arena of Despair by beating the Jabberwock Boss there.
    Hope Fragments: Collect a certain amount of hope fragments.
    """
    display_name = "Goal"
    option_school_secret = 0
    option_arena_of_despair = 1
    option_hope_fragments = 2
    default = 0

class FragmentCount(Range):
    """How many Hope Fragments you need to collect for a Hope Fragment goal?"""
    display_name = "Fragments"
    range_start = 1
    range_end = 67
    default = 62

class CharacterGen(Choice):
    """
    How do you want the characters to generate?
    All at once: Each character has 1 item, you get all 4 rarities
    Progressive: Each character has 4 items that increase the rarity of that character
    Scattered: Fuck it, every character card can be anywhere.
    """
    display_name = "Character Generation"
    option_all_at_once = 0
    option_progressive = 1
    ##option_scattered = 2
    default = 0

class UsamiFlowers(Toggle):
    """Usami Flowers are achievements in the game that can
    cause the game to become pretty grindy, during development
    of this AP, one of the people helping me suggested that
    I keep this as a YAML option because some of what you
    need to do can be pretty arduous."""
    display_name = "Usami Flowers"
    default = False

@dataclass
class DRASOptions(PerGameCommonOptions):
    goal: Goal
    fragments: FragmentCount
    character_gen: CharacterGen
    usami_flowers: UsamiFlowers