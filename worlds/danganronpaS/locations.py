from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, List
from BaseClasses import ItemClassification, Location, LocationProgressType, Region
from . import data, items, rules

if TYPE_CHECKING:
    from .world import DanganronpaSWorld

class DRSLocation(Location):
    game = "Danganronpa S"



## Location List
location_dictionary: dict[str, int] = {
    **{f"gachapull_{i}": i for i in range (1,807)},

    **{f"Battle Tower Floor {i} Mission A": i+1000 for i in range (1,201)},
    **{f"Battle Tower Floor {i} Mission B": i+1500 for i in range (1,201)},
    **{f"Battle Tower Floor {i} Mission C": i+2000 for i in range (1,201)},

    **{f"Craft {crafted_item}": i+2501 for i, crafted_item in enumerate(data.CraftedItem)},
    **{f"Clear a Development Plan with {character}": i+3001 for i, character in enumerate(data.Character)},
    **{f"Defeat {enemy}": i+3501 for i, enemy in enumerate(data.EnemyInformation)},
    **{f"[Friendsanity] - {friendsanity}": 1+16501 for i, friendsanity in enumerate(data.CharacterEvent)},

    ## Usami Flowers, jfc
    **{f"Acquire {x} character cards": i+4001 for i, x in enumerate([*range(10, 101, 10), *range(120, 241, 20)])},
    **{f"Acquire {x} hype cards": i+4501 for i, x in enumerate([*range(10, 101, 20), *range(150, 551, 50)])},
    **{f"Complete development for {x} characters": i+5001 for i, x in enumerate([*range(5, 201, 5)])},
    **{f"Reach level 99 on {x} or more characters": i+5501 for i, x in enumerate([*range(5, 61, 5)])},
    **{f"View {x} Events": i+6001 for i, x in enumerate([*range(10, 60, 10)])},
    **{f"Use {x} types of cards in 1 Dev Mode game": i+6501 for i, x in enumerate([*range(10, 21, 10)])},
    **{f"Collect {x} grimoire in 1 Dev Mode game": 1+7001 for i, x in enumerate([*range(1, 6, 1)])},
    **{f"Defeat {x} Monobeast in 1 Dev Mode game": i+7501 for i, x in enumerate([*range(1, 6, 1)])},
    **{f"Clear a Development Plan after winning {x} battles": i+8001 for i, x in enumerate([*range(5, 30, 15)])},
    **{f"Clear a Development Plan after shopping {x} times": i+8501 for i, x in enumerate([3,7,10])},
    **{f"Clear a Dev Plan acquiring {x} Jabbercoins": i+9001 for i, x in enumerate([*range(5000, 30001, 15000)])},
    **{f"Clear a Dev Plan stopping on {x} Growth Squares": i+9501 for i, x in enumerate([*range(10, 31, 10)])},
    **{f"Clear a Dev Plan stopping on {x} Talent Squares": i+10001 for i, x in enumerate([*range(10, 31, 10)])},
    **{f"Clear a Dev Plan stopping on {x} Event Squares": i+10501 for i, x in enumerate([*range(10, 31, 10)])},
    **{f"Clear a Dev Plan stopping on {x} Friendly Squares": i+11001 for i, x in enumerate([*range(10, 31, 10)])},
    **{f"Clear {x} Battle Mode Missions": i+11501 for i, x in enumerate([*range(30, 631, 30)])},
    **{f"Clear Lower Despair Tower {x} Times": i+12001 for i, x in enumerate([*range(25, 226, 25)])},
    **{f"Clear Upper Despair Tower {x} Times": i+12501 for i, x in enumerate([*range(25, 226, 25)])},
    **{f"Clear Lower Ultra Despair Tower {x} Times": i+13001 for i, x in enumerate([*range(25, 226, 25)])},
    **{f"Clear Upper Ultra Despair Tower {x} Times": i+13501 for i, x in enumerate([*range(25, 226, 25)])},
    **{f"Create {x} types of equipment in Battle Mode": i+14000 for i, x in enumerate([10, 20, 30, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 92])},
    **{f"Deal {x} damage in Battle Mode with 1 Hit": i+14501 for i, x in enumerate([*range(5000, 20001, 5000)])},
    **{f"Deal {x} damage in Arena of Despair": i+15000 for i, x in enumerate([50000, 100000, 200000, 300000, 400000, 500000])},
    **{f"View {character}'s Events 10 Times": i+15500 for i, character in enumerate(data.Character)},
    **{f"Clear a development plan without using a single card": 16001},
    **{f"Obtain 20 equipment in a single Development Plan": 16002},
    **{f"Clear a Development Plan without obtaining any equipment": 16003},
    **{f"Clear a Development Plan without taking any damage": 16004},
    **{f"Defeat an enemy with poison in battle mode": 16005},
    **{f"Clear a dev plan without resting": 16006},
}


## Actually creating the locations
def create_locations(world):
    for name, id in location_dictionary:
        if "gachapull" in name:
            pullnum = name.split("_")
            pullnum = pullnum[1]
            if pullnum < 53:
                region = world.getregion("Gacha1")
                location = DRSLocation(world.player, name, id, region)
                region.locations.append(location)
            elif pullnum < 106:
                region = world.getregion("Gacha2")
                location = DRSLocation(world.player, name, id, region)
                region.locations.append(location)
            elif pullnum < 159:
                region = world.getregion("Gacha3")
                location = DRSLocation(world.player, name, id, region)
                region.locations.append(location)
            elif pullnum < 212:
                region = world.getregion("Gacha4")
                location = DRSLocation(world.player, name, id, region)
                region.locations.append(location)
            elif pullnum < 265:
                region = world.getregion("Gacha5")
                location = DRSLocation(world.player, name, id, region)
                region.locations.append(location)
            elif pullnum < 318:
                region = world.getregion("Gacha6")
                location = DRSLocation(world.player, name, id, region)
                region.locations.append(location)
            elif pullnum < 371:
                region = world.getregion("Gacha7")
                location = DRSLocation(world.player, name, id, region)
                region.locations.append(location)
            elif pullnum < 424:
                region = world.getregion("Gacha8")
                location = DRSLocation(world.player, name, id, region)
                region.locations.append(location)
            elif pullnum < 477:
                region = world.getregion("Gacha9")
                location = DRSLocation(world.player, name, id, region)
                region.locations.append(location)
            elif pullnum < 530:
                region = world.getregion("Gacha10")
                location = DRSLocation(world.player, name, id, region)
                region.locations.append(location)
            elif pullnum < 583:
                region = world.getregion("Gacha11")
                location = DRSLocation(world.player, name, id, region)
                region.locations.append(location)
            elif pullnum < 636:
                region = world.getregion("Gacha12")
                location = DRSLocation(world.player, name, id, region)
                region.locations.append(location)
            elif pullnum < 689:
                region = world.getregion("Gacha13")
                location = DRSLocation(world.player, name, id, region)
                region.locations.append(location)
            elif pullnum < 742:
                region = world.getregion("Gacha14")
                location = DRSLocation(world.player, name, id, region)
                region.locations.append(location)
            elif pullnum < 806:
                region = world.getregion("Gacha15")
                location = DRSLocation(world.player, name, id, region)
                region.locations.append(location)
        elif "mission" in name:
            parts = name.split(" ")
            num = parts[3]
            if num < 51:
                region = world.getregion("Battle Tower Lower Floors")
                location = DRSLocation(world.player, name, id, region)
                region.locations.append(location)
            elif num < 101:
                region = world.getregion("Battle Tower Upper Floors")
                location = DRSLocation(world.player, name, id, region)
                region.locations.append(location)
            elif num < 151:
                region = world.getregion("Battle Tower Ultra Lower Floors")
                location = DRSLocation(world.player, name, id, region)
                region.locations.append(location)
            elif num < 201:
                region = world.getregion("Battle Tower Ultra Upper Floors")
                location = DRSLocation(world.player, name, id, region)
                region.locations.append(location)
        else:
            region = world.getregion("Menu")
            location = DRSLocation(world.player, name, id, region)
            region.locations.append(location)

