from __future__ import annotations

import math
from dataclasses import dataclass
from typing import TYPE_CHECKING
from rule_builder.rules import *

from BaseClasses import CollectionState, Region
from .items import item_table
from .data import Character, HypeCardType
from worlds.generic.Rules import add_rule, set_rule
from .options import *
from .AtLeast import AtLeast

if TYPE_CHECKING:
    from .world import DanganronpaSWorld


## Master Code B)
def create_rules(world: DanganronpaSWorld):
    create_entrance_rules(world)

@dataclass
class HasCharacters(Rule["DanganronpaSWorld"], game = "DanganronpaS"):
    number: int
    @override
    def resolve(self, world: DanganronpaSWorld) -> Rule.Resolved:
        return HasFromListUnique(*world.character_item_list, count = self.number).resolve(world)

@dataclass
class CheckCharacter(Rule["DanganronpaSWorld"], game = "DanganronpaS"):
    character: str
    @override
    def resolve(self, world: DanganronpaSWorld) -> Rule.Resolved:
        item_list: list[str] = get_items_for_character(world, self.character)

@dataclass
class HasMaxHype(Rule["DanganronpaSWorld"], game = "DanganronpaS"):
    character: str
    @override
    def resolve(self, world: DanganronpaSWorld) -> Rule.Resolved:
        hype_card_items = [f"{self.character} - {hypecard}" for hypecard in hypecards]
        return HasAll(*hype_card_items).resolve(world)

def get_items_for_character(world: DanganronpaSWorld, character: Character) -> list[str]:
    if world.options.character_gen == CharacterGen.option_all_at_once:
        return [f"{character}"]
    elif world.options.character_gen == CharacterGen.option_progressive:
        return [f"Progressive {character} Rarity"]
    else:
        return [f"{character} ({rarity})" for rarity in ['N', 'R', 'S', 'U']]




## Individual Entrance Rules
def create_entrance_rules(world: DanganronpaSWorld):

    #EXAMPLE:
    #entrance1, entrance2 = get_entrances(world.get_region(""), world.get_region(""))
    #rule = (HasAll = And) (HasAny = Or)
    #world.set_rule(entrance1)
    #world.set_rule(entrance2)

    entrance1, entrance2 = get_entrances(world, world.get_region("Battle Tower Lower Floor"), world.get_region("Battle Tower Upper Floor"))
    rule = HasCharacters(10)
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    entrance1, entrance2 = get_entrances(world, world.get_region("Battle Tower Upper Floor"), world.get_region("Battle Tower Lower Ultimate Floor"))
    rule = HasCharacters(20)
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    entrance1, entrance2 = get_entrances(world, world.get_region("Battle Tower Upper Floor"), world.get_region("Arena of Despair"))
    rule = HasCharacters(20)
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    entrance1, entrance2 = get_entrances(world, world.get_region("Battle Tower Lower Ultimate Floor"), world.get_region("Battle Tower Upper Ultimate Floor"))
    rule = HasCharacters(30)
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    entrance1, entrance2 = get_entrances(world, world.get_region("The First Island"), world.get_region("The Second Island"))
    rule = Has ("Progressive Scroll", count = 1)
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    entrance1, entrance2 = get_entrances(world, world.get_region("The Second Island"), world.get_region("The Third Island"))
    rule = Has ("Progressive Scroll", count = 2)
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    entrance1, entrance2 = get_entrances(world, world.get_region("The Third Island"), world.get_region("The Fourth Island"))
    rule = Has ("Progressive Scroll", count = 3)
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    entrance1, entrance2 = get_entrances(world, world.get_region("The Fourth Island"), world.get_region("The Fifth Island"))
    rule = Has ("Progressive Scroll", count = 4)
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    entrance1, entrance2 = get_entrances(world, world.get_region("The First Island"), world.get_region("Cottage"))
    rule = Has ("Cottage Unlock")
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    entrance1, entrance2 = get_entrances(world, world.get_region("The Second Island"), world.get_region("Beach House"))
    rule = Has ("Progressive Scroll", count = 1) & Has ("Beach House Unlock")
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    entrance1, entrance2 = get_entrances(world, world.get_region("The Third Island"), world.get_region("Hospital"))
    rule = Has ("Progressive Scroll", count = 2) & Has ("Hospital Unlock")
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    entrance1, entrance2 = get_entrances(world, world.get_region("The Fourth Island"), world.get_region("Fun House"))
    rule = Has ("Progressive Scroll", count = 3) & Has ("Fun House Unlock")
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    entrance1, entrance2 = get_entrances(world, world.get_region("The Fifth Island"), world.get_region("Factory"))
    rule = Has ("Progressive Scroll", count = 4) & Has ("Factory Unlock")
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    entrance1, entrance2 = get_entrances(world, world.get_region("The Fifth Island"), world.get_region("Hopes Peak"))
    rule = Has ("Progressive Scroll", count = 5)
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    hopefragments = []
    for name in item_table:
        if "Hope Fragment" in name:
            hopefragments.append(name)
    entrance1, entrance2 = get_entrances(world, world.get_region("Menu"), world.get_region("Monokids Hope"))
    rule = HasFromListUnique (*hopefragments, count = 10)
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    hopefragments = []
    for name in item_table:
        if "Hope Fragment" in name:
            hopefragments.append(name)
    entrance1, entrance2 = get_entrances(world, world.get_region("Monokids Hope"), world.get_region("Monossukes Hope"))
    rule = HasFromListUnique (*hopefragments, count = 20)
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    hopefragments = []
    for name in item_table:
        if "Hope Fragment" in name:
            hopefragments.append(name)
    entrance1, entrance2 = get_entrances(world, world.get_region("Monossukes Hope"), world.get_region("Monodams Hope"))
    rule = HasFromListUnique (*hopefragments, count = 30)
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    hopefragments = []
    for name in item_table:
        if "Hope Fragment" in name:
            hopefragments.append(name)
    entrance1, entrance2 = get_entrances(world, world.get_region("Monodams Hope"), world.get_region("Monophanies Hope"))
    rule = HasFromListUnique (*hopefragments, count = 40)
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    hopefragments = []
    for name in item_table:
        if "Hope Fragment" in name:
            hopefragments.append(name)
    entrance1, entrance2 = get_entrances(world, world.get_region("Monophanies Hope"), world.get_region("Monotaros Hope"))
    rule = HasFromListUnique (*hopefragments, count = 50)
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    hopefragments = []
    for name in item_table:
        if "Hope Fragment" in name:
            hopefragments.append(name)
    entrance1, entrance2 = get_entrances(world, world.get_region("Monotaros Hope"), world.get_region("Graduation"))
    rule = HasFromListUnique (*hopefragments, count = 67)
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    entrance1, entrance2 = get_entrances(world, world.get_region("Menu"), world.get_region("Gacha2"))
    rule = HasCharacters(10)
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    entrance1, entrance2 = get_entrances(world, world.get_region("Menu"), world.get_region("Gacha3"))
    rule = HasCharacters(20)
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    entrance1, entrance2 = get_entrances(world, world.get_region("Menu"), world.get_region("Gacha4"))
    rule = HasCharacters(30)
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    entrance1, entrance2 = get_entrances(world, world.get_region("Menu"), world.get_region("Gacha5"))
    rule = HasCharacters(40)
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    entrance1, entrance2 = get_entrances(world, world.get_region("Menu"), world.get_region("Gacha6"))
    rule = Has ("Progressive Scroll", count = 1)
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    entrance1, entrance2 = get_entrances(world, world.get_region("Menu"), world.get_region("Gacha7"))
    rule = Has ("Progressive Scroll", count = 2)
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    entrance1, entrance2 = get_entrances(world, world.get_region("Menu"), world.get_region("Gacha8"))
    rule = Has ("Progressive Scroll", count = 3)
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    entrance1, entrance2 = get_entrances(world, world.get_region("Menu"), world.get_region("Gacha9"))
    rule = Has ("Progressive Scroll", count = 4)
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    entrance1, entrance2 = get_entrances(world, world.get_region("Menu"), world.get_region("Gacha10"))
    rule = Has ("Cottage Unlock")
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    entrance1, entrance2 = get_entrances(world, world.get_region("Menu"), world.get_region("Gacha11"))
    rule = Has ("Progressive Scroll", count = 1) & Has ("Beach House Unlock")
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    entrance1, entrance2 = get_entrances(world, world.get_region("Menu"), world.get_region("Gacha12"))
    rule = Has ("Progressive Scroll", count = 2) & Has ("Hospital Unlock")
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    entrance1, entrance2 = get_entrances(world, world.get_region("Menu"), world.get_region("Gacha13"))
    rule = Has ("Progressive Scroll", count = 3) & Has ("Fun House Unlock")
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)
    
    entrance1, entrance2 = get_entrances(world, world.get_region("Menu"), world.get_region("Gacha14"))
    rule = Has ("Progressive Scroll", count = 4) & Has ("Factory Unlock")
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)

    entrance1, entrance2 = get_entrances(world, world.get_region("Menu"), world.get_region("Gacha15"))
    rule = HasCharacters(50)
    world.set_rule(entrance1, rule)
    world.set_rule(entrance2, rule)


## Rule helper thingy for regions
def get_entrances(world: DanganronpaSWorld, region1: Region, region2: Region):
    entrance1 = world.multiworld.get_entrance(f"{region1.name} => {region2.name}", world.player)
    entrance2 = world.multiworld.get_entrance(f"{region2.name} => {region1.name}", world.player)
    return entrance1, entrance2

##Creating Location Rules
def create_location_rules(world: DanganronpaSWorld):

    ##EXAMPLE
    ##location = world.multiworld.get_location("name")
    ##rule = ##logic##
    ##world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Army Knife", world.player)
    rule = Has("Gold Monster Fang")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Crossbow", world.player)
    rule = Has("Gold Monster Fur")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Dumbbell", world.player)
    rule = Has("Copper Monster Meat")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Gold Leaf Katana", world.player)
    rule = Has("Silver Monster Fur")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Hacking Gun", world.player)
    rule = HasAll("Small Monster Fang", "Monster Fang")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Hacking Gun Extreme", world.player)
    rule = HasAll("Big Monster Fang", "Sturdy Monster Fang")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Hacking Gun V3", world.player)
    rule = HasAll("Hacking Gun V", "Divine Monster Fang", "Lavish Monster Fang")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Hammer", world.player)
    rule = Has("Silver Monster Fur")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Hat of Hope", world.player)
    rule = Has("Lavish Monster Fur")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Hat of Legend", world.player)
    rule = HasAll("Big Monster Fur", "Sturdy Monster Fur", "Lavish Monster Fur")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Hat of Overflowing Talent", world.player)
    rule = HasAll("Monster Fur", "Big Monster Fur")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Hat V3", world.player)
    rule = HasAll("Ultimate Hat", "Divine Monster Fur")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft High Schooler's Hat", world.player)
    rule = HasAll("Small Monster Fur", "Monster Fur")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft High Schooler's Shoes", world.player)
    rule = HasAll("Small Monster Fur", "Monster Fur")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft High Schooler's Talisman", world.player)
    rule = HasAll("Small Monster Skin", "Monster Skin")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft High Schooler's Uniform", world.player)
    rule = HasAll("Small Monster Skin", "Monster Skin")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Shoes of Legend", world.player)
    rule = HasAll("Big Monster Fur", "Sturdy Monster Fur", "Lavish Monster Fur")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Hydraulic Press", world.player)
    rule = HasAll("Gold Monster Meat", "Gold Monster Skin", "Gold Monster Fur")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Iron Skewer", world.player)
    rule = HasAll("Copper Monster Fang", "Copper Monster Fur")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft JUSTICE HAMMER", world.player)
    rule = Has("Copper Monster Skin")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Katana", world.player)
    rule = HasAll("Small Monster Fang", "Monster Fang")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Katana Extreme", world.player)
    rule = HasAll("Big Monster Fang", "Sturdy Monster Fang")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Katana V3", world.player)
    rule = HasAll("V Katana", "Divine Monster Fang", "Lavish Monster Fang")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Kitchen Knife", world.player)
    rule = Has("Copper Monster Eye")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Metal Bat", world.player)
    rule = Has("Silver Monster Fang")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Monokuma's Special Poison", world.player)
    rule = Has("Gold Monster Fur")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Piranha", world.player)
    rule = Has("Silver Monster Skin")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Poison", world.player)
    rule = Has("Copper Monster Fur")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Replica Sword", world.player)
    rule = Has("Copper Monster Fang")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Rope Used for Hanging", world.player)
    rule = Has("Silver Monster Eye")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Scissors", world.player)
    rule = HasAll("Gold Monster Eye", "Gold Monster Fang", "Gold Monster Meat")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Shield", world.player)
    rule = HasAll("Small Monster Eye", "Monster Eye")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Shield Extreme", world.player)
    rule = HasAll("Big Monster Eye", "Sturdy Monster Eye")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Shield V3", world.player)
    rule = HasAll("V Shield", "Divine Monster Eye", "Lavish Monster Eye")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Shoes of Hope", world.player)
    rule = Has("Lavish Monster Fur")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Shoes of Overflowing Talent", world.player)
    rule = HasAll("Monster Fur", "Big Monster Fur")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Shoes V3", world.player)
    rule = HasAll("Ultimate Shoes", "Divine Monster Fur")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Shot Put Ball", world.player)
    rule = Has("Silver Monster Skin")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Sickle", world.player)
    rule = Has("Gold Monster Meat")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Spears of Gungnir", world.player)
    rule = Has("Gold Monster Eye")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Staff", world.player)
    rule = HasAll("Small Monster Meat", "Monster Meat")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Staff Extreme", world.player)
    rule = HasAll("Big Monster Meat", "Sturdy Monster Meat")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Staff V3", world.player)
    rule = HasAll("V Staff", "Divine Monster Meat", "Lavish Monster Meat")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Super Hacking Gun", world.player)
    rule = HasAll("Small Monster Fang", "Monster Fang")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Super Katana", world.player)
    rule = HasAll("Monster Fang", "Big Monster Fang")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Super Shield", world.player)
    rule = HasAll("Monster Eye", "Big Monster Eye")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Super Staff", world.player)
    rule = HasAll("Monster Meat", "Big Monster Meat")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Talisman of Hope", world.player)
    rule = Has("Lavish Monster Skin")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Talisman of Legend", world.player)
    rule = HasAll("Big Monster Skin", "Sturdy Monster Skin", "Lavish Monster Skin")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Talisman of Overflowing Talent", world.player)
    rule = HasAll("Monster Skin", "Big Monster Skin")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Talisman V3", world.player)
    rule = HasAll("Ultimate Talisman", "Divine Monster Skin")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Tattered Hat", world.player)
    rule = Has("Small Monster Fur")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Tattered Shoes", world.player)
    rule = Has("Small Monster Fur")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Tattered Talisman", world.player)
    rule = Has("Small Monster Skin")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Tattered Uniform", world.player)
    rule = Has("Small Monster Skin")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft The End of Hacking Gun", world.player)
    rule = HasAll("Divine Monster Fang", "Lavish Monster Fang")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft The End of Katana", world.player)
    rule = HasAll("Divine Monster Fang", "Lavish Monster Fang")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft The End of Shield", world.player)
    rule = HasAll("Lavish Monster Eye", "Sturdy Monster Eye")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft The End of Staff", world.player)
    rule = HasAll("Lavish Monster Meat", "Sturdy Monster Meat")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Toilet Paper", world.player)
    rule = Has("Gold Monster Skin")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Ultimate ??? Proof", world.player)
    rule = HasAll("Silver Monster Fang", "Silver Monster Eye")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Ultimate Affluent Progeny Proof", world.player)
    rule = HasAll("Copper Monster Fang", "Copper Monster Meat")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Ultimate Child Caregiver Proof", world.player)
    rule = HasAll("Gold Monster Fang", "Gold Monster Meat")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Ultimate Clairvoyant Proof", world.player)
    rule = HasAll("Copper Monster Fang", "Copper Monster Meat")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Ultimate Despair Proof", world.player)
    rule = HasAll("Platinum Monster Meat", "Platinum Monster Skin", "Platinum Monster Fur")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Ultimate Gymnast Proof", world.player)
    rule = HasAll("Silver Monster Fang", "Silver Monster Fur")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Ultimate Hat", world.player)
    rule = HasAll("Big Monster Fur", "Sturdy Monster Fur")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Ultimate Hope Proof", world.player)
    rule = HasAll("Platinum Monster Fang", "Copper Monster Fang", "Gold Monster Fang", "Silver Monster Fang")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Ultimate Lucky Student Proof", world.player)
    rule = HasAll("Copper Monster Fang", "Copper Monster Eye")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Ultimate Magician Proof", world.player)
    rule = HasAll("Gold Monster Fang", "Gold Monster Eye")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Ultimate Mechanic Proof", world.player)
    rule = HasAll("Silver Monster Fang", "Silver Monster Meat")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Ultimate Murderous Fiend Proof", world.player)
    rule = HasAll("Copper Monster Eye", "Copper Monster Fur")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Ultimate Princess Proof", world.player)
    rule = HasAll("Silver Monster Eye", "Silver Monster Meat")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Ultimate Shoes", world.player)
    rule = HasAll("Big Monster Fur", "Sturdy Monster Fur")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Ultimate Swimming Pro Proof", world.player)
    rule = HasAll("Copper Monster Eye", "Copper Monster Meat")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Craft Ultimate Talisman", world.player)
    rule = HasAll("Big Monster Skin", "Sturdy Monster Skin")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Ultimate Uniform", world.player)
    rule = HasAll("Big Monster Skin", "Sturdy Monster Skin")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Ultimate Writing Prodigy Proof", world.player)
    rule = HasAll("Copper Monster Eye", "Copper Monster Skin")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Ultimate Yakuza Proof", world.player)
    rule = HasAll("Silver Monster Fang", "Silver Monster Skin")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Uniform of Hope", world.player)
    rule = Has("Lavish Monster Skin")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Uniform of Legend", world.player)
    rule = HasAll("Big Monster Skin", "Sturdy Monster Skin", "Lavish Monster Skin")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Uniform of Overflowing Talent", world.player)
    rule = HasAll("Monster Skin", "Big Monster Skin")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Uniform V3", world.player)
    rule = HasAll("Ultimate Uniform", "Divine Monster Skin")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("V Hacking Gun", world.player)
    rule = HasAll("Big Monster Fang", "Sturdy Monster Fang")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("V Katana", world.player)
    rule = HasAll("Big Monster Fang", "Sturdy Monster Fang")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("V Shield", world.player)
    rule = HasAll("Big Monster Eye", "Sturdy Monster Eye")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("V Staff", world.player)
    rule = HasAll("Big Monster Meat", "Sturdy Monster Meat")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Worn Hacking Gun", world.player)
    rule = Has("Small Monster Fang")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Worn Katana", world.player)
    rule = Has("Small Monster Fang")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Worn Shield", world.player)
    rule = Has("Small Monster Eye")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Worn Staff", world.player)
    rule = Has("Small Monster Meat")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Akane Owari", world.player)
    rule = CheckCharacter("Akane Owari")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Angie Yonaga", world.player)
    rule = CheckCharacter("Angie Yonaga")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Aoi Asahina", world.player)
    rule = CheckCharacter("Aoi Asahina")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Byakuya Togami", world.player)
    rule = CheckCharacter("Byakuya Togami")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Celestia Ludenberg", world.player)
    rule = CheckCharacter("Celestia Ludenberg")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Chiaki Nanami", world.player)
    rule = CheckCharacter("Chiaki Nanami")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Chihiro Fujisaki", world.player)
    rule = CheckCharacter("Chihiro Fujisaki")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Fuyuhiko Kuzuryu", world.player)
    rule = CheckCharacter("Fuyuhiko Kuzuryu")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Genocide Jack", world.player)
    rule = CheckCharacter("Genocide Jack")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Gonta Gokuhara", world.player)
    rule = CheckCharacter("Gonta Gokuhara")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Gundham Tanaka", world.player)
    rule = CheckCharacter("Gundham Tanaka")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Hajime Hinata", world.player)
    rule = CheckCharacter("Hajime Hinata")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Hifumi Yamada", world.player)
    rule = CheckCharacter("Hifumi Yamada")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Himiko Yumeno", world.player)
    rule = CheckCharacter("Himiko Yumeno")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Hiroko Hagakure", world.player)
    rule = CheckCharacter("Hiroko Hagakure")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Hiyoko Saionji", world.player)
    rule = CheckCharacter("Hiyoko Saionji")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Ibuki Mioda", world.player)
    rule = CheckCharacter("Ibuki Mioda")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Izuru Kamukura", world.player)
    rule = CheckCharacter("Izuru Kamukura")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Jataro Kemuri", world.player)
    rule = CheckCharacter("Jataro Kemuri")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Junko Enoshima", world.player)
    rule = CheckCharacter("Junko Enoshima")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with K1-B0", world.player)
    rule = CheckCharacter("K1-B0")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Kaede Akamatsu", world.player)
    rule = CheckCharacter("Kaede Akamatsu")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Kaito Momota", world.player)
    rule = CheckCharacter("Kaito Momota")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Kazuichi Soda", world.player)
    rule = CheckCharacter("Kazuichi Soda")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Kirumi Tojo", world.player)
    rule = CheckCharacter("Kirumi Tojo")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Kiyotaka Ishimaru", world.player)
    rule = CheckCharacter("Kiyotaka Ishimaru")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Kokichi Oma", world.player)
    rule = CheckCharacter("Kokichi Oma")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Komaru Naegi", world.player)
    rule = CheckCharacter("Komaru Naegi")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Korekiyo Shinguji", world.player)
    rule = CheckCharacter("Korekiyo Shinguji")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Kotoko Utsugi", world.player)
    rule = CheckCharacter("Kotoko Utsugi")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Kurokuma", world.player)
    rule = CheckCharacter("Kurokuma")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Kyoko Kirigiri", world.player)
    rule = CheckCharacter("Kyoko Kirigiri")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Leon Kuwata", world.player)
    rule = CheckCharacter("Leon Kuwata")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Mahiru Koizumi", world.player)
    rule = CheckCharacter("Mahiru Koizumi")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Maki Harukawa", world.player)
    rule = CheckCharacter("Maki Harukawa")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Makoto Naegi", world.player)
    rule = CheckCharacter("Makoto Naegi")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Masaru Daimon", world.player)
    rule = CheckCharacter("Masaru Daimon")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Mikan Tsumiki", world.player)
    rule = CheckCharacter("Mikan Tsumiki")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Miu Iruma", world.player)
    rule = CheckCharacter("Miu Iruma")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Monaca Towa", world.player)
    rule = CheckCharacter("Monaca Towa")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Mondo Owada", world.player)
    rule = CheckCharacter("Mondo Owada")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Monokuma", world.player)
    rule = CheckCharacter("Monokuma")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Monomi", world.player)
    rule = CheckCharacter("Monomi")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Mukuro Ikusaba", world.player)
    rule = CheckCharacter("Mukuro Ikusaba")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Nagisa Shingetsu", world.player)
    rule = CheckCharacter("Nagisa Shingetsu")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Nagito Komaeda", world.player)
    rule = CheckCharacter("Nagito Komaeda")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Nekomaru Nidai", world.player)
    rule = CheckCharacter("Nekomaru Nidai")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Peko Pekoyama", world.player)
    rule = CheckCharacter("Peko Pekoyama")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Rantaro Amami", world.player)
    rule = CheckCharacter("Rantaro Amami")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Ryoma Hoshi", world.player)
    rule = CheckCharacter("Ryoma Hoshi")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Sakura Ogami", world.player)
    rule = CheckCharacter("Sakura Ogami")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Sayaka Maizono", world.player)
    rule = CheckCharacter("Sayaka Maizono")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Shirokuma", world.player)
    rule = CheckCharacter("Shirokuma")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Shuichi Saihara", world.player)
    rule = CheckCharacter("Shuichi Saihara")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Sonia Nevermind", world.player)
    rule = CheckCharacter("Sonia Nevermind")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Tenko Chabashira", world.player)
    rule = CheckCharacter("Tenko Chabashira")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Teruteru Hanamura", world.player)
    rule = CheckCharacter("Teruteru Hanamura")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with The Ultimate Imposter", world.player)
    rule = CheckCharacter("The Ultimate Imposter")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Toko Fukawa", world.player)
    rule = CheckCharacter("Toko Fukawa")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Tsumugi Shirogane", world.player)
    rule = CheckCharacter("Tsumugi Shirogane")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Usami", world.player)
    rule = CheckCharacter("Usami")
    world.set_rule(location, rule)

    location = world.multiworld.get_location("Clear a Development Plan with Yasuhiro Hagakure", world.player)
    rule = CheckCharacter("Yasuhiro Hagakure")
    world.set_rule(location, rule)

    location = world.multiworld.get_location













    all_at_once_option = OptionFilter(CharacterGen, CharacterGen.option_all_at_once)
    progressive_option = OptionFilter(CharacterGen, CharacterGen.option_progressive)
    character_card_indices = [*range(10, 101, 10), *range(120, 241, 20)]
    for x in character_card_indices:
        location = world.multiworld.get_location(f"Acquire {x} Character Cards", world.player)
        rule = HasFromList(*world.character_item_list, count=x, options=[progressive_option]) | HasFromListUnique(
            *world.character_item_list, count=math.ceil(x / 4), options=[all_at_once_option])
        world.set_rule(location, rule)

    hype_card_indices = [*range(10, 101, 20), *range(150, 551, 50)]
    for x in hype_card_indices:
        location = world.multiworld.get_location(f"Acquire {x} Hype Cards", world.player)
        rule = HasFromListUnique(*world.character_item_list, count=x)
        world.set_rule(location, rule)

    dev_completion_indices = [*range(5, 201, 5)]
    for x in dev_completion_indices:
        location = world.multiworld.get_location(f"Complete Development for {x} Characters", world.player)
        rule = HasFromList(*world.character_item_list, count=x, options=[progressive_option]) | HasFromListUnique(
            *world.character_item_list, count=math.ceil(x / 4), options=[all_at_once_option])
        world.set_rule(location, rule)

    reach_level_99_indices = [*range(5, 61, 5)]
    for x in reach_level_99_indices:
        location = world.multiworld.get_location(f"Reach Level 99 on {x} or More Characters", world.player)
        child_rules = [CheckCharacter(character) & HasMaxHype(character) for character in characters]
        rule = AtLeast(x, *child_rules) & Has("Progressive Scroll", 5) & HasAll ("Monokid's Hope Fragment", "Monosuke's Hope Fragment", "Monodam's Hope Fragment", "Monophanie's Hope Fragment", "Monotaro's Hope Fragment")
        world.set_rule(location, rule)

    ##view_event_indices = [*range(10, 60, 10)]
    ##for x in view_event_indices:
    ##    location = world.multiworld.get_location(f"View {x} Events", world.player)
