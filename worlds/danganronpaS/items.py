from __future__ import annotations

import enum
from dataclasses import dataclass
from typing import TYPE_CHECKING, Dict, List

from BaseClasses import Item, ItemClassification

from .data import Present, Character, CharacterRarity, MonoKub, HypeCardType, CraftingMaterialQuality, crafting_materials, CraftedItem, DevModeDungeon
from .options import CharacterGen

if TYPE_CHECKING:
    from .world import DanganronpaSWorld

## data class made to make things easier(tm)
@dataclass
class ItemData:
    classification: ItemClassification
    count: int = 1

class FillerItem(enum.StrEnum):
    MONOCOINS_10 = "10 Monocoins"
    GOLDEN_MONOCOINS_10 = "10 Golden Monocoins"
    USAMI_COINS_10 = "10 Usami Coins"

## The list of items
item_table: dict[str, ItemData] = {
    **{item.value: ItemData(classification = ItemClassification.filler) for item in FillerItem},

    **{item.value: ItemData(classification = ItemClassification.useful) for item in Present},

    **{character.char_name: ItemData(classification = ItemClassification.progression) for character in Character},
    **{f"Progressive {character.char_name} Rarity": ItemData(classification = ItemClassification.progression, count = 4) for character in Character},
    **{f"{character.char_name} (N)": ItemData(classification = ItemClassification.progression) for character in Character},
    **{f"{character.char_name} (R)": ItemData(classification = ItemClassification.progression) for character in Character},
    **{f"{character.char_name} (S)": ItemData(classification = ItemClassification.progression) for character in Character},
    **{f"{character.char_name} (U)": ItemData(classification = ItemClassification.progression) for character in Character},

    **{f"{character.char_name} - {hypecard}": ItemData(classification = ItemClassification.progression_skip_balancing) for character in Character for hypecard in HypeCardType},
    **{f"{character.char_name}'s Hope Fragment": ItemData(classification = ItemClassification.progression_skip_balancing) for character in Character},
    **{f"{monokub.value}'s Hope Fragment": ItemData(classification = ItemClassification.progression) for monokub in MonoKub},

    "Progressive Scroll": ItemData(classification = ItemClassification.progression, count = 5),
    **{f"{dungeon.value} Unlock": ItemData(classification = ItemClassification.progression) for dungeon in DevModeDungeon},

    **{crafted_item.item_name: ItemData(classification = ItemClassification.progression) for crafted_item in CraftedItem},
    **{f"{material.material_name}": ItemData(classification=ItemClassification.progression) for material_type, quality_dict in crafting_materials.items() for quality, material in quality_dict.items()},
}

raw_items: List[str] = [item for item, classification in item_table.items()]



#Stuff left over from before the rewrite (see: trash.py) that I probably don't want to touch without proper guidance.
#This shit is my Sys32, lol
class DanganronpaSItem(Item):
    game = "DanganronpaS"

def get_random_filler_item_name(world: DanganronpaSWorld) -> str:
    presents_and_filler: list[str] = [present.value for present in Present]
    presents_and_filler += [filler.value for filler in FillerItem]
    return world.random.choice(presents_and_filler)

def create_item_with_correct_classification(world: DanganronpaSWorld, name: str) -> DanganronpaSItem:
    return DanganronpaSItem(name, item_table[name].classification, world.item_name_to_id[name], world.player)

def create_all_items(world: DanganronpaSWorld) -> None:
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    print(f"Number of unfilled locations: {number_of_unfilled_locations}")

    print(f"Starting Inventory: {world.precollected_inventory}")
    for starting_item in world.precollected_inventory:
        world.push_precollected(world.create_item(starting_item))

    itempool: list[Item] = []
    filler_item_names: list[str] = [filler.value for filler in FillerItem]
    for name, data in item_table.items():
        num_to_create: int = data.count
        if name in world.precollected_inventory:
            num_to_create -= 1
        if name not in filler_item_names:
            for _ in range(num_to_create):
                itempool.append(world.create_item(name))

    print(f"num_items_placed: {len(itempool)}")

    needed_number_of_filler_items = number_of_unfilled_locations - len(itempool)
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += itempool

def get_character_item_list(world: DanganronpaSWorld) -> None:
    if world.options.character_gen == CharacterGen.option_scattered:
        for character in Character:
            world.character_item_dict[character] = \
            [f"{character.char_name} ({rarity.value})" for rarity in CharacterRarity]

    elif world.options.character_gen == CharacterGen.option_progressive:
        for character in Character:
            world.character_item_dict[character] = [f"Progressive {character.char_name} Rarity"]

    else:
        for character in Character:
            world.character_item_dict[character] = [f"{character.char_name}"]