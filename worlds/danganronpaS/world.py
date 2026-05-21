from collections.abc import Mapping
from typing import Any, Optional

from BaseClasses import MultiWorld
from worlds.AutoWorld import World
from .constants import DANGANRONPA_S

from . import data, items, locations, options, regions, rules, web_world, goals


class DanganronpaSWorld(World):
    """
    Danganronpa S is a game.
    """

    game = DANGANRONPA_S
    web = web_world.DanganronpaSWebWorld()

    options_dataclass = options.DRASOptions
    options: options.DRASOptions

    location_name_to_id = {loc_name: loc_id for loc_name, loc_id in locations.location_dictionary.items()}
    item_name_to_id = {value: index + 1 for index, value in enumerate(items.raw_items)}

    #constructor for World class
    def __init__(self, multiworld: MultiWorld, player: int) -> None:
        # put instance unique things here (to prevent global state bleed)
        # make sure that any editable things that the world reads is initialized here
        self.num_starting_characters: int = 5
        self.starting_characters: list[data.Character] = []
        self.character_item_dict: dict[data.Character, list[str]] = {}

        self.is_ut_gen: bool = False
        """Is this a UT gen?"""
        self.precollected_inventory: list[str] = []
        """Starting Inventory (list of item names)"""
        super().__init__(multiworld, player)

    def handle_ut_yamlless(self, slot_data: Optional[dict[str, Any]]) -> Optional[dict[str, Any]]:
        if not slot_data \
                and hasattr(self.multiworld, "re_gen_passthrough") \
                and isinstance(self.multiworld.re_gen_passthrough, dict) \
                and self.game in self.multiworld.re_gen_passthrough:
            slot_data = self.multiworld.re_gen_passthrough[self.game]
        if not slot_data:
            return None
        # we are now in a UT gen, set any options and other randomization to slot data
        self.is_ut_gen = True

        self.starting_characters = []
        for character in data.Character:
            if character.char_name in slot_data["starting_characters"]:
                self.starting_characters.append(character)

        return slot_data


    def create_item(self, name: str) -> items.DanganronpaSItem:
        return items.create_item_with_correct_classification(self, name)
    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    #done first (options exist here)
    #check valid options and do stuff here
    def generate_early(self) -> None:
        #UT support here
        self.handle_ut_yamlless(None)

        items.get_character_item_list(self)

        if not self.is_ut_gen:
            #starting characters
            self.starting_characters = self.random.sample(list(self.character_item_dict.keys()), self.num_starting_characters)
            match self.options.character_gen.value:
                case options.CharacterGen.option_all_at_once:
                    for x in range(self.num_starting_characters):
                        self.precollected_inventory.append(self.character_item_dict[self.starting_characters[x]][0])
                case options.CharacterGen.option_progressive:
                    for x in range(self.num_starting_characters):
                        self.precollected_inventory.append(self.character_item_dict[self.starting_characters[x]][0])
                case options.CharacterGen.option_scattered:
                    for x in range(self.num_starting_characters):
                        #will pull specifically Normal Rarity
                        self.precollected_inventory.append(self.character_item_dict[self.starting_characters[x]][0])

    #second is regions (and locations)
    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_locations(self)

    #after regions is items (locations are done, though events can be later)
    def create_items(self) -> None:
        items.create_all_items(self)

    #after items is rules (items are done at this point, events can be later)
    def set_rules(self) -> None:
        rules.create_rules(self)
        goals.set_goal(self)

    #after rules is connect_entrances (this is prob not needed except for GER)
    # rules / connections should be done at the end of this function
    def connect_entrances(self) -> None:
        pass

    #fill happens here pre_fill, fill_hook

    def pre_fill(self) -> None:
        pass


    # run after regular fill (but before progression balancing)
    # if you are erroring in generation, then make a PUML here if needed
    def post_fill(self) -> None:
        # self.make_puml(True)
        pass


    # There may be data that the game client will need to modify the behavior of the game.
    # This is what slot_data exists for. Upon every client connection, the slot's slot_data is sent to the client.
    # slot_data is just a dictionary using basic types, that will be converted to json when sent to the client.
    def fill_slot_data(self) -> Mapping[str, Any]:
        self.make_puml(True)
        # If you need access to the player's chosen options on the client side, there is a helper for that.
        return \
        {
            "starting_characters": [char.char_name for char in self.starting_characters],
            "goal": self.options.goal.value,
            "fragments": self.options.fragments.value,
        }

    def make_puml(self, highlight_unreachable: bool = True):
        print("MAKE PUML HERE")
        from Utils import visualize_regions
        state = self.multiworld.get_all_state()
        state.update_reachable_regions(self.player)

        reachable_regions = state.reachable_regions[self.player]
        unreachable_regions: set[Region] = set()  # type: ignore
        for region in self.multiworld.regions:
            if region not in reachable_regions:
                unreachable_regions.add(region)

        if highlight_unreachable:
            visualize_regions(self.get_region("Menu"), f"{self.player_name}_world.puml", show_entrance_names=True, regions_to_highlight=unreachable_regions)

        else:
            visualize_regions(self.get_region("Menu"), f"{self.player_name}_world.puml", show_entrance_names=True, regions_to_highlight=reachable_regions)
