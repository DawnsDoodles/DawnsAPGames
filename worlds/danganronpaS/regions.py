from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region
from .rules import has_characters, can_get_grimoire_scroll, can_access_specific_island

if TYPE_CHECKING:
    from .world import DanganronpaSWorld


## Important stuff from APQuest
def create_and_connect_regions(world: DanganronpaSWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_region_helper(name:str, world: DanganronpaSWorld) -> None:
    region = Region(name, world.player, world.multiworld)
    world.multiworld.regions.append(region)



## Names of Regions
def create_all_regions(world: DanganronpaSWorld) -> None:
    create_region_helper("Menu", world)

    create_region_helper("Gacha1", world)
    create_region_helper("Gacha2", world)
    create_region_helper("Gacha3", world)
    create_region_helper("Gacha4", world)
    create_region_helper("Gacha5", world)
    create_region_helper("Gacha6", world)
    create_region_helper("Gacha7", world)
    create_region_helper("Gacha8", world)
    create_region_helper("Gacha9", world)
    create_region_helper("Gacha10", world)
    create_region_helper("Gacha11", world)
    create_region_helper("Gacha12", world)
    create_region_helper("Gacha13", world)
    create_region_helper("Gacha14", world)
    create_region_helper("Gacha15", world)

    create_region_helper("Battle Tower Lower Floors", world)
    create_region_helper("Battle Tower Upper Floors", world)
    create_region_helper("Battle Tower Ultra Lower Floors", world)
    create_region_helper("Battle Tower Ultra Upper Floors", world)
    create_region_helper("Arena of Despair", world)

    create_region_helper("First Island", world)
    create_region_helper("Second Island", world)
    create_region_helper("Third Island", world)
    create_region_helper("Fourth Island", world)
    create_region_helper("Fifth Island", world)

    create_region_helper("Cottage", world)
    create_region_helper("Beach House", world)
    create_region_helper("Hospital", world)
    create_region_helper("Fun House", world)
    create_region_helper("Factory", world)
    create_region_helper("Hopes Peak", world)

    create_region_helper("Monokids Hope", world)
    create_region_helper("Monosukes Hope", world)
    create_region_helper("Monodams Hope", world)
    create_region_helper("Monophanies Hope", world)
    create_region_helper("Monotaros Hope", world)
    create_region_helper("Graduation", world)



## Connector Helper
def connector_help(world: DanganronpaSWorld, parent:Region, target:Region, rule = None) -> None:
    entrance = Entrance(world.player, f"{parent.name} => {target.name}", parent=parent)
    parent.exits.append(entrance)
    entrance.connect(target)

    entrance = Entrance(world.player, f"{target.name} => {parent.name}",parent=target)
    target.exits.append(entrance)
    entrance.connect(parent)



## connecting regions
def connect_regions(world: DanganronpaSWorld) -> None:
    Menu = world.get_region("Menu")

    Gacha1 = world.get_region("Gacha1")
    Gacha2 = world.get_region("Gacha2")
    Gacha3 = world.get_region("Gacha3")
    Gacha4 = world.get_region("Gacha4")
    Gacha5 = world.get_region("Gacha5")
    Gacha6 = world.get_region("Gacha6")
    Gacha7 = world.get_region("Gacha7")
    Gacha8 = world.get_region("Gacha8")
    Gacha9 = world.get_region("Gacha9")
    Gacha10 = world.get_region("Gacha10")
    Gacha11 = world.get_region("Gacha11")
    Gacha12 = world.get_region("Gacha12")
    Gacha13 = world.get_region("Gacha13")
    Gacha14 = world.get_region("Gacha14")
    Gacha15 = world.get_region("Gacha15")

    Battle_Tower_Lower_Floor = world.get_region("Battle Tower Lower Floor")
    Battle_Tower_Upper_Floor = world.get_region("Battle Tower Upper Floor")
    Battle_Tower_Lower_Ultimate_Floor = world.get_region("Battle Tower Lower Ultimate Floor")
    Battle_Tower_Upper_Ultimate_Floor = world.get_region("Battle Tower Upper Ultimate Floor")
    Arena_of_Despair = world.get_region("Arena of Despair")

    The_First_Island = world.get_region("The First Island")
    The_Second_Island = world.get_region("The Second Island")
    The_Third_Island = world.get_region("The Third Island")
    The_Fourth_Island = world.get_region("The Fourth Island")
    The_Fifth_Island = world.get_region("The Fifth Island")

    Cottage = world.get_region("Cottage")
    Beach_House = world.get_region("Beach House")
    Hospital = world.get_region("Hospital")
    Fun_House = world.get_region("Fun House")
    Factory = world.get_region("Factory")
    Hopes_Peak = world.get_region("Hopes Peak")

    Monokids_Hope = world.get_region("Monokids Hope")
    Monosukes_Hope = world.get_region("Monossukes Hope")
    Monodams_Hope = world.get_region("Monodams Hope")
    Monophanies_Hope = world.get_region("Monophanies Hope")
    Monotaros_Hope = world.get_region("Monotaros Hope")
    Graduation = world.get_region("Graduation")



##I hate having to define the fuckin' doors
    connector_help(world, Menu, Gacha1)
    connector_help(world, Menu, Gacha2)
    connector_help(world, Menu, Gacha3)
    connector_help(world, Menu, Gacha4)
    connector_help(world, Menu, Gacha5)
    connector_help(world, Menu, Gacha6)
    connector_help(world, Menu, Gacha7)
    connector_help(world, Menu, Gacha8)
    connector_help(world, Menu, Gacha9)
    connector_help(world, Menu, Gacha10)
    connector_help(world, Menu, Gacha11)
    connector_help(world, Menu, Gacha12)
    connector_help(world, Menu, Gacha13)
    connector_help(world, Menu, Gacha14)
    connector_help(world, Menu, Gacha15)

    connector_help(world, Menu, Battle_Tower_Lower_Floor)
    connector_help(world, Battle_Tower_Lower_Floor, Battle_Tower_Upper_Floor)
    connector_help(world, Battle_Tower_Upper_Floor, Battle_Tower_Lower_Ultimate_Floor)
    connector_help(world, Battle_Tower_Upper_Floor, Arena_of_Despair)
    connector_help(world, Battle_Tower_Lower_Ultimate_Floor, Battle_Tower_Upper_Ultimate_Floor)

    connector_help(world, Menu, The_First_Island)
    connector_help(world, The_First_Island, The_Second_Island)
    connector_help(world, The_First_Island, Cottage)
    connector_help(world, The_Second_Island, The_Third_Island)
    connector_help(world, The_Second_Island, Beach_House)
    connector_help(world, The_Third_Island, The_Fourth_Island)
    connector_help(world, The_Third_Island, Hospital)
    connector_help(world, The_Fourth_Island, The_Fifth_Island)
    connector_help(world, The_Fourth_Island, Fun_House)
    connector_help(world, The_Fifth_Island, Factory)
    connector_help(world, The_Fifth_Island, Hopes_Peak)

    connector_help(world, Menu, Monokids_Hope)
    connector_help(world, Monokids_Hope, Monosukes_Hope)
    connector_help(world, Monosukes_Hope, Monodams_Hope)
    connector_help(world, Monodams_Hope, Monophanies_Hope)
    connector_help(world, Monophanies_Hope, Monotaros_Hope)
    connector_help(world, Monotaros_Hope, Graduation)

