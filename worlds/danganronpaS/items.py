from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Dict, List

from BaseClasses import Item, ItemClassification

from .data import characters, monokubs, hypecards, ingredientlevels, crafted_items, presents, filler, dev_mode_dungeons, scrolls
from .options import CharacterGen

if TYPE_CHECKING:
    from .world import DanganronpaSWorld

## data class made to make things easier(tm)
@dataclass
class ItemData:
    classification: ItemClassification
    count: int = 1

## The list of items
item_table: dict[str, ItemData] = {
    **{item: ItemData(classification = ItemClassification.filler) for item in filler},

    **{item: ItemData(classification = ItemClassification.useful) for item in presents},

    **{item: ItemData(classification = ItemClassification.progression) for item in characters},
    **{f"Progressive {character} Rarity": ItemData(classification = ItemClassification.progression, count = 4) for character in characters},
    **{f"{character} (N)": ItemData(classification = ItemClassification.progression) for character in characters},
    **{f"{character} (R)": ItemData(classification = ItemClassification.progression) for character in characters},
    **{f"{character} (S)": ItemData(classification = ItemClassification.progression) for character in characters},
    **{f"{character} (U)": ItemData(classification = ItemClassification.progression) for character in characters},

    **{f"{character} - {hypecard}": ItemData(classification = ItemClassification.progression_skip_balancing) for character in characters for hypecard in hypecards},
    **{f"{character}'s Hope Fragment": ItemData(classification = ItemClassification.progression) for character in characters},
    **{f"{monokub}'s Hope Fragment": ItemData(classification = ItemClassification.progression) for monokub in monokubs},

    "Progressive Scroll": ItemData(classification = ItemClassification.progression, count = 5),
    **{f"{item} Unlock": ItemData(classification = ItemClassification.progression) for item in dev_mode_dungeons},

    **{item: ItemData(classification = ItemClassification.progression) for item in crafted_items},
    **{f"{item} Monster Eye": ItemData(classification = ItemClassification.progression) for item in ingredientlevels},
    **{f"{item} Monster Fang": ItemData(classification = ItemClassification.progression) for item in ingredientlevels},
    **{f"{item} Monster Fur": ItemData(classification = ItemClassification.progression) for item in ingredientlevels},
    **{f"{item} Monster Meat": ItemData(classification = ItemClassification.progression) for item in ingredientlevels},
    **{f"{item} Monster Skin": ItemData(classification = ItemClassification.progression) for item in ingredientlevels},
}

raw_items: List[str] = [item for item, classification in item_table.items()]



#Stuff left over from before the rewrite (see: trash.py) that I probably don't want to touch without proper guidance.
#This shit is my Sys32, lol
class DanganronpaSItem(Item):
    game = "DanganronpaS"

def get_random_filler_item_name(world: DanganronpaSWorld) -> str:
    return world.random.choice([*presents, *filler])

def create_item_with_correct_classification(world: DanganronpaSWorld, name: str) -> DanganronpaSItem:
    return DanganronpaSItem(name, item_table[name].classification, world.item_name_to_id[name], world.player)

def create_all_items(world: DanganronpaSWorld) -> None:
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    print(f"Number of unfilled locations: {number_of_unfilled_locations}")

    print(f"Starting Inventory: {world.precollected_inventory}")
    for starting_item in world.precollected_inventory:
        world.push_precollected(world.create_item(starting_item))

    itempool: list[Item] = []
    for name, data in item_table.items():
        if name not in filler and name not in world.precollected_inventory:
            for _ in range(data.count):
                itempool.append(world.create_item(name))

    print(f"num_items_placed: {len(itempool)}")

    needed_number_of_filler_items = number_of_unfilled_locations - len(itempool)
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += itempool

def get_character_item_list(world: DanganronpaSWorld) -> None:
    if world.options.character_gen == CharacterGen.option_scattered:
        for character in characters:
            world.character_item_list.append(f"{character} (N)")
            world.character_item_list.append(f"{character} (R)")
            world.character_item_list.append(f"{character} (S)")
            world.character_item_list.append(f"{character} (U)")
    elif world.options.character_gen == CharacterGen.option_progressive:
        for character in characters:
            world.character_item_list.append(f"Progressive {character} Rarity")
    else:
        for character in characters:
            world.character_item_list.append(f"{character}")