from __future__ import annotations

import math
from dataclasses import dataclass
from tkinter import EventType
from typing import TYPE_CHECKING
from rule_builder.rules import *

from BaseClasses import CollectionState, Entrance, Location, Region
from .items import item_table
from .data import *
from .constants import *
from .options import *


if TYPE_CHECKING:
    from .world import DanganronpaSWorld



## Master Code B)
def create_rules(world: DanganronpaSWorld):
    create_location_rules(world)
    create_entrance_rules(world)


@dataclass
class HasCharacter(Rule["DanganronpaSWorld"], game = DANGANRONPA_S):
    character: Character

    @override
    def _instantiate(self, world: DanganronpaSWorld) -> Rule.Resolved:
        return HasFromListUnique(*world.character_item_dict[self.character], count=1).resolve(world)


@dataclass(kw_only=True)
class HasCharacterRarity(HasCharacter, game=DANGANRONPA_S):
    rarity: CharacterRarity

    @override
    def _instantiate(self, world: DanganronpaSWorld) -> Rule.Resolved:
        match world.options.character_gen.value:
            case CharacterGen.option_all_at_once:
                return HasCharacter(self.character).resolve(world)
            case CharacterGen.option_progressive:
                match self.rarity:
                    case CharacterRarity.ULTRA_RARE:
                        return Has(*world.character_item_dict[self.character], count=4).resolve(world)
                    case CharacterRarity.SUPER_RARE:
                        return Has(*world.character_item_dict[self.character], count=3).resolve(world)
                    case CharacterRarity.RARE:
                        return Has(*world.character_item_dict[self.character], count=2).resolve(world)
                    case CharacterRarity.NORMAL:
                        return Has(*world.character_item_dict[self.character], count=1).resolve(world)
            case CharacterGen.option_scattered:
                return Has(f"{self.character.char_name} ({self.rarity.value})").resolve(world)


@dataclass
class HasCharacters(Rule["DanganronpaSWorld"], game = DANGANRONPA_S):
    number: int
    @override
    def _instantiate(self, world: DanganronpaSWorld) -> Rule.Resolved:
        return AtLeast(self.number, *[HasCharacter(character) for character in world.character_item_dict.keys()]).resolve(world)


@dataclass
class HasMaxHype(Rule["DanganronpaSWorld"], game = DANGANRONPA_S):
    character: Character
    @override
    def resolve(self, world: DanganronpaSWorld) -> Rule.Resolved:
        hype_card_items = [f"{self.character.char_name} - {hype_card.value}" for hype_card in HypeCardType]
        return HasAll(*hype_card_items).resolve(world)

@dataclass(kw_only=True)
class HasCharacterCards(Rule["DanganronpaSWorld"], game = DANGANRONPA_S):
    number: int

    @override
    def _instantiate(self, world: DanganronpaSWorld) -> Rule.Resolved:
        if world.options.character_gen == CharacterGen.option_all_at_once:
            return HasFromListUnique(*[char_item for character, char_items in world.character_item_dict.items() for char_item in char_items], count=math.ceil(self.number / 4)).resolve(world)

        elif world.options.character_gen == CharacterGen.option_progressive:
            return self.Resolved(number=self.number, character_item_list=tuple([char_items[0] for character, char_items in world.character_item_dict.items()]), player=world.player)
        else:
            #scattered
            return HasFromListUnique(*[char_item for character, char_items in world.character_item_dict.items() for char_item in char_items], count=self.number).resolve(world)


    class Resolved(Rule.Resolved):
        number: int = 0
        character_item_list: tuple[str, ...] = field(default_factory=tuple)

        @override
        def _evaluate(self, state: CollectionState) -> bool:
            return self._get_card_count(state) >= self.number

        def _get_card_count(self, state: CollectionState) -> int:
            card_count: int = 0
            for item_name in self.character_item_list:
                card_count += min(state.count(item=item_name, player=self.player), 4)
            return card_count

        @override
        def item_dependencies(self) -> dict[str, set[int]]:
            return {item_name: {id(self)} for item_name in self.character_item_list}


@dataclass(kw_only=True)
class CanReachTowerFloor(Rule["DanganronpaSWorld"], game = DANGANRONPA_S):
    tower_floor: int

    @override
    def _instantiate(self, world: DanganronpaSWorld) -> Rule.Resolved:
        if self.tower_floor < 1:
            return False_["DanganronpaSWorld"]().resolve(world=world)

        monokub_fragment_list = [f"{monokub.value}'s Hope Fragment" for monokub in MonoKub]
        if self.tower_floor < 20:
            return True_["DanganronpaSWorld"]().resolve(world=world)
        if self.tower_floor < 40:
            return Has("Progressive Scroll", count=1).resolve(world=world)
        elif self.tower_floor < 60:
            return (Has("Progressive Scroll", count=1) & HasFromListUnique(*monokub_fragment_list, count=1)).resolve(world=world)
        elif self.tower_floor < 80:
            return (Has("Progressive Scroll", count=2) & HasFromListUnique(*monokub_fragment_list, count=1)).resolve(world=world)
        elif self.tower_floor < 100:
            return (Has("Progressive Scroll", count=2) & HasFromListUnique(*monokub_fragment_list, count=2)).resolve(world=world)
        elif self.tower_floor < 120:
            return (Has("Progressive Scroll", count=3) & HasFromListUnique(*monokub_fragment_list, count=2)).resolve(world=world)
        elif self.tower_floor < 140:
            return (Has("Progressive Scroll", count=3) & HasFromListUnique(*monokub_fragment_list, count=3)).resolve(world=world)
        elif self.tower_floor < 160:
            return (Has("Progressive Scroll", count=4) & HasFromListUnique(*monokub_fragment_list, count=3)).resolve(world=world)
        elif self.tower_floor < 180:
            return (Has("Progressive Scroll", count=4) & HasFromListUnique(*monokub_fragment_list, count=4)).resolve(world=world)
        elif self.tower_floor < 200:
            return (Has("Progressive Scroll", count=5) & HasFromListUnique(*monokub_fragment_list, count=4)).resolve(world=world)
        else:
            return (Has("Progressive Scroll", count=5) & HasFromListUnique(*monokub_fragment_list, count=5)).resolve(world=world)


## Individual Entrance Rules
def create_entrance_rules(world: DanganronpaSWorld):

    #EXAMPLE:
    #entrance = get_entrances(world.get_region(""), world.get_region(""))
    #rule = (HasAll = And) (HasAny = Or)
    #world.set_rule(entrance1)


    entrance: Entrance = get_entrance(world, world.get_region("Battle Tower Lower Floors"), world.get_region("Battle Tower Upper Floors"))
    world.set_rule(entrance, HasCharacters(10))

    entrance = get_entrance(world, world.get_region("Battle Tower Upper Floors"), world.get_region("Battle Tower Lower Ultimate Floors"))
    world.set_rule(entrance, HasCharacters(20))

    entrance = get_entrance(world, world.get_region("Battle Tower Upper Floors"), world.get_region("Arena of Despair"))
    world.set_rule(entrance, HasCharacters(20))

    entrance = get_entrance(world, world.get_region("Battle Tower Lower Ultimate Floors"), world.get_region("Battle Tower Upper Ultimate Floors"))
    world.set_rule(entrance, HasCharacters(30))

    entrance = get_entrance(world, world.get_region(DevModeLocation.FIRST_ISLAND), world.get_region(DevModeLocation.SECOND_ISLAND))
    world.set_rule(entrance, Has("Progressive Scroll"))

    entrance = get_entrance(world, world.get_region(DevModeLocation.SECOND_ISLAND), world.get_region(DevModeLocation.THIRD_ISLAND))
    world.set_rule(entrance, Has("Progressive Scroll", count=2))

    entrance = get_entrance(world, world.get_region(DevModeLocation.THIRD_ISLAND), world.get_region(DevModeLocation.FOURTH_ISLAND))
    world.set_rule(entrance, Has("Progressive Scroll", count=3))

    entrance = get_entrance(world, world.get_region(DevModeLocation.FOURTH_ISLAND), world.get_region(DevModeLocation.FIFTH_ISLAND))
    world.set_rule(entrance, Has("Progressive Scroll", count=4))

    entrance = get_entrance(world, world.get_region(DevModeLocation.FIRST_ISLAND), world.get_region(DevModeLocation.COTTAGE))
    world.set_rule(entrance, Has(f"{DevModeLocation.COTTAGE} Unlock"))

    entrance = get_entrance(world, world.get_region(DevModeLocation.SECOND_ISLAND), world.get_region(DevModeLocation.BEACH_HOUSE))
    world.set_rule(entrance, Has(f"{DevModeLocation.BEACH_HOUSE} Unlock"))

    entrance = get_entrance(world, world.get_region(DevModeLocation.THIRD_ISLAND), world.get_region(DevModeLocation.HOSPITAL))
    world.set_rule(entrance, Has(f"{DevModeLocation.HOSPITAL} Unlock"))

    entrance = get_entrance(world, world.get_region(DevModeLocation.FOURTH_ISLAND), world.get_region(DevModeLocation.FUN_HOUSE))
    world.set_rule(entrance, Has(f"{DevModeLocation.FUN_HOUSE} Unlock"))

    entrance= get_entrance(world, world.get_region(DevModeLocation.FIFTH_ISLAND), world.get_region(DevModeLocation.FACTORY))
    world.set_rule(entrance, Has(f"{DevModeLocation.FACTORY} Unlock"))

    entrance = get_entrance(world, world.get_region(DevModeLocation.FIFTH_ISLAND), world.get_region(DevModeLocation.SECRET))
    world.set_rule(entrance, Has("Progressive Scroll", count=5))

    hope_fragments = [item_name for item_name in item_table if "Hope Fragment" in item_name]

    entrance = get_entrance(world, world.get_region("Menu"), world.get_region(f"{MonoKub.MONOKID}s Hope"))
    world.set_rule(entrance, HasFromListUnique(*hope_fragments, count=10))

    entrance = get_entrance(world, world.get_region(f"{MonoKub.MONOKID}s Hope"), world.get_region(f"{MonoKub.MONOSUKE}s Hope"))
    world.set_rule(entrance, HasFromListUnique(*hope_fragments, count=20))

    entrance = get_entrance(world, world.get_region(f"{MonoKub.MONOSUKE}s Hope"), world.get_region(f"{MonoKub.MONODAM}s Hope"))
    world.set_rule(entrance, HasFromListUnique(*hope_fragments, count=30))

    entrance = get_entrance(world, world.get_region(f"{MonoKub.MONODAM}s Hope"), world.get_region(f"{MonoKub.MONOPHANIE}s Hope"))
    world.set_rule(entrance, HasFromListUnique(*hope_fragments, count=40))

    entrance = get_entrance(world, world.get_region(f"{MonoKub.MONOPHANIE}s Hope"), world.get_region(f"{MonoKub.MONOTARO}s Hope"))
    world.set_rule(entrance, HasFromListUnique(*hope_fragments, count=50))

    entrance = get_entrance(world, world.get_region(f"{MonoKub.MONOTARO}s Hope"), world.get_region("Graduation"))
    world.set_rule(entrance, HasFromListUnique(*hope_fragments, count=67))

    entrance = get_entrance(world, world.get_region("Menu"), world.get_region("Gacha2"))
    world.set_rule(entrance, HasCharacters(10))

    entrance = get_entrance(world, world.get_region("Menu"), world.get_region("Gacha3"))
    world.set_rule(entrance, HasCharacters(20))

    entrance = get_entrance(world, world.get_region("Menu"), world.get_region("Gacha4"))
    world.set_rule(entrance, HasCharacters(30))

    entrance = get_entrance(world, world.get_region("Menu"), world.get_region("Gacha5"))
    world.set_rule(entrance, HasCharacters(40))

    entrance = get_entrance(world, world.get_region("Menu"), world.get_region("Gacha6"))
    world.set_rule(entrance, Has("Progressive Scroll", count=1))

    entrance = get_entrance(world, world.get_region("Menu"), world.get_region("Gacha7"))
    world.set_rule(entrance, Has("Progressive Scroll", count=2))

    entrance = get_entrance(world, world.get_region("Menu"), world.get_region("Gacha8"))
    world.set_rule(entrance, Has("Progressive Scroll", count=3))

    entrance = get_entrance(world, world.get_region("Menu"), world.get_region("Gacha9"))
    world.set_rule(entrance, Has("Progressive Scroll", count=4))

    entrance = get_entrance(world, world.get_region("Menu"), world.get_region("Gacha10"))
    world.set_rule(entrance, Has(f"{DevModeLocation.COTTAGE} Unlock"))

    entrance = get_entrance(world, world.get_region("Menu"), world.get_region("Gacha11"))
    world.set_rule(entrance, Has("Progressive Scroll", count=1) & Has(f"{DevModeLocation.BEACH_HOUSE} Unlock"))

    entrance = get_entrance(world, world.get_region("Menu"), world.get_region("Gacha12"))
    world.set_rule(entrance, Has("Progressive Scroll", count=2) & Has(f"{DevModeLocation.HOSPITAL} Unlock"))

    entrance = get_entrance(world, world.get_region("Menu"), world.get_region("Gacha13"))
    world.set_rule(entrance, Has("Progressive Scroll", count=3) & Has(f"{DevModeLocation.FUN_HOUSE} Unlock"))
    
    entrance = get_entrance(world, world.get_region("Menu"), world.get_region("Gacha14"))
    world.set_rule(entrance, Has("Progressive Scroll", count=4) & Has(f"{DevModeLocation.FACTORY} Unlock"))

    entrance = get_entrance(world, world.get_region("Menu"), world.get_region("Gacha15"))
    world.set_rule(entrance, HasCharacters(50))


## Rule helper thingy for regions
def get_entrance(world: DanganronpaSWorld, region1: Region, region2: Region) -> Entrance:
    entrance1 = world.multiworld.get_entrance(f"{region1.name} => {region2.name}", world.player)
    return entrance1

##Creating Location Rules
def create_location_rules(world: DanganronpaSWorld) -> None:

    ##EXAMPLE
    ##location = world.multiworld.get_location("name")
    ##rule = ##logic##
    ##world.set_rule(location, rule)

    crafted_item_rules: list[Rule["DanganronpaSWorld"]] = []

    for crafted_item in CraftedItem:
        location: Location = world.multiworld.get_location(f"Craft {crafted_item.item_name}", world.player)
        crafting_mats: list[str] = [material.material_name for material in crafted_item.material_list]
        rule: Rule["DanganronpaSWorld"] = HasAll(*crafting_mats)
        if crafted_item.prereq_item_name != "":
            rule &= Has(f"{crafted_item.prereq_item_name}")
        crafted_item_rules.append(rule)
        world.set_rule(location, rule)



    crafted_item_count_indices = [10, 20, 30, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 92]
    for x in crafted_item_count_indices:
        location = world.multiworld.get_location(f"Create {x} types of equipment in Battle Mode", world.player)
        rule: Rule["DanganronpaSWorld"] = AtLeast(x, *crafted_item_rules)
        world.set_rule(location, rule)



    for character in world.character_item_dict.keys():
        location = world.multiworld.get_location(f"Clear a Development Plan with {character.char_name}", world.player)
        rule: Rule["DanganronpaSWorld"] = HasCharacter(character)
        world.set_rule(location, rule)


    character_card_indices = [*range(10, 101, 10), *range(120, 241, 20)]
    for x in character_card_indices:
        location = world.multiworld.get_location(f"Acquire {x} character cards", world.player)
        world.set_rule(location, HasCharacterCards(number=x))

    hype_card_indices = [*range(10, 101, 20), *range(150, 551, 50)]
    for x in hype_card_indices:
        location = world.multiworld.get_location(f"Acquire {x} hype cards", world.player)
        rule = HasFromListUnique(*[f"{character.char_name} - {hype_card}" for character in world.character_item_dict.keys() for hype_card in HypeCardType], count=x)
        world.set_rule(location, rule)

    dev_completion_indices = [*range(5, 201, 5)]
    for x in dev_completion_indices:
        location = world.multiworld.get_location(f"Complete development for {x} characters", world.player)
        rule = HasCharacterCards(number=x)
        world.set_rule(location, rule)

    reach_level_99_indices = [*range(5, 61, 5)]
    for x in reach_level_99_indices:
        location = world.multiworld.get_location(f"Reach level 99 on {x} or more characters", world.player)
        child_rules = [HasCharacter(character) & HasMaxHype(character) for character in world.character_item_dict.keys()]
        rule = AtLeast(x, *child_rules) & Has("Progressive Scroll", 5) & HasAll ("Monokid's Hope Fragment", "Monosuke's Hope Fragment", "Monodam's Hope Fragment", "Monophanie's Hope Fragment", "Monotaro's Hope Fragment")
        world.set_rule(location, rule)



    event_rules_mapping: dict[Character, dict[CharacterEventType, Rule["DanganronpaSWorld"]]] = {}

    for character in world.character_item_dict.keys():
        event_rules_mapping[character] = {}

    for event in CharacterEvent:
        match event.event_type:
            case CharacterEventType.FRIEND:
                char_list: list[Character] = event.char_list
                rule: Rule["DanganronpaSWorld"] = False_["DanganronpaSWorld"]()
                for index, character in enumerate(char_list):
                    if character in event.get_logically_needed_characters():
                        rule |= HasCharacter(character)
                for character in char_list:
                    event_rules_mapping[character][event.event_type] = rule

            case CharacterEventType.MY_FUTURE:
                # done on second iteration
                pass

            case CharacterEventType.SWIMSUIT:
                event_rules_mapping[event.char_list[0]][event.event_type] = HasCharacterRarity(character=event.char_list[0], rarity=CharacterRarity.SUPER_RARE) | HasCharacterRarity(character=event.char_list[0], rarity=CharacterRarity.ULTRA_RARE)

            case CharacterEventType.POTENTIAL_TALENT:
                event_rules_mapping[event.char_list[0]][event.event_type] = HasCharacter(event.char_list[0])

            case CharacterEventType.SUMMER_FESTIVAL:
                event_rules_mapping[event.char_list[0]][event.event_type] = HasCharacter(event.char_list[0])

            case CharacterEventType.CAMPFIRE:
                event_rules_mapping[event.char_list[0]][event.event_type] = HasCharacter(event.char_list[0])

    event_rule_list: list[Rule["DanganronpaSWorld"]] = []

    for event in CharacterEvent:
        match event.event_type:
            case CharacterEventType.MY_FUTURE:
                rule: Rule["DanganronpaSWorld"] = True_["DanganronpaSWorld"]()
                for event_type in CharacterEventType:
                    if event_type is not CharacterEventType.MY_FUTURE:
                        rule &= event_rules_mapping[event.char_list[0]][event_type]

                event_rules_mapping[event.char_list[0]][event.event_type] = rule
                event_rule_list.append(rule)
                pass
            case _:
                event_rule_list.append(event_rules_mapping[event.char_list[0]][event.event_type])
                pass


    view_event_indices = [*range(10, 60, 10)]
    for x in view_event_indices:
       location = world.multiworld.get_location(f"View {x} Events", world.player)
       rule: Rule["DanganronpaSWorld"] = AtLeast(x, *event_rule_list)
       world.set_rule(location, rule)

    for event in CharacterEvent:
        location = world.multiworld.get_location(f"[Eventsanity] - {event.event_name}", world.player)
        world.set_rule(location, event_rules_mapping[event.char_list[0]][event.event_type])


    collect_grimoire_indices: list[int] = [*range(1, 6, 1)]
    for x in collect_grimoire_indices:
        location = world.multiworld.get_location(f"Collect {x} grimoire in 1 Dev Mode game", world.player)
        world.set_rule(location, Has("Progressive Scroll", count=x))
        location = world.multiworld.get_location(f"Defeat {x} Monobeast in 1 Dev Mode game", world.player)
        world.set_rule(location, Has("Progressive Scroll", count=x))


    collect_jabbercoin_indices = [5000, 15000, 30000]
    monokub_fragment_list = [f"{monokub.value}'s Hope Fragment" for monokub in MonoKub]
    for x in collect_jabbercoin_indices:
        location = world.multiworld.get_location(f"Clear a Dev Plan acquiring {x} Jabbercoins", world.player)
        if x == 5000:
            continue
        if x == 15000:
            world.set_rule(location, Has("Progressive Scroll", count=2) & HasFromListUnique(*monokub_fragment_list, count=2))
        elif x == 30000:
            world.set_rule(location, Has("Progressive Scroll", count=4) & HasFromListUnique(*monokub_fragment_list, count=4))


    for character in world.character_item_dict.keys():
        location = world.multiworld.get_location(f"View {character.char_name}'s Events 10 Times", world.player)
        world.set_rule(location, HasCharacter(character))
        location = world.multiworld.get_location(f"Clear a Development Plan with {character.char_name}", world.player)
        world.set_rule(location, HasCharacter(character))

    location = world.multiworld.get_location("Obtain 20 equipment in a single Development Plan", world.player)
    world.set_rule(location, Has("Progressive Scroll", count=5))


    for enemy in EnemyInformation:
        location: Location = world.multiworld.get_location(f"Defeat {enemy.enemy_name}", world.player)
        # print(f"Creating Rule for: Defeat {enemy.enemy_name}")
        world.set_rule(location, enemy.get_location_rule())


    for x in range(1, 201):
        location = world.multiworld.get_location(f"Battle Tower Floor {x} Mission A", world.player)
        world.set_rule(location, CanReachTowerFloor(tower_floor=x))
        location = world.multiworld.get_location(f"Battle Tower Floor {x} Mission B", world.player)
        world.set_rule(location, CanReachTowerFloor(tower_floor=x))
        location = world.multiworld.get_location(f"Battle Tower Floor {x} Mission C", world.player)
        world.set_rule(location, CanReachTowerFloor(tower_floor=x))


    battle_mode_mission_indices = [*range(30, 631, 30)]
    for x in battle_mode_mission_indices:
        location = world.multiworld.get_location(f"Clear {x} Battle Mode Missions", world.player)
        world.set_rule(location, CanReachTowerFloor(tower_floor = math.ceil(x / 3)))


    clear_lower_tower_indices = [*range(25, 226, 25)]
    for x in clear_lower_tower_indices:
        location = world.multiworld.get_location(f"Clear Lower Despair Tower {x} Times", world.player)
    world.set_rule(location, CanReachTowerFloor(tower_floor = 50))

    clear_lower_tower_indices = [*range(25, 226, 25)]
    for x in clear_lower_tower_indices:
        location = world.multiworld.get_location(f"Clear Upper Despair Tower {x} Times", world.player)
    world.set_rule(location, CanReachTowerFloor(tower_floor=100))

    clear_lower_tower_indices = [*range(25, 226, 25)]
    for x in clear_lower_tower_indices:
        location = world.multiworld.get_location(f"Clear Lower Ultra Despair Tower {x} Times", world.player)
    world.set_rule(location, CanReachTowerFloor(tower_floor=150))

    clear_lower_tower_indices = [*range(25, 226, 25)]
    for x in clear_lower_tower_indices:
        location = world.multiworld.get_location(f"Clear Upper Ultra Despair Tower {x} Times", world.player)
    world.set_rule(location, CanReachTowerFloor(tower_floor=200))

    one_hit_damage_indices = [*range(5000, 20001, 5000)]
    for x in one_hit_damage_indices:
        location = world.multiworld.get_location(f"Deal {x} damage in Battle Mode with 1 Hit", world.player)
        if x == 5000:
            world.set_rule(location, CanReachTowerFloor(tower_floor=50))
        elif x == 10000:
            world.set_rule(location, CanReachTowerFloor(tower_floor=100))
        elif x == 15000:
            world.set_rule(location, CanReachTowerFloor(tower_floor=150))
        else:
            world.set_rule(location, CanReachTowerFloor(tower_floor=200))


    arena_damage_indices = [50000, 100000, 200000, 300000, 400000, 500000]
    for x in arena_damage_indices:
        location = world.multiworld.get_location(f"Deal {x} damage in Arena of Despair", world.player)
    world.set_rule(location, CanReachTowerFloor(tower_floor=100) & HasAll("Hat V3", "Uniform V3", "Shoes V3", "Talisman V3") & HasAny("Katana V3", "Hacking Gun V3", "Staff V3", "Shield V3"))





