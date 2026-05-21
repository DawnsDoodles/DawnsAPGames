import dataclasses
import enum
from dataclasses import dataclass, field
from typing import NamedTuple, Self


class DanganronpaGame(enum.StrEnum):
    TRIGGER_HAPPY_HAVOC = "Trigger Happy Havoc"
    DANGANRONPA_1 = TRIGGER_HAPPY_HAVOC
    GOODBYE_DESPAIR = "Goodbye Despair"
    DANGANRONPA_2 = GOODBYE_DESPAIR
    ULTRA_DESPAIR_GIRLS = "Ultra Despair Girls"
    UDG = ULTRA_DESPAIR_GIRLS
    KILLING_HARMONY = "Killing Harmony"
    DANGANRONPA_3 = KILLING_HARMONY


class CharacterMainStat(enum.StrEnum):
    BALANCED = "Balanced"
    ATHLETIC = "Athletic"
    CEREBRAL = "Cerebral"


class Gender(enum.StrEnum):
    MALE = "Male"
    FEMALE = "Female"


@dataclasses.dataclass(frozen=True)
class _CharacterData:
    char_name: str
    games_list: list[DanganronpaGame]
    main_stat: CharacterMainStat
    gender: Gender


class Character(enum.Enum):
    AKANE_OWARI = _CharacterData(char_name="Akane Owari", games_list=[DanganronpaGame.DANGANRONPA_2], main_stat=CharacterMainStat.ATHLETIC, gender=Gender.FEMALE)
    ANGIE_YONAGA = _CharacterData(char_name="Angie Yonaga", games_list=[DanganronpaGame.DANGANRONPA_3], main_stat=CharacterMainStat.BALANCED, gender=Gender.FEMALE)
    AOI_ASAHINA = _CharacterData(char_name="Aoi Asahina", games_list=[DanganronpaGame.DANGANRONPA_1], main_stat=CharacterMainStat.ATHLETIC, gender=Gender.FEMALE)
    BYAKUYA_TOGAMI = _CharacterData(char_name="Byakuya Togami", games_list=[DanganronpaGame.DANGANRONPA_1], main_stat=CharacterMainStat.CEREBRAL, gender=Gender.MALE)
    CELESTIA_LUDENBERG = _CharacterData(char_name="Celestia Ludenberg", games_list=[DanganronpaGame.DANGANRONPA_1], main_stat=CharacterMainStat.CEREBRAL, gender=Gender.FEMALE)
    CHIAKI_NANAMI = _CharacterData(char_name="Chiaki Nanami", games_list=[DanganronpaGame.DANGANRONPA_2], main_stat=CharacterMainStat.CEREBRAL, gender=Gender.FEMALE)
    CHIHIRO_FUJISAKI = _CharacterData(char_name="Chihiro Fujisaki", games_list=[DanganronpaGame.DANGANRONPA_1], main_stat=CharacterMainStat.CEREBRAL, gender=Gender.MALE)
    FUYUHIKO_KUZURYU = _CharacterData(char_name="Fuyuhiko Kuzuryu", games_list=[DanganronpaGame.DANGANRONPA_2], main_stat=CharacterMainStat.BALANCED, gender=Gender.MALE)
    GENOCIDE_JACK = _CharacterData(char_name="Genocide Jack", games_list=[DanganronpaGame.DANGANRONPA_1, DanganronpaGame.ULTRA_DESPAIR_GIRLS], main_stat=CharacterMainStat.ATHLETIC, gender=Gender.FEMALE)
    GONTA_GOKUHARA = _CharacterData(char_name="Gonta Gokuhara", games_list=[DanganronpaGame.DANGANRONPA_3], main_stat=CharacterMainStat.ATHLETIC, gender=Gender.MALE)
    GUNDHAM_TANAKA = _CharacterData(char_name="Gundham Tanaka", games_list=[DanganronpaGame.DANGANRONPA_3], main_stat=CharacterMainStat.BALANCED, gender=Gender.MALE)
    HAJIME_HINATA = _CharacterData(char_name="Hajime Hinata", games_list=[DanganronpaGame.DANGANRONPA_2], main_stat=CharacterMainStat.ATHLETIC, gender=Gender.MALE)
    HIFUMI_YAMADA = _CharacterData(char_name="Hifumi Yamada", games_list=[DanganronpaGame.DANGANRONPA_1], main_stat=CharacterMainStat.BALANCED, gender=Gender.MALE)
    HIMIKO_YUMENO = _CharacterData(char_name="Himiko Yumeno", games_list=[DanganronpaGame.DANGANRONPA_3], main_stat=CharacterMainStat.BALANCED, gender=Gender.FEMALE)
    HIROKO_HAGAKURE = _CharacterData(char_name="Hiroko Hagakure", games_list=[DanganronpaGame.ULTRA_DESPAIR_GIRLS], main_stat=CharacterMainStat.ATHLETIC, gender=Gender.FEMALE)
    HIYOKO_SAIONJI = _CharacterData(char_name="Hiyoko Saionji", games_list=[DanganronpaGame.DANGANRONPA_2], main_stat=CharacterMainStat.BALANCED, gender=Gender.FEMALE)
    IBUKI_MIODA = _CharacterData(char_name="Ibuki Mioda", games_list=[DanganronpaGame.DANGANRONPA_2], main_stat=CharacterMainStat.BALANCED, gender=Gender.FEMALE)
    IZURU_KAMUKURA = _CharacterData(char_name="Izuru Kamukura", games_list=[DanganronpaGame.DANGANRONPA_2], main_stat=CharacterMainStat.ATHLETIC, gender=Gender.MALE)
    JATARO_KEMURI = _CharacterData(char_name="Jataro Kemuri", games_list=[DanganronpaGame.ULTRA_DESPAIR_GIRLS], main_stat=CharacterMainStat.BALANCED, gender=Gender.MALE)
    JUNKO_ENOSHIMA = _CharacterData(char_name="Junko Enoshima", games_list=[DanganronpaGame.DANGANRONPA_1], main_stat=CharacterMainStat.CEREBRAL, gender=Gender.FEMALE)
    K1_B0 = _CharacterData(char_name="K1-B0", games_list=[DanganronpaGame.DANGANRONPA_3], main_stat=CharacterMainStat.BALANCED, gender=Gender.MALE)
    KAEDE_AKAMATSU = _CharacterData(char_name="Kaede Akamatsu", games_list=[DanganronpaGame.DANGANRONPA_3], main_stat=CharacterMainStat.BALANCED, gender=Gender.FEMALE)
    KAITO_MOMOTA = _CharacterData(char_name="Kaito Momota", games_list=[DanganronpaGame.DANGANRONPA_3], main_stat=CharacterMainStat.ATHLETIC, gender=Gender.MALE)
    KAZUICHI_SODA = _CharacterData(char_name="Kazuichi Soda", games_list=[DanganronpaGame.DANGANRONPA_2], main_stat=CharacterMainStat.CEREBRAL, gender=Gender.MALE)
    KIRUMI_TOJO = _CharacterData(char_name="Kirumi Tojo", games_list=[DanganronpaGame.DANGANRONPA_3], main_stat=CharacterMainStat.CEREBRAL, gender=Gender.FEMALE)
    KIYOTAKA_ISHIMARU = _CharacterData(char_name="Kiyotaka Ishimaru", games_list=[DanganronpaGame.DANGANRONPA_1], main_stat=CharacterMainStat.BALANCED, gender=Gender.MALE)
    KOKICHI_OMA = _CharacterData(char_name="Kokichi Oma", games_list=[DanganronpaGame.DANGANRONPA_3], main_stat=CharacterMainStat.CEREBRAL, gender=Gender.MALE)
    KOMARU_NAEGI = _CharacterData(char_name="Komaru Naegi", games_list=[DanganronpaGame.ULTRA_DESPAIR_GIRLS], main_stat=CharacterMainStat.ATHLETIC, gender=Gender.FEMALE)
    KOREKIYO_SHINGUJI = _CharacterData(char_name="Korekiyo Shinguji", games_list=[DanganronpaGame.DANGANRONPA_3], main_stat=CharacterMainStat.CEREBRAL, gender=Gender.MALE)
    KOTOKO_UTSUGI = _CharacterData(char_name="Kotoko Utsugi", games_list=[DanganronpaGame.ULTRA_DESPAIR_GIRLS], main_stat=CharacterMainStat.BALANCED, gender=Gender.FEMALE)
    KUROKUMA = _CharacterData(char_name="Kurokuma", games_list=[DanganronpaGame.ULTRA_DESPAIR_GIRLS], main_stat=CharacterMainStat.BALANCED, gender=Gender.MALE)
    KYOKO_KIRIGIRI = _CharacterData(char_name="Kyoko Kirigiri", games_list=[DanganronpaGame.DANGANRONPA_1], main_stat=CharacterMainStat.CEREBRAL, gender=Gender.FEMALE)
    LEON_KUWATA = _CharacterData(char_name="Leon Kuwata", games_list=[DanganronpaGame.DANGANRONPA_1], main_stat=CharacterMainStat.ATHLETIC, gender=Gender.MALE)
    MAHIRU_KOIZUMI = _CharacterData(char_name="Mahiru Koizumi", games_list=[DanganronpaGame.DANGANRONPA_2], main_stat=CharacterMainStat.CEREBRAL, gender=Gender.FEMALE)
    MAKI_HARUKAWA = _CharacterData(char_name="Maki Harukawa", games_list=[DanganronpaGame.DANGANRONPA_3], main_stat=CharacterMainStat.ATHLETIC, gender=Gender.FEMALE)
    MAKOTO_NAEGI = _CharacterData(char_name="Makoto Naegi", games_list=[DanganronpaGame.DANGANRONPA_1], main_stat=CharacterMainStat.BALANCED, gender=Gender.MALE)
    MASARU_DAIMON = _CharacterData(char_name="Masaru Daimon", games_list=[DanganronpaGame.ULTRA_DESPAIR_GIRLS], main_stat=CharacterMainStat.ATHLETIC, gender=Gender.MALE)
    MIKAN_TSUMIKI = _CharacterData(char_name="Mikan Tsumiki", games_list=[DanganronpaGame.DANGANRONPA_2], main_stat=CharacterMainStat.BALANCED, gender=Gender.FEMALE)
    MIU_IRUMA = _CharacterData(char_name="Miu Iruma", games_list=[DanganronpaGame.DANGANRONPA_3], main_stat=CharacterMainStat.CEREBRAL, gender=Gender.FEMALE)
    MONACA_TOWA = _CharacterData(char_name="Monaca Towa", games_list=[DanganronpaGame.ULTRA_DESPAIR_GIRLS], main_stat=CharacterMainStat.CEREBRAL, gender=Gender.FEMALE)
    MONDO_OWADA = _CharacterData(char_name="Mondo Owada", games_list=[DanganronpaGame.DANGANRONPA_1], main_stat=CharacterMainStat.ATHLETIC, gender=Gender.MALE)
    MONOKUMA = _CharacterData(char_name="Monokuma", games_list=[DanganronpaGame.DANGANRONPA_1], main_stat=CharacterMainStat.ATHLETIC, gender=Gender.MALE)
    MONOMI = _CharacterData(char_name="Monomi", games_list=[DanganronpaGame.DANGANRONPA_2], main_stat=CharacterMainStat.BALANCED, gender=Gender.FEMALE)
    MUKURO_IKUSABA = _CharacterData(char_name="Mukuro Ikusaba", games_list=[DanganronpaGame.DANGANRONPA_1], main_stat=CharacterMainStat.ATHLETIC, gender=Gender.FEMALE)
    NAGISA_SHINGETSU = _CharacterData(char_name="Nagisa Shingetsu", games_list=[DanganronpaGame.ULTRA_DESPAIR_GIRLS], main_stat=CharacterMainStat.CEREBRAL, gender=Gender.MALE)
    NAGITO_KOMAEDA = _CharacterData(char_name="Nagito Komaeda", games_list=[DanganronpaGame.DANGANRONPA_2], main_stat=CharacterMainStat.BALANCED, gender=Gender.MALE)
    NEKOMARU_NIDAI = _CharacterData(char_name="Nekomaru Nidai", games_list=[DanganronpaGame.DANGANRONPA_2], main_stat=CharacterMainStat.ATHLETIC, gender=Gender.MALE)
    PEKO_PEKOYAMA = _CharacterData(char_name="Peko Pekoyama", games_list=[DanganronpaGame.DANGANRONPA_2], main_stat=CharacterMainStat.ATHLETIC, gender=Gender.FEMALE)
    RANTARO_AMAMI = _CharacterData(char_name="Rantaro Amami", games_list=[DanganronpaGame.DANGANRONPA_3], main_stat=CharacterMainStat.BALANCED, gender=Gender.MALE)
    RYOMA_HOSHI = _CharacterData(char_name="Ryoma Hoshi", games_list=[DanganronpaGame.DANGANRONPA_3], main_stat=CharacterMainStat.ATHLETIC, gender=Gender.MALE)
    SAKURA_OGAMI = _CharacterData(char_name="Sakura Ogami", games_list=[DanganronpaGame.DANGANRONPA_1], main_stat=CharacterMainStat.ATHLETIC, gender=Gender.FEMALE)
    SAYAKA_MAIZONO = _CharacterData(char_name="Sayaka Maizono", games_list=[DanganronpaGame.DANGANRONPA_1], main_stat=CharacterMainStat.BALANCED, gender=Gender.FEMALE)
    SHIROKUMA = _CharacterData(char_name="Shirokuma", games_list=[DanganronpaGame.ULTRA_DESPAIR_GIRLS], main_stat=CharacterMainStat.CEREBRAL, gender=Gender.MALE)
    SHUICHI_SAIHARA = _CharacterData(char_name="Shuichi Saihara", games_list=[DanganronpaGame.DANGANRONPA_3], main_stat=CharacterMainStat.CEREBRAL, gender=Gender.MALE)
    SONIA_NEVERMIND = _CharacterData(char_name="Sonia Nevermind", games_list=[DanganronpaGame.DANGANRONPA_2], main_stat=CharacterMainStat.CEREBRAL, gender=Gender.FEMALE)
    TENKO_CHABASHIRA = _CharacterData(char_name="Tenko Chabashira", games_list=[DanganronpaGame.DANGANRONPA_3], main_stat=CharacterMainStat.ATHLETIC, gender=Gender.FEMALE)
    TERUTERU_HANAMURA = _CharacterData(char_name="Teruteru Hanamura", games_list=[DanganronpaGame.DANGANRONPA_2], main_stat=CharacterMainStat.BALANCED, gender=Gender.MALE)
    THE_ULTIMATE_IMPOSTER = _CharacterData(char_name="The Ultimate Imposter", games_list=[DanganronpaGame.DANGANRONPA_2], main_stat=CharacterMainStat.CEREBRAL, gender=Gender.MALE)
    TOKO_FUKAWA = _CharacterData(char_name="Toko Fukawa", games_list=[DanganronpaGame.DANGANRONPA_1, DanganronpaGame.ULTRA_DESPAIR_GIRLS], main_stat=CharacterMainStat.CEREBRAL, gender=Gender.FEMALE)
    TSUMUGI_SHIROGANE = _CharacterData(char_name="Tsumugi Shirogane", games_list=[DanganronpaGame.DANGANRONPA_3], main_stat=CharacterMainStat.CEREBRAL, gender=Gender.FEMALE)
    USAMI = _CharacterData(char_name="Usami", games_list=[DanganronpaGame.DANGANRONPA_2], main_stat=CharacterMainStat.CEREBRAL, gender=Gender.FEMALE)
    YASUHIRO_HAGAKURE = _CharacterData(char_name="Yasuhiro Hagakure", games_list=[DanganronpaGame.DANGANRONPA_1], main_stat=CharacterMainStat.BALANCED, gender=Gender.MALE)

    def __new__(cls, info: _CharacterData) -> Self:
        obj = object.__new__(cls)
        obj._value_ = info
        return obj

    def __init__(self, info: _CharacterData) -> None:
        self.char_name: str = info.char_name
        self.games_list: list[DanganronpaGame] = info.games_list
        self.main_stat: CharacterMainStat = info.main_stat
        self.gender: Gender = info.gender

    @property
    def main_game(self) -> DanganronpaGame:
        return self.games_list[0]


class CharacterRarity(enum.StrEnum):
    NORMAL = "N"
    N = NORMAL
    RARE = "R"
    R = RARE
    SUPER_RARE = "S"
    S = SUPER_RARE
    ULTRA_RARE = "U"
    U = ULTRA_RARE


class MonoKub(enum.StrEnum):
    MONOKID = "Monokid"
    MONOSUKE = "Monosuke"
    MONODAM = "Monodam"
    MONOPHANIE = "Monophanie"
    MONOTARO = "Monotaro"


class HypeCardType(enum.StrEnum):
    RECOVER_INFLUENCE = "Recover 10% Influence/Turn"
    DAMAGE_DEALT = "Damage Dealt +10%"
    DAMAGE_TAKEN = "Damage Taken -10%"
    BREAK_DAMAGE_CAP = "Break Damage Cap"
    FOCUS_MAX = "Focus Max +3"
    AWAKENING_BONUS = "Awakening Bonus +20%"
    FOCUS_REGEN = "Focus Regen +1"
    EQUIPMENT_STATS = "Equipment Stats +10%"
    BREAK_ATTRIBUTE_CAP = "Break Attribute Cap"


class CraftingMaterialQuality(enum.StrEnum):
    SMALL = "Small"
    NORMAL = ""
    BIG = "Big"
    STURDY = "Sturdy"
    DIVINE = "Divine"
    LAVISH = "Lavish"
    COPPER = "Copper"
    SILVER = "Silver"
    GOLD = "Gold"
    PLATINUM = "Platinum"


class CraftingMaterialType(enum.StrEnum):
    MONSTER_FANG = "Monster Fang"
    MONSTER_MEAT = "Monster Meat"
    MONSTER_EYE = "Monster Eye"
    MONSTER_FUR = "Monster Fur"
    MONSTER_SKIN = "Monster Skin"


@dataclasses.dataclass
class CraftingMaterial:
    quality: CraftingMaterialQuality
    type: CraftingMaterialType

    @property
    def material_name(self) -> str:
        result: str = f"{self.quality}"
        if self.quality != CraftingMaterialQuality.NORMAL:
           result += " "
        result += f"{self.type}"
        return result


crafting_materials: dict[CraftingMaterialType, dict[CraftingMaterialQuality, CraftingMaterial]] = \
{
    material_type:
        {
            material_quality: CraftingMaterial(quality=material_quality, type=material_type)
            for material_quality in CraftingMaterialQuality
        }
    for material_type in CraftingMaterialType
}


@dataclasses.dataclass(frozen=True)
class _CraftedItemData:
    item_name: str
    prereq_item_name: str
    material_list: list[CraftingMaterial]
    influence: int
    focus: int
    strength: int
    stamina: int
    intellect: int
    endurance: int
    agility: int
    luck: int


class CraftedItem(enum.Enum):
    ARMY_KNIFE = _CraftedItemData(item_name="Army Knife", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.GOLD]], influence=-30, focus=0, strength=50, stamina=-50, intellect=0, endurance=0, agility=100, luck=150)
    CROSSBOW = _CraftedItemData(item_name="Crossbow", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.GOLD]], influence=0, focus=0, strength=200, stamina=-100, intellect=-100, endurance=200, agility=0, luck=0)
    DUMBBELL = _CraftedItemData(item_name="Dumbbell", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.COPPER]], influence=30, focus=0, strength=50, stamina=70, intellect=-50, endurance=0, agility=100, luck=0)
    GOLD_LEAF_KATANA = _CraftedItemData(item_name="Gold Leaf Katana", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.SILVER]], influence=0, focus=0, strength=150, stamina=-50, intellect=0, endurance=-50, agility=0, luck=0)
    HACKING_GUN = _CraftedItemData(item_name="Hacking Gun", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.SMALL], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.NORMAL]], influence=0, focus=0, strength=0, stamina=0, intellect=50, endurance=0, agility=0, luck=0)
    HACKING_GUN_EXTREME = _CraftedItemData(item_name="Hacking Gun Extreme", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.STURDY]], influence=0, focus=0, strength=0, stamina=0, intellect=150, endurance=0, agility=0, luck=0)
    HACKING_GUN_V3 = _CraftedItemData(item_name="Hacking Gun V3", prereq_item_name="V Hacking Gun", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.DIVINE], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.LAVISH]], influence=0, focus=0, strength=30, stamina=30, intellect=300, endurance=30, agility=30, luck=30)
    HAMMER = _CraftedItemData(item_name="Hammer", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.SILVER]], influence=0, focus=0, strength=-50, stamina=150, intellect=-50, endurance=50, agility=-100, luck=0)
    HAT_OF_HOPE = _CraftedItemData(item_name="Hat of Hope", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.LAVISH]], influence=80, focus=0, strength=80, stamina=80, intellect=80, endurance=80, agility=80, luck=80)
    HAT_OF_LEGEND = _CraftedItemData(item_name="Hat of Legend", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.STURDY], crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.LAVISH]], influence=100, focus=0, strength=100, stamina=100, intellect=100, endurance=100, agility=100, luck=100)
    HAT_OF_OVERFLOWING_TALENT = _CraftedItemData(item_name="Hat of Overflowing Talent", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.NORMAL], crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.BIG]], influence=40, focus=0, strength=40, stamina=40, intellect=40, endurance=40, agility=40, luck=40)
    HAT_V3 = _CraftedItemData(item_name="Hat V3", prereq_item_name="Ultimate Hat", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.DIVINE]], influence=130, focus=0, strength=130, stamina=130, intellect=130, endurance=130, agility=130, luck=130)
    HIGH_SCHOOLERS_HAT = _CraftedItemData(item_name="High Schooler's Hat", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.SMALL], crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.NORMAL]], influence=20, focus=0, strength=20, stamina=20, intellect=20, endurance=20, agility=20, luck=20)
    HIGH_SCHOOLERS_SHOES = _CraftedItemData(item_name="High Schooler's Shoes", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.SMALL], crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.NORMAL]], influence=0, focus=0, strength=0, stamina=0, intellect=0, endurance=0, agility=70, luck=0)
    HIGH_SCHOOLERS_TALISMAN = _CraftedItemData(item_name="High Schooler's Talisman", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.SMALL], crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.NORMAL]], influence=0, focus=0, strength=0, stamina=0, intellect=0, endurance=0, agility=0, luck=70)
    HIGH_SCHOOLERS_UNIFORM = _CraftedItemData(item_name="High Schooler's Uniform", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.SMALL], crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.NORMAL]], influence=70, focus=0, strength=0, stamina=0, intellect=0, endurance=0, agility=0, luck=0)
    SHOES_OF_LEGEND = _CraftedItemData(item_name="Shoes of Legend", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.STURDY], crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.LAVISH]], influence=0, focus=0, strength=0, stamina=0, intellect=0, endurance=0, agility=250, luck=0)
    HYDRAULIC_PRESS = _CraftedItemData(item_name="Hydraulic Press", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.GOLD], crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.GOLD], crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.GOLD]], influence=-50, focus=0, strength=250, stamina=250, intellect=250, endurance=250, agility=-999, luck=-999)
    IRON_SKEWER = _CraftedItemData(item_name="Iron Skewer", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.COPPER], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.COPPER]], influence=0, focus=0, strength=-50, stamina=0, intellect=-50, endurance=150, agility=0, luck=0)
    JUSTICE_HAMMER = _CraftedItemData(item_name="JUSTICE HAMMER", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.COPPER]], influence=0, focus=0, strength=-50, stamina=0, intellect=-50, endurance=100, agility=0, luck=0)
    KATANA = _CraftedItemData(item_name="Katana", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.SMALL], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.NORMAL]], influence=0, focus=0, strength=50, stamina=0, intellect=0, endurance=0, agility=0, luck=0)
    KATANA_EXTREME = _CraftedItemData(item_name="Katana Extreme", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.STURDY]], influence=0, focus=0, strength=150, stamina=0, intellect=0, endurance=0, agility=0, luck=0)
    KATANA_V3 = _CraftedItemData(item_name="Katana V3", prereq_item_name="V Katana", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.DIVINE], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.LAVISH]], influence=0, focus=0, strength=300, stamina=30, intellect=30, endurance=30, agility=30, luck=30)
    KITCHEN_KNIFE = _CraftedItemData(item_name="Kitchen Knife", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.COPPER]], influence=0, focus=0, strength=20, stamina=-50, intellect=50, endurance=-50, agility=0, luck=-50)
    METAL_BAT = _CraftedItemData(item_name="Metal Bat", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.SILVER]], influence=0, focus=0, strength=120, stamina=-50, intellect=-50, endurance=-50, agility=100, luck=0)
    MONOKUMAS_SPECIAL_POISON = _CraftedItemData(item_name="Monokuma's Special Poison", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.GOLD]], influence=-20, focus=0, strength=50, stamina=50, intellect=100, endurance=100, agility=0, luck=-200)
    PIRANHA = _CraftedItemData(item_name="Piranha", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.SILVER]], influence=0, focus=0, strength=-50, stamina=0, intellect=150, endurance=-50, agility=0, luck=0)
    POISON = _CraftedItemData(item_name="Poison", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.COPPER]], influence=-60, focus=0, strength=120, stamina=50, intellect=-100, endurance=-120, agility=20, luck=0)
    REPLICA_SWORD = _CraftedItemData(item_name="Replica Sword", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.COPPER]], influence=0, focus=0, strength=50, stamina=-50, intellect=0, endurance=-50, agility=20, luck=-50)
    ROPE_USED_FOR_HANGING = _CraftedItemData(item_name="Rope Used for Hanging", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.SILVER]], influence=-50, focus=0, strength=0, stamina=0, intellect=150, endurance=150, agility=0, luck=-100)
    SCISSORS = _CraftedItemData(item_name="Scissors", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.GOLD], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.GOLD], crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.GOLD]], influence=0, focus=0, strength=150, stamina=0, intellect=-50, endurance=-50, agility=150, luck=0)
    SHIELD = _CraftedItemData(item_name="Shield", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.SMALL], crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.NORMAL]], influence=0, focus=0, strength=0, stamina=50, intellect=0, endurance=0, agility=0, luck=0)
    SHIELD_EXTREME = _CraftedItemData(item_name="Shield Extreme", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.STURDY]], influence=0, focus=0, strength=0, stamina=150, intellect=0, endurance=0, agility=0, luck=0)
    SHIELD_V3 = _CraftedItemData(item_name="Shield V3", prereq_item_name="V Shield", material_list=[crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.DIVINE], crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.LAVISH]], influence=0, focus=0, strength=30, stamina=300, intellect=30, endurance=30, agility=30, luck=30)
    SHOES_OF_HOPE = _CraftedItemData(item_name="Shoes of Hope", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.LAVISH]], influence=0, focus=0, strength=0, stamina=0, intellect=0, endurance=0, agility=200, luck=0)
    SHOES_OF_OVERFLOWING_TALENT = _CraftedItemData(item_name="Shoes of Overflowing Talent", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.NORMAL], crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.BIG]], influence=0, focus=0, strength=0, stamina=0, intellect=0, endurance=0, agility=100, luck=0)
    SHOES_V3 = _CraftedItemData(item_name="Shoes V3", prereq_item_name="Ultimate Shoes", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.DIVINE]], influence=300, focus=0, strength=10, stamina=10, intellect=10, endurance=10, agility=10, luck=10)
    SHOT_PUT_BALL = _CraftedItemData(item_name="Shot Put Ball", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.SILVER]], influence=0, focus=0, strength=-50, stamina=200, intellect=-50, endurance=0, agility=-100, luck=-100)
    SICKLE = _CraftedItemData(item_name="Sickle", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.GOLD]], influence=0, focus=0, strength=-50, stamina=0, intellect=50, endurance=150, agility=0, luck=0)
    SPEARS_OF_GUNGNIR = _CraftedItemData(item_name="Spears of Gungnir", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.GOLD]], influence=0, focus=0, strength=150, stamina=150, intellect=-50, endurance=-50, agility=0, luck=-50)
    STAFF = _CraftedItemData(item_name="Staff", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.SILVER]], influence=0, focus=0, strength=0, stamina=0, intellect=0, endurance=50, agility=0, luck=0)
    STAFF_EXTREME = _CraftedItemData(item_name="Staff Extreme", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.STURDY]], influence=0, focus=0, strength=0, stamina=0, intellect=0, endurance=150, agility=0, luck=0)
    STAFF_V3 = _CraftedItemData(item_name="Staff V3", prereq_item_name="V Staff", material_list=[crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.DIVINE], crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.LAVISH]], influence=0, focus=0, strength=30, stamina=30, intellect=30, endurance=300, agility=30, luck=30)
    SUPER_HACKING_GUN = _CraftedItemData(item_name="Super Hacking Gun", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.SMALL], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.NORMAL]], influence=0, focus=0, strength=0, stamina=0, intellect=70, endurance=0, agility=0, luck=0)
    SUPER_KATANA = _CraftedItemData(item_name="Super Katana", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.NORMAL], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.BIG]], influence=0, focus=0, strength=70, stamina=0, intellect=0, endurance=0, agility=0, luck=0)
    SUPER_SHIELD = _CraftedItemData(item_name="Super Shield", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.NORMAL], crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.BIG]], influence=0, focus=0, strength=0, stamina=70, intellect=0, endurance=0, agility=0, luck=0)
    SUPER_STAFF = _CraftedItemData(item_name="Super Staff", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.NORMAL], crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.BIG]], influence=0, focus=0, strength=0, stamina=0, intellect=0, endurance=70, agility=0, luck=0)
    TALISMAN_OF_HOPE = _CraftedItemData(item_name="Talisman of Hope", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.LAVISH]], influence=0, focus=0, strength=0, stamina=0, intellect=0, endurance=0, agility=0, luck=200)
    TALISMAN_OF_LEGEND = _CraftedItemData(item_name="Talisman of Legend", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.STURDY], crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.LAVISH]], influence=0, focus=0, strength=0, stamina=0, intellect=0, endurance=0, agility=0, luck=250)
    TALISMAN_OF_OVERFLOWING_TALENT = _CraftedItemData(item_name="Talisman of Overflowing Talent", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.NORMAL], crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.BIG]], influence=0, focus=0, strength=0, stamina=0, intellect=0, endurance=0, agility=0, luck=100)
    TALISMAN_V3 = _CraftedItemData(item_name="Talisman V3", prereq_item_name="Ultimate Talisman", material_list=[crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.DIVINE]], influence=10, focus=0, strength=10, stamina=10, intellect=10, endurance=10, agility=10, luck=300)
    TATTERED_HAT = _CraftedItemData(item_name="Tattered Hat", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.SMALL]], influence=10, focus=0, strength=10, stamina=10, intellect=10, endurance=10, agility=10, luck=10)
    TATTERED_SHOES = _CraftedItemData(item_name="Tattered Shoes", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.SMALL]], influence=0, focus=0, strength=0, stamina=0, intellect=0, endurance=0, agility=30, luck=0)
    TATTERED_TALISMAN = _CraftedItemData(item_name="Tattered Talisman", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.SMALL]], influence=0, focus=0, strength=0, stamina=0, intellect=0, endurance=0, agility=0, luck=30)
    TATTERED_UNIFORM = _CraftedItemData(item_name="Tattered Uniform", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.SMALL]], influence=30, focus=0, strength=0, stamina=0, intellect=0, endurance=0, agility=0, luck=0)
    THE_END_OF_HACKING_GUN = _CraftedItemData(item_name="The End of Hacking Gun", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.DIVINE], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.LAVISH]], influence=0, focus=0, strength=0, stamina=0, intellect=200, endurance=0, agility=0, luck=0)
    THE_END_OF_KATANA = _CraftedItemData(item_name="The End of Katana", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.DIVINE], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.LAVISH]], influence=0, focus=0, strength=200, stamina=0, intellect=0, endurance=0, agility=0, luck=0)
    THE_END_OF_SHIELD = _CraftedItemData(item_name="The End of Shield", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.LAVISH], crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.STURDY]], influence=0, focus=0, strength=0, stamina=200, intellect=0, endurance=0, agility=0, luck=0)
    THE_END_OF_STAFF = _CraftedItemData(item_name="The End of Staff", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.LAVISH], crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.STURDY]], influence=0, focus=0, strength=0, stamina=0, intellect=0, endurance=200, agility=0, luck=0)
    TOILET_PAPER = _CraftedItemData(item_name="Toilet Paper", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.GOLD]], influence=0, focus=0, strength=-50, stamina=200, intellect=200, endurance=-50, agility=0, luck=0)
    ULTIMATE_____PROOF = _CraftedItemData(item_name="Ultimate ??? Proof", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.SILVER], crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.SILVER]], influence=25, focus=25, strength=25, stamina=0, intellect=0, endurance=0, agility=0, luck=0)
    ULTIMATE_AFFLUENT_PROGENY_PROOF = _CraftedItemData(item_name="Ultimate Affluent Progeny Proof", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.COPPER], crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.COPPER]], influence=30, focus=0, strength=0, stamina=20, intellect=25, endurance=0, agility=0, luck=0)
    ULTIMATE_CHILD_CAREGIVER_PROOF = _CraftedItemData(item_name="Ultimate Child Caregiver Proof", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.GOLD], crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.GOLD]], influence=0, focus=30, strength=0, stamina=0, intellect=0, endurance=30, agility=15, luck=0)
    ULTIMATE_CLAIRVOYANT_PROOF = _CraftedItemData(item_name="Ultimate Clairvoyant Proof", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.COPPER], crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.COPPER]], influence=0, focus=25, strength=0, stamina=0, intellect=25, endurance=25, agility=0, luck=0)
    ULTIMATE_DESPAIR_PROOF = _CraftedItemData(item_name="Ultimate Despair Proof", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.PLATINUM], crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.PLATINUM], crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.PLATINUM]], influence=75, focus=75, strength=0, stamina=0, intellect=0, endurance=0, agility=0, luck=0)
    ULTIMATE_DETECTIVE_PROOF = _CraftedItemData(item_name="Ultimate Detective Proof", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.COPPER], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.COPPER]], influence=20, focus=0, strength=0, stamina=0, intellect=55, endurance=0, agility=0, luck=0)
    ULTIMATE_GYMNAST_PROOF = _CraftedItemData(item_name="Ultimate Gymnast Proof", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.SILVER], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.SILVER]], influence=0, focus=25, strength=25, stamina=25, intellect=0, endurance=0, agility=0, luck=0)
    ULTIMATE_HAT = _CraftedItemData(item_name="Ultimate Hat", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.STURDY]], influence=60, focus=0, strength=60, stamina=60, intellect=60, endurance=60, agility=60, luck=60)
    ULTIMATE_HOPE_PROOF = _CraftedItemData(item_name="Ultimate Hope Proof", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.SILVER], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.PLATINUM], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.GOLD], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.COPPER]], influence=30, focus=30, strength=15, stamina=15, intellect=15, endurance=15, agility=15, luck=15)
    ULTIMATE_LUCKY_STUDENT_PROOF = _CraftedItemData(item_name="Ultimate Lucky Student Proof", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.COPPER], crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.COPPER]], influence=25, focus=0, strength=0, stamina=0, intellect=0, endurance=0, agility=0, luck=50)
    ULTIMATE_MAGICIAN_PROOF = _CraftedItemData(item_name="Ultimate Magician Proof", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.GOLD], crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.GOLD]], influence=0, focus=25, strength=0, stamina=0, intellect=25, endurance=15, agility=0, luck=10)
    ULTIMATE_MECHANIC_PROOF = _CraftedItemData(item_name="Ultimate Mechanic Proof", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.SILVER], crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.SILVER]], influence=0, focus=20, strength=0, stamina=15, intellect=20, endurance=0, agility=0, luck=20)
    ULTIMATE_MURDEROUS_FIEND_PROOF = _CraftedItemData(item_name="Ultimate Murderous Fiend Proof", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.COPPER], crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.COPPER]], influence=20, focus=-10, strength=40, stamina=0, intellect=0, endurance=-10, agility=35, luck=0)
    ULTIMATE_PRINCESS_PROOF = _CraftedItemData(item_name="Ultimate Princess Proof", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.SILVER], crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.SILVER]], influence=50, focus=0, strength=0, stamina=0, intellect=15, endurance=10, agility=0, luck=0)
    ULTIMATE_SHOES = _CraftedItemData(item_name="Ultimate Shoes", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.STURDY]], influence=5, focus=0, strength=5, stamina=5, intellect=5, endurance=5, agility=150, luck=5)
    ULTIMATE_SWIMMING_PRO_PROOF = _CraftedItemData(item_name="Ultimate Swimming Pro Proof", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.COPPER], crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.COPPER]], influence=0, focus=10, strength=10, stamina=50, intellect=0, endurance=0, agility=0, luck=0)
    ULTIMATE_TALISMAN = _CraftedItemData(item_name="Ultimate Talisman", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.STURDY]], influence=5, focus=0, strength=5, stamina=5, intellect=5, endurance=5, agility=5, luck=150)
    ULTIMATE_UNIFORM = _CraftedItemData(item_name="Ultimate Uniform", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.STURDY]], influence=150, focus=0, strength=5, stamina=5, intellect=5, endurance=5, agility=5, luck=5)
    ULTIMATE_WRITING_PRODIGY_PROOF = _CraftedItemData(item_name="Ultimate Writing Prodigy Proof", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.COPPER], crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.COPPER]], influence=0, focus=35, strength=0, stamina=0, intellect=25, endurance=15, agility=0, luck=0)
    ULTIMATE_YAKUZA_PROOF = _CraftedItemData(item_name="Ultimate Yakuza Proof", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.SILVER], crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.SILVER]], influence=20, focus=0, strength=0, stamina=15, intellect=0, endurance=40, agility=0, luck=0)
    UNIFORM_OF_HOPE = _CraftedItemData(item_name="Ultimate of Hope", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.LAVISH]], influence=200, focus=0, strength=0, stamina=0, intellect=0, endurance=0, agility=0, luck=0)
    UNIFORM_OF_LEGEND = _CraftedItemData(item_name="Uniform of Legend", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.STURDY], crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.LAVISH]], influence=250, focus=0, strength=0, stamina=0, intellect=0, endurance=0, agility=0, luck=0)
    UNIFORM_OF_OVERFLOWING_TALENT = _CraftedItemData(item_name="Uniform of Overflowing Talent", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.NORMAL], crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.BIG]], influence=100, focus=0, strength=0, stamina=0, intellect=0, endurance=0, agility=0, luck=0)
    UNIFORM_V3 = _CraftedItemData(item_name="Uniform V3", prereq_item_name="Ultimate Uniform", material_list=[crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.DIVINE]], influence=300, focus=0, strength=10, stamina=10, intellect=10, endurance=10, agility=10, luck=10)
    V_HACKING_GUN = _CraftedItemData(item_name="V Hacking Gun", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.STURDY]], influence=0, focus=0, strength=15, stamina=15, intellect=100, endurance=15, agility=15, luck=15)
    V_KATANA = _CraftedItemData(item_name="V Katana", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.STURDY]], influence=0, focus=0, strength=100, stamina=15, intellect=15, endurance=15, agility=15, luck=15)
    V_SHIELD = _CraftedItemData(item_name="V Shield", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.STURDY]], influence=0, focus=0, strength=15, stamina=100, intellect=15, endurance=15, agility=15, luck=15)
    V_STAFF = _CraftedItemData(item_name="V Staff", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.STURDY]], influence=0, focus=0, strength=15, stamina=15, intellect=15, endurance=100, agility=15, luck=15)
    WORN_HACKING_GUN = _CraftedItemData(item_name="Worn Hacking Gun", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.SMALL]], influence=0, focus=0, strength=0, stamina=0, intellect=30, endurance=0, agility=0, luck=0)
    WORN_KATANA = _CraftedItemData(item_name="Worn Katana", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.SMALL]], influence=0, focus=0, strength=30, stamina=0, intellect=0, endurance=0, agility=0, luck=0)
    WORN_SHIELD = _CraftedItemData(item_name="Worn Shield", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.SMALL]], influence=0, focus=0, strength=0, stamina=30, intellect=0, endurance=0, agility=0, luck=0)
    WORN_STAFF = _CraftedItemData(item_name="Worn Staff", prereq_item_name="", material_list=[crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.SMALL]], influence=0, focus=0, strength=0, stamina=0, intellect=0, endurance=30, agility=0, luck=0)

    def __new__(cls, info: _CraftedItemData) -> Self:
        obj = object.__new__(cls)
        obj._value_ = info
        return obj


    def __init__(self, info: _CraftedItemData) -> None:
        self.item_name: str = info.item_name
        self.prereq_item_name: str = info.prereq_item_name
        self.material_list: list[CraftingMaterial] = info.material_list
        self.influence: int = info.influence
        self.focus: int = info.focus
        self.strength: int = info.strength
        self.stamina: int = info.stamina
        self.intellect: int = info.intellect
        self.endurance: int = info.endurance
        self.agility: int = info.agility
        self.luck: int = info.luck


class Present(enum.StrEnum):
    STAR_BADGE = "3 Star Badge"
    ANCIENT_TOUR_TICKETS = "Ancient Tour Tickets"
    COMMEMORATIVE_MEDAL_SET = "Commemorative Medal Set"
    CRAZY_DIAMOND = "Crazy Diamond"
    DAGAN_WEREWOLF = "Dagan Werewolf"
    DATE_TICKET = "Date Ticket"
    EASTER_EGG = "Easter Egg"
    FRESH_BINDINGS = "Fresh Bindings"
    FUN_BOOK_OF_ANIMALS = "Fun Book of Animals"
    GAMERS_BACKPACK = "Gamer's Backpack"
    HAGAKURE_CRYSTAL_BALL = "Hagakure Crystal Ball"
    HAND_GRIPS = "Hand Grips"
    HELL_HOUND_EARRING = "Hell Hound Earring"
    HOPES_PEAK_RING = "Hope's Peak Ring"
    MACS_GLOVES = "Mac's Gloves"
    MEMORY_NOTEBOOK = "Memory Notebook"
    MILK_PUZZLE = "Milk Puzzle"
    POTATO_CHIPS = "Potato Chips"
    PROP_CARRYING_CASE = "Prop Carrying Case"
    PURE_WHITE_PRACTICE_SWORD = "Pure-White Practice Sword"
    REPLICA_SWORD = "Replica Sword"
    ROCK_PAPER_SCISSORS_CARDS = "Rock-Paper-Scissors Cards"
    SAFETY_HALF_SHOES = "Safety Half-Shoes"
    SCHOOL_CREST = "School Crest"
    SOMEONES_STUDENT_ID = "Someone's Student ID"
    SPY_SPIKE = "Spy Spike"
    SUPER_LUCKY_BUTTON = "Super Lucky Button"
    TEDDY_BEAR = "Teddy Bear"
    TIPS_AND_TIPS = "Tips & Tips"
    USAMI_STRAP = "Usami Strap"


class DevModeDungeon(enum.StrEnum):
    COTTAGE = "Cottage"
    BEACH_HOUSE = "Beach House"
    HOSPITAL = "Hospital"
    FUN_HOUSE = "Fun House"
    FACTORY = "Factory"


class DevModeLocation(enum.StrEnum):
    NO_LOCATION = "No Location"
    FIRST_ISLAND = "First Island"
    SECOND_ISLAND = "Second Island"
    THIRD_ISLAND = "Third Island"
    FOURTH_ISLAND = "Fourth Island"
    FIFTH_ISLAND = "Fifth Island"
    CENTRAL_ISLAND = "Central Island"
    COTTAGE = "Cottage"
    BEACH_HOUSE = "Beach House"
    HOSPITAL = "Hospital"
    FUN_HOUSE = "Fun House"
    FACTORY = "Factory"
    SECRET = "Secret Boss"
    EVENT = "Story Event"


@dataclasses.dataclass(frozen=True)
class _EnemyInfo:
    enemy_name: str
    dev_location: DevModeLocation
    tower_floor: int
    influence: int
    strength: int
    stamina: int
    intelligence: int
    endurance: int
    agility: int
    luck: int


class EnemyInformation(enum.Enum):
    MONOKUMAMEL = _EnemyInfo(enemy_name="Monokumamel", dev_location=DevModeLocation.FIRST_ISLAND, tower_floor=1, influence=50, strength=12, stamina=26, intelligence=28, endurance=13, agility=36, luck=48)
    MONOKUMAMEL_V = _EnemyInfo(enemy_name="Monokumamel V", dev_location=DevModeLocation.COTTAGE, tower_floor=51, influence=330, strength=120, stamina=180, intelligence=120, endurance=180, agility=116, luck=188)
    MONOKUMAMEL_V2 = _EnemyInfo(enemy_name="Monokumamel V2", dev_location=DevModeLocation.NO_LOCATION, tower_floor=101, influence=1200, strength=250, stamina=333, intelligence=150, endurance=333, agility=255, luck=200)
    MONOKUMAMEL_V3 = _EnemyInfo(enemy_name="Monokumamel V3", dev_location=DevModeLocation.NO_LOCATION, tower_floor=151, influence=2300, strength=200, stamina=666, intelligence=180, endurance=666, agility=333, luck=240)
    FLUFFY_MONOBUNNY = _EnemyInfo(enemy_name="Fluffy Monobunny", dev_location=DevModeLocation.NO_LOCATION, tower_floor=2, influence=80, strength=30, stamina=40, intelligence=70, endurance=90, agility=34, luck=22)
    FLUFFY_MONOBUNNY_V = _EnemyInfo(enemy_name="Fluffy Monobunny V", dev_location=DevModeLocation.NO_LOCATION, tower_floor=51, influence=550, strength=120, stamina=190, intelligence=158, endurance=190, agility=120, luck=85)
    FLUFFY_MONOBUNNY_V2 = _EnemyInfo(enemy_name="Fluffy Monobunny V2", dev_location=DevModeLocation.NO_LOCATION, tower_floor=96, influence=1000, strength=180, stamina=333, intelligence=240, endurance=333, agility=200, luck=155)
    FLUFFY_MONOBUNNY_V3 = _EnemyInfo(enemy_name="Fluffy Monobunny V3", dev_location=DevModeLocation.NO_LOCATION, tower_floor=151, influence=2000, strength=200, stamina=666, intelligence=255, endurance=666, agility=255, luck=255)
    MONOKUMA_GATHER = _EnemyInfo(enemy_name="Monokuma Gather", dev_location=DevModeLocation.SECOND_ISLAND, tower_floor=3, influence=60, strength=44, stamina=200, intelligence=0, endurance=10, agility=20, luck=44)
    MONOKUMA_GATHER_V = _EnemyInfo(enemy_name="Monokuma Gather V", dev_location=DevModeLocation.BEACH_HOUSE, tower_floor=52, influence=850, strength=100, stamina=400, intelligence=0, endurance=150, agility=50, luck=78)
    MONOKUMA_GATHER_V2 = _EnemyInfo(enemy_name="Monokuma Gather V2", dev_location=DevModeLocation.NO_LOCATION, tower_floor=103, influence=1200, strength=150, stamina=700, intelligence=200, endurance=255, agility=100, luck=96)
    MONOKUMA_GATHER_V3 = _EnemyInfo(enemy_name="Monokuma Gather V3", dev_location=DevModeLocation.NO_LOCATION, tower_floor=152, influence=2500, strength=200, stamina=900, intelligence=255, endurance=400, agility=120, luck=106)
    MONOKUMA_HERMIT = _EnemyInfo(enemy_name="Monokuma Hermit", dev_location=DevModeLocation.FOURTH_ISLAND, tower_floor=6, influence=250, strength=22, stamina=34, intelligence=150, endurance=100, agility=145, luck=46)
    MONOKUMA_HERMIT_V = _EnemyInfo(enemy_name="Monokuma Hermit V", dev_location=DevModeLocation.FUN_HOUSE, tower_floor=54, influence=770, strength=80, stamina=130, intelligence=255, endurance=220, agility=255, luck=52)
    MONOKUMA_HERMIT_V2 = _EnemyInfo(enemy_name="Monokuma Hermit V2", dev_location=DevModeLocation.NO_LOCATION, tower_floor=105, influence=1200, strength=90, stamina=666, intelligence=333, endurance=255, agility=300, luck=70)
    MONOKUMA_HERMIT_V3 = _EnemyInfo(enemy_name="Monokuma Hermit V3", dev_location=DevModeLocation.NO_LOCATION, tower_floor=154, influence=2500, strength=255, stamina=999, intelligence=748, endurance=480, agility=500, luck=160)
    CURSE_MONOGIRL = _EnemyInfo(enemy_name="Curse Monogirl", dev_location=DevModeLocation.NO_LOCATION, tower_floor=8, influence=120, strength=32, stamina=35, intelligence=180, endurance=90, agility=160, luck=80)
    CURSE_MONOGIRL_V = _EnemyInfo(enemy_name="Curse Monogirl V", dev_location=DevModeLocation.NO_LOCATION, tower_floor=55, influence=800, strength=80, stamina=92, intelligence=200, endurance=170, agility=230, luck=255)
    CURSE_MONOGIRL_V2 = _EnemyInfo(enemy_name="Curse Monogirl V2", dev_location=DevModeLocation.NO_LOCATION, tower_floor=108, influence=1680, strength=155, stamina=255, intelligence=333, endurance=255, agility=999, luck=666)
    CURSE_MONOGIRL_V3 = _EnemyInfo(enemy_name="Curse Monogirl V3", dev_location=DevModeLocation.NO_LOCATION, tower_floor=155, influence=3200, strength=255, stamina=700, intelligence=748, endurance=666, agility=1500, luck=888)
    MONOKUMANTALA = _EnemyInfo(enemy_name="Monokumantala", dev_location=DevModeLocation.NO_LOCATION, tower_floor=4, influence=90, strength=60, stamina=80, intelligence=32, endurance=31, agility=145, luck=48)
    MONOKUMANTALA_V = _EnemyInfo(enemy_name="Monokumantala V", dev_location=DevModeLocation.NO_LOCATION, tower_floor=55, influence=120, strength=120, stamina=100, intelligence=110, endurance=80, agility=255, luck=122)
    MONOKUMANTALA_V2 = _EnemyInfo(enemy_name="Monokumantala V2", dev_location=DevModeLocation.NO_LOCATION, tower_floor=104, influence=300, strength=500, stamina=255, intelligence=190, endurance=255, agility=999, luck=150)
    MONOKUMANTALA_V3 = _EnemyInfo(enemy_name="Monokumantala V3", dev_location=DevModeLocation.NO_LOCATION, tower_floor=155, influence=1000, strength=1000, stamina=555, intelligence=255, endurance=555, agility=1500, luck=180)
    MONODRAGON_HEAD = _EnemyInfo(enemy_name="Monodragon Head", dev_location=DevModeLocation.SECOND_ISLAND, tower_floor=12, influence=580, strength=98, stamina=80, intelligence=70, endurance=92, agility=110, luck=200)
    MONODRAGON_HEAD_V = _EnemyInfo(enemy_name="Monodragon Head V", dev_location=DevModeLocation.BEACH_HOUSE, tower_floor=62, influence=1060, strength=255, stamina=255, intelligence=120, endurance=255, agility=255, luck=255)
    MONODRAGON_HEAD_V2 = _EnemyInfo(enemy_name="Monodragon Head V2", dev_location=DevModeLocation.NO_LOCATION, tower_floor=112, influence=1480, strength=444, stamina=650, intelligence=100, endurance=560, agility=444, luck=666)
    MONODRAGON_HEAD_V3 = _EnemyInfo(enemy_name="Monodragon Head V3", dev_location=DevModeLocation.NO_LOCATION, tower_floor=162, influence=2300, strength=666, stamina=1050, intelligence=190, endurance=1000, agility=666, luck=999)
    FLOOR_MONODRAGON = _EnemyInfo(enemy_name="Floor Monodragon", dev_location=DevModeLocation.FIFTH_ISLAND, tower_floor=22, influence=1000, strength=150, stamina=200, intelligence=50, endurance=150, agility=10, luck=54)
    FLOOR_MONODRAGON_V = _EnemyInfo(enemy_name="Floor Monodragon V", dev_location=DevModeLocation.FACTORY, tower_floor=66, influence=1500, strength=220, stamina=255, intelligence=70, endurance=255, agility=60, luck=75)
    FLOOR_MONODRAGON_V2 = _EnemyInfo(enemy_name="Floor Monodragon V2", dev_location=DevModeLocation.NO_LOCATION, tower_floor=116, influence=2000, strength=333, stamina=570, intelligence=240, endurance=550, agility=100, luck=150)
    FLOOR_MONODRAGON_V3 = _EnemyInfo(enemy_name="Floor Monodragon V3", dev_location=DevModeLocation.NO_LOCATION, tower_floor=165, influence=2800, strength=666, stamina=1000, intelligence=255, endurance=1000, agility=255, luck=210)
    TWISTY_MONOKUMA = _EnemyInfo(enemy_name="Twisty Monokuma", dev_location=DevModeLocation.NO_LOCATION, tower_floor=19, influence=420, strength=66, stamina=98, intelligence=55, endurance=98, agility=120, luck=100)
    TWISTY_MONOKUMA_V = _EnemyInfo(enemy_name="Twisty Monokuma V", dev_location=DevModeLocation.NO_LOCATION, tower_floor=64, influence=900, strength=87, stamina=255, intelligence=150, endurance=255, agility=366, luck=100)
    TWISTY_MONOKUMA_V2 = _EnemyInfo(enemy_name="Twisty Monokuma V2", dev_location=DevModeLocation.NO_LOCATION, tower_floor=119, influence=1800, strength=255, stamina=580, intelligence=255, endurance=488, agility=666, luck=140)
    TWISTY_MONOKUMA_V3 = _EnemyInfo(enemy_name="Twisty Monokuma V3", dev_location=DevModeLocation.NO_LOCATION, tower_floor=164, influence=2700, strength=360, stamina=1200, intelligence=360, endurance=666, agility=888, luck=330)
    MONOKUMAMEL_B = _EnemyInfo(enemy_name="Monokumamel B", dev_location=DevModeLocation.NO_LOCATION, tower_floor=14, influence=8, strength=92, stamina=500, intelligence=500, endurance=500, agility=50, luck=300)
    MONOKUMAMEL_S = _EnemyInfo(enemy_name="Monokumamel S", dev_location=DevModeLocation.NO_LOCATION, tower_floor=29, influence=16, strength=145, stamina=800, intelligence=800, endurance=800, agility=100, luck=600)
    MONOKUMAMEL_G = _EnemyInfo(enemy_name="Monokumamel G", dev_location=DevModeLocation.NO_LOCATION, tower_floor=92, influence=24, strength=166, stamina=900, intelligence=900, endurance=900, agility=150, luck=900)
    MONOKUMAMEL_P = _EnemyInfo(enemy_name="Monokumamel P", dev_location=DevModeLocation.NO_LOCATION, tower_floor=115, influence=50, strength=187, stamina=1200, intelligence=1200, endurance=1200, agility=200, luck=900)
    EXISAL_BLUE = _EnemyInfo(enemy_name="Exisal Blue", dev_location=DevModeLocation.NO_LOCATION, tower_floor=15, influence=1500, strength=350, stamina=100, intelligence=102, endurance=0, agility=150, luck=120)
    EXISAL_YELLOW = _EnemyInfo(enemy_name="Exisal Yellow", dev_location=DevModeLocation.NO_LOCATION, tower_floor=55, influence=2700, strength=500, stamina=500, intelligence=180, endurance=50, agility=180, luck=120)
    EXISAL_GREEN = _EnemyInfo(enemy_name="Exisal Green", dev_location=DevModeLocation.NO_LOCATION, tower_floor=105, influence=3333, strength=800, stamina=150, intelligence=600, endurance=60, agility=90, luck=150)
    EXISAL_PINK = _EnemyInfo(enemy_name="Exisal Pink", dev_location=DevModeLocation.NO_LOCATION, tower_floor=131, influence=999999, strength=160, stamina=255, intelligence=255, endurance=255, agility=60, luck=80)
    EXISAL_V3 = _EnemyInfo(enemy_name="Exisal V3", dev_location=DevModeLocation.NO_LOCATION, tower_floor=191, influence=35000, strength=500, stamina=1200, intelligence=99999, endurance=333, agility=500, luck=333)
    MONOKUMASECT = _EnemyInfo(enemy_name="Monokumasect", dev_location=DevModeLocation.COTTAGE, tower_floor=10, influence=1500, strength=100, stamina=85, intelligence=100, endurance=85, agility=80, luck=70)
    MONOKUMASECT_V3 = _EnemyInfo(enemy_name="Monokumasect V3", dev_location=DevModeLocation.NO_LOCATION, tower_floor=110, influence=20000, strength=500, stamina=650, intelligence=500, endurance=650, agility=330, luck=240)
    MONOKUMA_TANK = _EnemyInfo(enemy_name="Monokuma Tank", dev_location=DevModeLocation.BEACH_HOUSE, tower_floor=30, influence=1800, strength=150, stamina=240, intelligence=220, endurance=250, agility=70, luck=90)
    MONOKUMA_TANK_V3 = _EnemyInfo(enemy_name="Monokuma Tank V3", dev_location=DevModeLocation.NO_LOCATION, tower_floor=130, influence=18000, strength=800, stamina=800, intelligence=800, endurance=800, agility=200, luck=200)
    MONOKUMA_BOSS = _EnemyInfo(enemy_name="Monokuma Boss", dev_location=DevModeLocation.HOSPITAL, tower_floor=50, influence=2000, strength=600, stamina=230, intelligence=200, endurance=230, agility=70, luck=190)
    MONOKUMA_BOSS_V3 = _EnemyInfo(enemy_name="Monokuma Boss V3", dev_location=DevModeLocation.NO_LOCATION, tower_floor=150, influence=18000, strength=999, stamina=666, intelligence=255, endurance=666, agility=255, luck=200)
    MONDUBA = _EnemyInfo(enemy_name="Mon'Duba", dev_location=DevModeLocation.FUN_HOUSE, tower_floor=70, influence=3000, strength=333, stamina=222, intelligence=666, endurance=666, agility=120, luck=300)
    MONDUBA_V3 = _EnemyInfo(enemy_name="Mon'Duba V3", dev_location=DevModeLocation.NO_LOCATION, tower_floor=170, influence=30000, strength=600, stamina=1300, intelligence=1500, endurance=1300, agility=450, luck=300)
    MONOKOPPA = _EnemyInfo(enemy_name="Monokoppa", dev_location=DevModeLocation.FACTORY, tower_floor=90, influence=7500, strength=333, stamina=300, intelligence=333, endurance=600, agility=777, luck=255)
    MONOKOPPA_V3 = _EnemyInfo(enemy_name="Monokoppa", dev_location=DevModeLocation.NO_LOCATION, tower_floor=190, influence=35000, strength=999, stamina=888, intelligence=999, endurance=1500, agility=1700, luck=500)
    EXISAL_RED = _EnemyInfo(enemy_name="Exisal Red", dev_location=DevModeLocation.NO_LOCATION, tower_floor=161, influence=15000, strength=800, stamina=500, intelligence=888, endurance=80, agility=666, luck=666)
    VANGUARD_MONOKUMA = _EnemyInfo(enemy_name="Vanguard Monokuma", dev_location=DevModeLocation.FIFTH_ISLAND, tower_floor=24, influence=850, strength=42, stamina=999, intelligence=10, endurance=0, agility=106, luck=72)
    VANGUARD_MONOKUMA_2 = _EnemyInfo(enemy_name="Vanguard Monokuma 2", dev_location=DevModeLocation.FACTORY, tower_floor=74, influence=1000, strength=160, stamina=999, intelligence=20, endurance=160, agility=255, luck=148)
    VANGUARD_MONOKUMA_ZZ = _EnemyInfo(enemy_name="Vanguard Monokuma ZZ", dev_location=DevModeLocation.NO_LOCATION, tower_floor=124, influence=1850, strength=255, stamina=9999, intelligence=30, endurance=333, agility=333, luck=160)
    VANGUARD_MONOKUMA_V3 = _EnemyInfo(enemy_name="Vanguard Monokuma V3", dev_location=DevModeLocation.NO_LOCATION, tower_floor=174, influence=2800, strength=333, stamina=9999, intelligence=40, endurance=666, agility=666, luck=184)
    MONOSLUDGE = _EnemyInfo(enemy_name="Monosludge", dev_location=DevModeLocation.FIRST_ISLAND, tower_floor=25, influence=850, strength=45, stamina=64, intelligence=200, endurance=90, agility=180, luck=100)
    MONOSLUDGE_2 = _EnemyInfo(enemy_name="Monosludge 2", dev_location=DevModeLocation.COTTAGE, tower_floor=76, influence=1000, strength=89, stamina=255, intelligence=255, endurance=255, agility=255, luck=133)
    MONOSLUDGE_ZZ = _EnemyInfo(enemy_name="Monosludge ZZ", dev_location=DevModeLocation.NO_LOCATION, tower_floor=127, influence=1850, strength=360, stamina=666, intelligence=380, endurance=666, agility=388, luck=255)
    MONOSLUDGE_V3 = _EnemyInfo(enemy_name="Monosludge V3", dev_location=DevModeLocation.NO_LOCATION, tower_floor=176, influence=2800, strength=500, stamina=1500, intelligence=700, endurance=1500, agility=666, luck=699)
    MONOHELPER = _EnemyInfo(enemy_name="Monohelper", dev_location=DevModeLocation.THIRD_ISLAND, tower_floor=32, influence=164, strength=80, stamina=30, intelligence=42, endurance=64, agility=255, luck=64)
    MONOHELPER_2 = _EnemyInfo(enemy_name="Monohelper 2", dev_location=DevModeLocation.HOSPITAL, tower_floor=82, influence=1300, strength=125, stamina=255, intelligence=180, endurance=255, agility=505, luck=150)
    MONOHELPER_ZZ = _EnemyInfo(enemy_name="Monohelper ZZ", dev_location=DevModeLocation.NO_LOCATION, tower_floor=132, influence=1800, strength=255, stamina=366, intelligence=180, endurance=366, agility=800, luck=255)
    MONOHELPER_V3 = _EnemyInfo(enemy_name="Monohelper V3", dev_location=DevModeLocation.NO_LOCATION, tower_floor=182, influence=2100, strength=355, stamina=666, intelligence=200, endurance=777, agility=1200, luck=366)
    GANGSTAKUMA = _EnemyInfo(enemy_name="Gangstakuma", dev_location=DevModeLocation.SECOND_ISLAND, tower_floor=33, influence=980, strength=500, stamina=120, intelligence=86, endurance=120, agility=150, luck=80)
    GANGSTAKUMA_2 = _EnemyInfo(enemy_name="Gangstakuma 2", dev_location=DevModeLocation.BEACH_HOUSE, tower_floor=83, influence=1800, strength=800, stamina=355, intelligence=150, endurance=355, agility=366, luck=106)
    GANGSTAKUMA_ZZ = _EnemyInfo(enemy_name="Gangstakuma ZZ", dev_location=DevModeLocation.NO_LOCATION, tower_floor=133, influence=3500, strength=1200, stamina=500, intelligence=180, endurance=500, agility=666, luck=255)
    GANGSTAKUMA_V3 = _EnemyInfo(enemy_name="Gangstakuma V3", dev_location=DevModeLocation.NO_LOCATION, tower_floor=183, influence=6000, strength=1800, stamina=788, intelligence=255, endurance=788, agility=888, luck=300)
    AETHERKUMA = _EnemyInfo(enemy_name="Aetherkuma", dev_location=DevModeLocation.THIRD_ISLAND, tower_floor=36, influence=380, strength=86, stamina=64, intelligence=130, endurance=333, agility=100, luck=120)
    AETHERKUMA_2 = _EnemyInfo(enemy_name="Aetherkuma 2", dev_location=DevModeLocation.HOSPITAL, tower_floor=85, influence=850, strength=150, stamina=255, intelligence=180, endurance=444, agility=366, luck=140)
    AETHERKUMA_ZZ = _EnemyInfo(enemy_name="Aetherkuma ZZ", dev_location=DevModeLocation.NO_LOCATION, tower_floor=136, influence=1250, strength=255, stamina=366, intelligence=255, endurance=555, agility=555, luck=160)
    AETHERKUMA_V3 = _EnemyInfo(enemy_name="Aetherkuma V3", dev_location=DevModeLocation.NO_LOCATION, tower_floor=186, influence=3500, strength=300, stamina=488, intelligence=666, endurance=666, agility=1000, luck=180)
    BONYKUMA = _EnemyInfo(enemy_name="Bonykuma", dev_location=DevModeLocation.FIRST_ISLAND, tower_floor=43, influence=360, strength=104, stamina=80, intelligence=255, endurance=255, agility=80, luck=46)
    BONYKUMA_2 = _EnemyInfo(enemy_name="Bonykuma 2", dev_location=DevModeLocation.COTTAGE, tower_floor=91, influence=1800, strength=160, stamina=200, intelligence=333, endurance=488, agility=165, luck=102)
    BONYKUMA_ZZ = _EnemyInfo(enemy_name="Bonykuma ZZ", dev_location=DevModeLocation.NO_LOCATION, tower_floor=143, influence=2500, strength=200, stamina=355, intelligence=444, endurance=888, agility=180, luck=150)
    BONYKUMA_V3 = _EnemyInfo(enemy_name="Bonykuma V3", dev_location=DevModeLocation.NO_LOCATION, tower_floor=175, influence=3000, strength=255, stamina=555, intelligence=555, endurance=1000, agility=255, luck=180)
    MONOKUMA_SAMURAI = _EnemyInfo(enemy_name="Monokuma Samurai", dev_location=DevModeLocation.THIRD_ISLAND, tower_floor=42, influence=800, strength=94, stamina=70, intelligence=100, endurance=70, agility=70, luck=46)
    MONOKUMA_SAMURAI_2 = _EnemyInfo(enemy_name="Monokuma Samurai 2", dev_location=DevModeLocation.HOSPITAL, tower_floor=94, influence=1500, strength=188, stamina=255, intelligence=200, endurance=255, agility=114, luck=102)
    MONOKUMA_SAMURAI_ZZ = _EnemyInfo(enemy_name="Monokuma Samurai ZZ", dev_location=DevModeLocation.NO_LOCATION, tower_floor=142, influence=3500, strength=255, stamina=999, intelligence=300, endurance=999, agility=360, luck=255)
    MONOKUMA_SAMURAI_V3 = _EnemyInfo(enemy_name="Monokuma Samurai V3", dev_location=DevModeLocation.NO_LOCATION, tower_floor=194, influence=5500, strength=466, stamina=1200, intelligence=900, endurance=1200, agility=480, luck=255)
    MONOBEL = _EnemyInfo(enemy_name="Monobel", dev_location=DevModeLocation.FOURTH_ISLAND, tower_floor=45, influence=312, strength=70, stamina=70, intelligence=70, endurance=113, agility=150, luck=94)
    MONOBEL_2 = _EnemyInfo(enemy_name="Monobel 2", dev_location=DevModeLocation.FUN_HOUSE, tower_floor=94, influence=1200, strength=140, stamina=255, intelligence=136, endurance=255, agility=255, luck=152)
    MONOBEL_ZZ = _EnemyInfo(enemy_name="Monobel ZZ", dev_location=DevModeLocation.NO_LOCATION, tower_floor=145, influence=2500, strength=333, stamina=999, intelligence=200, endurance=999, agility=366, luck=255)
    MONOBEL_V3 = _EnemyInfo(enemy_name="Monobel V3", dev_location=DevModeLocation.NO_LOCATION, tower_floor=194, influence=5300, strength=666, stamina=1500, intelligence=255, endurance=1500, agility=477, luck=255)
    ABYSSAL_MONOKUMA = _EnemyInfo(enemy_name="Abyssal Monokuma", dev_location=DevModeLocation.FOURTH_ISLAND, tower_floor=46, influence=450, strength=140, stamina=120, intelligence=100, endurance=70, agility=100, luck=70)
    ABYSSAL_MONOKUMA_2 = _EnemyInfo(enemy_name="Abyssal Monokuma 2", dev_location=DevModeLocation.FUN_HOUSE, tower_floor=91, influence=980, strength=228, stamina=255, intelligence=200, endurance=255, agility=255, luck=114)
    ABYSSAL_MONOKUMA_ZZ = _EnemyInfo(enemy_name="Abyssal Monokuma ZZ", dev_location=DevModeLocation.NO_LOCATION, tower_floor=143, influence=1800, strength=333, stamina=888, intelligence=444, endurance=1000, agility=775, luck=130)
    ABYSSAL_MONOKUMA_V3 = _EnemyInfo(enemy_name="Abyssal Monokuma V3", dev_location=DevModeLocation.NO_LOCATION, tower_floor=193, influence=5900, strength=666, stamina=1500, intelligence=1500, endurance=1500, agility=888, luck=154)
    VOLATILE_MONOURCHIN = _EnemyInfo(enemy_name="Volatile Monourchin", dev_location=DevModeLocation.FIFTH_ISLAND, tower_floor=48, influence=800, strength=90, stamina=150, intelligence=90, endurance=200, agility=100, luck=94)
    VOLATILE_MONOURCHIN_2 = _EnemyInfo(enemy_name="Volatile Monourchin 2", dev_location=DevModeLocation.FACTORY, tower_floor=-1, influence=1000, strength=180, stamina=255, intelligence=180, endurance=400, agility=160, luck=152)
    VOLATILE_MONOURCHIN_ZZ = _EnemyInfo(enemy_name="Volatile Monourchin ZZ", dev_location=DevModeLocation.NO_LOCATION, tower_floor=148, influence=1600, strength=333, stamina=600, intelligence=333, endurance=600, agility=500, luck=170)
    VOLATILE_MONOURCHIN_V3 = _EnemyInfo(enemy_name="Volatile Monourchin ZZ", dev_location=DevModeLocation.NO_LOCATION, tower_floor=193, influence=2700, strength=777, stamina=1550, intelligence=777, endurance=1550, agility=800, luck=182)
    MONOBEAST_TIGER = _EnemyInfo(enemy_name="Monobeast (Tiger)", dev_location=DevModeLocation.CENTRAL_ISLAND, tower_floor=20, influence=1800, strength=90, stamina=100, intelligence=90, endurance=180, agility=150, luck=80)
    MONOBEAST_TIGER_AWAKENED = _EnemyInfo(enemy_name="Monobeast (Tiger Awakened)", dev_location=DevModeLocation.NO_LOCATION, tower_floor=120, influence=13000, strength=500, stamina=350, intelligence=350, endurance=255, agility=450, luck=255)
    MONOBEAST_BIRD = _EnemyInfo(enemy_name="Monobeast (Bird)", dev_location=DevModeLocation.CENTRAL_ISLAND, tower_floor=60, influence=2300, strength=200, stamina=200, intelligence=200, endurance=255, agility=220, luck=200)
    MONOBEAST_BIRD_AWAKENED = _EnemyInfo(enemy_name="Monobeast (Bird Awakened)", dev_location=DevModeLocation.NO_LOCATION, tower_floor=160, influence=20000, strength=800, stamina=777, intelligence=777, endurance=777, agility=900, luck=355)
    MONOBEAST_SNAKE = _EnemyInfo(enemy_name="Monobeast (Snake)", dev_location=DevModeLocation.CENTRAL_ISLAND, tower_floor=40, influence=2000, strength=130, stamina=190, intelligence=130, endurance=200, agility=180, luck=240)
    MONOBEAST_SNAKE_AWAKENED = _EnemyInfo(enemy_name="Monobeast (Snake Awakened)", dev_location=DevModeLocation.NO_LOCATION, tower_floor=140, influence=15000, strength=500, stamina=999, intelligence=999, endurance=999, agility=500, luck=255)
    MONOBEAST_HORSE = _EnemyInfo(enemy_name="Monobeast (Horse)", dev_location=DevModeLocation.CENTRAL_ISLAND, tower_floor=80, influence=4000, strength=255, stamina=400, intelligence=250, endurance=400, agility=200, luck=155)
    MONOBEAST_HORSE_AWAKENED = _EnemyInfo(enemy_name="Monobeast (Horse Awakened)", dev_location=DevModeLocation.NO_LOCATION, tower_floor=180, influence=33000, strength=888, stamina=999, intelligence=800, endurance=999, agility=788, luck=888)
    MONOBEAST_HUMAN = _EnemyInfo(enemy_name="Monobeast (Human)", dev_location=DevModeLocation.CENTRAL_ISLAND, tower_floor=100, influence=8000, strength=300, stamina=555, intelligence=666, endurance=655, agility=333, luck=333)
    MONOBEAST_HUMAN_AWAKENED = _EnemyInfo(enemy_name="Monobeast (Human Awakened)", dev_location=DevModeLocation.NO_LOCATION, tower_floor=200, influence=40000, strength=833, stamina=3500, intelligence=833, endurance=3500, agility=700, luck=666)
    ALMIGHTY_JABBERWOCK = _EnemyInfo(enemy_name="Almighty Jabberwock", dev_location=DevModeLocation.SECRET, tower_floor=200, influence=50000, strength=2300, stamina=5200, intelligence=9999, endurance=5200, agility=955, luck=666)
    ALMIGHTY_JABBERWOCK_AWAKENED = _EnemyInfo(enemy_name="Almighty Jabberwock Awakened", dev_location=DevModeLocation.NO_LOCATION, tower_floor=201, influence=500000000, strength=720, stamina=780, intelligence=9999, endurance=780, agility=1300, luck=1500)
    MONOKID = _EnemyInfo(enemy_name="Monokid", dev_location=DevModeLocation.EVENT, tower_floor=-1, influence=2500, strength=70, stamina=60, intelligence=50, endurance=60, agility=150, luck=80)
    MONOSUKE = _EnemyInfo(enemy_name="Monosuke", dev_location=DevModeLocation.EVENT, tower_floor=-1, influence=4000, strength=90, stamina=150, intelligence=90, endurance=180, agility=120, luck=190)
    MONODAM = _EnemyInfo(enemy_name="Monodam", dev_location=DevModeLocation.EVENT, tower_floor=-1, influence=6000, strength=120, stamina=180, intelligence=120, endurance=200, agility=200, luck=180)
    MONOTARO = _EnemyInfo(enemy_name="Monotaro", dev_location=DevModeLocation.EVENT, tower_floor=-1, influence=15000, strength=150, stamina=255, intelligence=150, endurance=255, agility=222, luck=190)
    HERO_ROBOT = _EnemyInfo(enemy_name="Hero Robot", dev_location=DevModeLocation.EVENT, tower_floor=-1, influence=7000, strength=130, stamina=120, intelligence=75, endurance=95, agility=150, luck=70)
    PRIEST_ROBOT = _EnemyInfo(enemy_name="Priest Robot", dev_location=DevModeLocation.EVENT, tower_floor=-1, influence=7000, strength=140, stamina=95, intelligence=120, endurance=120, agility=150, luck=85)
    WARRIOR_ROBOT = _EnemyInfo(enemy_name="Warrior Robot", dev_location=DevModeLocation.EVENT, tower_floor=-1, influence=9000, strength=150, stamina=105, intelligence=105, endurance=105, agility=200, luck=110)
    SAGE_ROBOT = _EnemyInfo(enemy_name="Sage Robot", dev_location=DevModeLocation.EVENT, tower_floor=-1, influence=9000, strength=170, stamina=150, intelligence=200, endurance=150, agility=200, luck=110)
    MAGE_ROBOT = _EnemyInfo(enemy_name="Mage Robot", dev_location=DevModeLocation.EVENT, tower_floor=-1, influence=10000, strength=190, stamina=255, intelligence=190, endurance=255, agility=255, luck=200)
    MONOKUMA = _EnemyInfo(enemy_name="Monokuma", dev_location=DevModeLocation.EVENT, tower_floor=-1, influence=20000, strength=210, stamina=280, intelligence=210, endurance=280, agility=255, luck=255)


    def __new__(cls, info: _EnemyInfo) -> Self:
        obj = object.__new__(cls)
        obj._value_ = info
        return obj

    def __init__(self, info: _EnemyInfo) -> None:
        self.enemy_name: str = info.enemy_name
        self.dev_location: DevModeLocation = info.dev_location
        self.tower_floor: int = info.tower_floor
        self.influence: int = info.influence
        self.strength: int = info.strength
        self.stamina: int = info.stamina
        self.intelligence: int = info.intelligence
        self.endurance: int = info.endurance
        self.agility: int = info.agility
        self.luck: int = info.luck


class CharacterEventType(enum.StrEnum):
    """Types of dev mode events based on the character that you currently are"""
    FRIEND = "Friend Event"
    """Events between multiple chars. Junko, Izuru, and Usami events require them specifically"""
    MY_FUTURE = "My Future Event"
    """U Rare and hit all events for char in 1 dev mode"""
    SWIMSUIT = "Swimsuit Event"
    """Event requiring S or U Rare for char"""
    POTENTIAL_TALENT = "Potential Talent Event"
    """1st regular event in dev mode (based on turns)"""
    SUMMER_FESTIVAL = "Summer Festival Event"
    """2nd regular event in dev mode (based on turns)"""
    CAMPFIRE = "Campfire Event"
    """3rd regular event in dev mode (based on turns)"""


@dataclasses.dataclass(frozen=True)
class _CharacterEventData:
    event_name: str
    event_type: CharacterEventType
    char_list: list[Character]


class CharacterEvent(enum.Enum):
    JUNKO_AND_MAKOTO = _CharacterEventData(event_name="Junko & Makoto", event_type=CharacterEventType.FRIEND, char_list=[Character.JUNKO_ENOSHIMA, Character.MAKOTO_NAEGI])
    AKANE_AND_CHIAKI_AND_PEKO = _CharacterEventData(event_name="Akane & Chiaki & Peko", event_type=CharacterEventType.FRIEND, char_list=[Character.AKANE_OWARI, Character.CHIAKI_NANAMI, Character.PEKO_PEKOYAMA])
    AKANE_AND_JATARO = _CharacterEventData(event_name="Akane & Jataro", event_type=CharacterEventType.FRIEND, char_list=[Character.AKANE_OWARI, Character.JATARO_KEMURI])
    AKANE_AND_SHIROKUMA = _CharacterEventData(event_name="Akane & Shirokuma", event_type=CharacterEventType.FRIEND, char_list=[Character.AKANE_OWARI, Character.SHIROKUMA])
    AKANE_AND_SONIA = _CharacterEventData(event_name="Akane & Sonia", event_type=CharacterEventType.FRIEND, char_list=[Character.AKANE_OWARI, Character.SONIA_NEVERMIND])
    ANGIE_AND_CELESTIA = _CharacterEventData(event_name="Angie & Celestia", event_type=CharacterEventType.FRIEND, char_list=[Character.ANGIE_YONAGA, Character.CELESTIA_LUDENBERG])
    ANGIE_AND_HIFUMI_AND_GUNDHAM = _CharacterEventData(event_name="Angie & Hifumi & Gundham", event_type=CharacterEventType.FRIEND, char_list=[Character.ANGIE_YONAGA, Character.HIFUMI_YAMADA, Character.GUNDHAM_TANAKA])
    ANGIE_AND_KAEDE = _CharacterEventData(event_name="Angie & Kaede", event_type=CharacterEventType.FRIEND, char_list=[Character.ANGIE_YONAGA, Character.KAEDE_AKAMATSU])
    ANGIE_AND_LEON = _CharacterEventData(event_name="Angie & Leon", event_type=CharacterEventType.FRIEND, char_list=[Character.ANGIE_YONAGA, Character.LEON_KUWATA])
    ANGIE_AND_MONOKUMA = _CharacterEventData(event_name="Angie & Monokuma", event_type=CharacterEventType.FRIEND, char_list=[Character.ANGIE_YONAGA, Character.MONOKUMA])
    ANGIE_AND_MONOMI_AND_JATARO = _CharacterEventData(event_name="Angie & Monomi & Jataro", event_type=CharacterEventType.FRIEND, char_list=[Character.ANGIE_YONAGA, Character.MONOMI, Character.JATARO_KEMURI])
    ANGIE_AND_NAGITO = _CharacterEventData(event_name="Angie & Nagito", event_type=CharacterEventType.FRIEND, char_list=[Character.ANGIE_YONAGA, Character.NAGITO_KOMAEDA])
    ANGIE_AND_SONIA = _CharacterEventData(event_name="Angie & Sonia", event_type=CharacterEventType.FRIEND, char_list=[Character.ANGIE_YONAGA, Character.SONIA_NEVERMIND])
    AOI_AND_AKANE = _CharacterEventData(event_name="Aoi & Akane", event_type=CharacterEventType.FRIEND, char_list=[Character.AOI_ASAHINA, Character.AKANE_OWARI])
    AOI_AND_CHIAKI = _CharacterEventData(event_name="Aoi & Chiaki", event_type=CharacterEventType.FRIEND, char_list=[Character.AOI_ASAHINA, Character.CHIAKI_NANAMI])
    AOI_AND_MUKURO = _CharacterEventData(event_name="Aoi & Mukuro", event_type=CharacterEventType.FRIEND, char_list=[Character.AOI_ASAHINA, Character.MUKURO_IKUSABA])
    AOI_AND_NAGISA = _CharacterEventData(event_name="Aoi & Nagisa", event_type=CharacterEventType.FRIEND, char_list=[Character.AOI_ASAHINA, Character.NAGISA_SHINGETSU])
    BYAKUYA_AND_HAJIME = _CharacterEventData(event_name="Byakuya & Hajime", event_type=CharacterEventType.FRIEND, char_list=[Character.BYAKUYA_TOGAMI, Character.HAJIME_HINATA])
    BYAKUYA_AND_HIROKO = _CharacterEventData(event_name="Byakuya & Hiroko", event_type=CharacterEventType.FRIEND, char_list=[Character.BYAKUYA_TOGAMI, Character.HIROKO_HAGAKURE])
    BYAKUYA_AND_MUKURO = _CharacterEventData(event_name="Byakuya & Mukuro", event_type=CharacterEventType.FRIEND, char_list=[Character.BYAKUYA_TOGAMI, Character.MUKURO_IKUSABA])
    BYAKUYA_AND_KYOKO = _CharacterEventData(event_name="Byakuya & Kyoko", event_type=CharacterEventType.FRIEND, char_list=[Character.BYAKUYA_TOGAMI, Character.KYOKO_KIRIGIRI])
    BYAKUYA_AND_SONIA = _CharacterEventData(event_name="Byakuya & Sonia", event_type=CharacterEventType.FRIEND, char_list=[Character.BYAKUYA_TOGAMI, Character.SONIA_NEVERMIND])
    BYAKUYA_AND_TOKO_AND_PEKO = _CharacterEventData(event_name="Byakuya & Toko & Peko", event_type=CharacterEventType.FRIEND, char_list=[Character.BYAKUYA_TOGAMI, Character.TOKO_FUKAWA, Character.PEKO_PEKOYAMA])
    IMPOSTER_AND_TERUTERU = _CharacterEventData(event_name="The Ultimate Imposter & Teruteru", event_type=CharacterEventType.FRIEND, char_list=[Character.THE_ULTIMATE_IMPOSTER, Character.TERUTERU_HANAMURA])
    CELESTIA_AND_CHIAKI = _CharacterEventData(event_name="Celestia & Chiaki", event_type=CharacterEventType.FRIEND, char_list=[Character.CELESTIA_LUDENBERG, Character.CHIAKI_NANAMI])
    CELESTIA_AND_FUYUHIKO = _CharacterEventData(event_name="Celestia & Fuyuhiko", event_type=CharacterEventType.FRIEND, char_list=[Character.CELESTIA_LUDENBERG, Character.FUYUHIKO_KUZURYU])
    CELESTIA_AND_KOMARU_AND_MONACA = _CharacterEventData(event_name="Celestia & Komaru & Monaca", event_type=CharacterEventType.FRIEND, char_list=[Character.CELESTIA_LUDENBERG, Character.KOMARU_NAEGI, Character.MONACA_TOWA])
    CELESTIA_AND_MASARU = _CharacterEventData(event_name="Celestia & Masaru", event_type=CharacterEventType.FRIEND, char_list=[Character.CELESTIA_LUDENBERG, Character.MASARU_DAIMON])
    CELESTIA_AND_SONIA = _CharacterEventData(event_name="Celestia & Sonia", event_type=CharacterEventType.FRIEND, char_list=[Character.CELESTIA_LUDENBERG, Character.SONIA_NEVERMIND])
    CHIAKI_AND_IBUKI = _CharacterEventData(event_name="Chiaki & Ibuki", event_type=CharacterEventType.FRIEND, char_list=[Character.CHIAKI_NANAMI, Character.IBUKI_MIODA])
    CHIHIRO_AND_FUYUHIKO = _CharacterEventData(event_name="Chihiro & Fuyuhiko", event_type=CharacterEventType.FRIEND, char_list=[Character.CHIHIRO_FUJISAKI, Character.FUYUHIKO_KUZURYU])
    CHIHIRO_AND_JATARO = _CharacterEventData(event_name="Chihiro & Jataro", event_type=CharacterEventType.FRIEND, char_list=[Character.CHIHIRO_FUJISAKI, Character.JATARO_KEMURI])
    CHIHIRO_AND_NEKOMARU = _CharacterEventData(event_name="Chihiro & Nekomaru", event_type=CharacterEventType.FRIEND, char_list=[Character.CHIHIRO_FUJISAKI, Character.NEKOMARU_NIDAI])
    CHIHIRO_AND_SAKURA = _CharacterEventData(event_name="Chihiro & Sakura", event_type=CharacterEventType.FRIEND, char_list=[Character.CHIHIRO_FUJISAKI, Character.SAKURA_OGAMI])
    CHIHIRO_AND_SONIA_AND_SHIROKUMA = _CharacterEventData(event_name="Chihiro & Sonia & Shirokuma", event_type=CharacterEventType.FRIEND, char_list=[Character.CHIHIRO_FUJISAKI, Character.SONIA_NEVERMIND, Character.SHIROKUMA])
    FUYUHIKO_AND_KOTOKO = _CharacterEventData(event_name="Fuyuhiko & Kotoko", event_type=CharacterEventType.FRIEND, char_list=[Character.FUYUHIKO_KUZURYU, Character.KOTOKO_UTSUGI])
    FUYUHIKO_AND_MIKAN_AND_IBUKI = _CharacterEventData(event_name="Fuyuhiko & Mikan & Ibuki", event_type=CharacterEventType.FRIEND, char_list=[Character.FUYUHIKO_KUZURYU, Character.MIKAN_TSUMIKI, Character.IBUKI_MIODA])
    FUYUHIKO_AND_PEKO = _CharacterEventData(event_name="Fuyuhiko & Peko", event_type=CharacterEventType.FRIEND, char_list=[Character.FUYUHIKO_KUZURYU, Character.PEKO_PEKOYAMA])
    JACK_AND_IMPOSTER = _CharacterEventData(event_name="Genocide Jack & The Ultimate Imposter", event_type=CharacterEventType.FRIEND, char_list=[Character.GENOCIDE_JACK, Character.THE_ULTIMATE_IMPOSTER])
    JACK_AND_CELESTIA_AND_KOTOKO = _CharacterEventData(event_name="Genocide Jack & Celestia & Kotoko", event_type=CharacterEventType.FRIEND, char_list=[Character.GENOCIDE_JACK, Character.CELESTIA_LUDENBERG, Character.KOTOKO_UTSUGI])
    JACK_AND_HIYOKO = _CharacterEventData(event_name="Genocide Jack & Hiyoko", event_type=CharacterEventType.FRIEND, char_list=[Character.GENOCIDE_JACK, Character.HIYOKO_SAIONJI])
    JACK_AND_KOMARU = _CharacterEventData(event_name="Genocide Jack & Komaru", event_type=CharacterEventType.FRIEND, char_list=[Character.GENOCIDE_JACK, Character.KOMARU_NAEGI])
    JACK_AND_SONIA = _CharacterEventData(event_name="Genocide Jack & Sonia", event_type=CharacterEventType.FRIEND, char_list=[Character.GENOCIDE_JACK, Character.SONIA_NEVERMIND])
    JACK_AND_TERUTERU_AND_MONOMI = _CharacterEventData(event_name="Genocide Jack & Teruteru & Monomi", event_type=CharacterEventType.FRIEND, char_list=[Character.GENOCIDE_JACK, Character.TERUTERU_HANAMURA, Character.MONOMI])
    GONTA_AND_AOI_AND_GUNDHAM = _CharacterEventData(event_name="Gonta & Aoi & Gundham", event_type=CharacterEventType.FRIEND, char_list=[Character.GONTA_GOKUHARA, Character.AOI_ASAHINA, Character.GUNDHAM_TANAKA])
    GONTA_AND_HAJIME = _CharacterEventData(event_name="Gonta & Hajime", event_type=CharacterEventType.FRIEND, char_list=[Character.GONTA_GOKUHARA, Character.HAJIME_HINATA])
    GONTA_AND_MUKURO_AND_MONACA = _CharacterEventData(event_name="Gonta & Mukuro & Monaca", event_type=CharacterEventType.FRIEND, char_list=[Character.GONTA_GOKUHARA, Character.MUKURO_IKUSABA, Character.MONACA_TOWA])
    GONTA_AND_K1_B0_AND_KUROKUMA = _CharacterEventData(event_name="Gonta & K1-B0 & Kurokuma", event_type=CharacterEventType.FRIEND, char_list=[Character.GONTA_GOKUHARA, Character.K1_B0, Character.KUROKUMA])
    GONTA_AND_KIYOTAKA = _CharacterEventData(event_name="Gonta & Kiyotaka", event_type=CharacterEventType.FRIEND, char_list=[Character.GONTA_GOKUHARA, Character.KIYOTAKA_ISHIMARU])
    GONTA_AND_KOKICHI = _CharacterEventData(event_name="Gonta & Kokichi", event_type=CharacterEventType.FRIEND, char_list=[Character.GONTA_GOKUHARA, Character.KOKICHI_OMA])
    GONTA_AND_SHIROKUMA = _CharacterEventData(event_name="Gonta & Shirokuma", event_type=CharacterEventType.FRIEND, char_list=[Character.GONTA_GOKUHARA, Character.SHIROKUMA])
    GONTA_AND_SONIA = _CharacterEventData(event_name="Gonta & Sonia", event_type=CharacterEventType.FRIEND, char_list=[Character.GONTA_GOKUHARA, Character.SONIA_NEVERMIND])
    GONTA_AND_TOKO = _CharacterEventData(event_name="Gonta & Toko", event_type=CharacterEventType.FRIEND, char_list=[Character.GONTA_GOKUHARA, Character.TOKO_FUKAWA])
    GUNDHAM_AND_KAZUICHI_AND_SONIA = _CharacterEventData(event_name="Gundham & Kazuichi & Sonia", event_type=CharacterEventType.FRIEND, char_list=[Character.GUNDHAM_TANAKA, Character.KAZUICHI_SODA, Character.SONIA_NEVERMIND])
    GUNDHAM_AND_PEKO = _CharacterEventData(event_name="Gundham & Peko", event_type=CharacterEventType.FRIEND, char_list=[Character.GUNDHAM_TANAKA, Character.PEKO_PEKOYAMA])
    HAJIME_AND_GUNDHAM = _CharacterEventData(event_name="Hajime & Gundham", event_type=CharacterEventType.FRIEND, char_list=[Character.HAJIME_HINATA, Character.GUNDHAM_TANAKA])
    HAJIME_AND_HIYOKO = _CharacterEventData(event_name="Hajime & Hiyoko", event_type=CharacterEventType.FRIEND, char_list=[Character.HAJIME_HINATA, Character.HIYOKO_SAIONJI])
    HAJIME_AND_MAHIRU_AND_MIKAN = _CharacterEventData(event_name="Hajime & Mahiru & Mikan", event_type=CharacterEventType.FRIEND, char_list=[Character.HAJIME_HINATA, Character.MAHIRU_KOIZUMI, Character.MIKAN_TSUMIKI])
    HIFUMI_AND_HIYOKO_AND_KOTOKO = _CharacterEventData(event_name="Hifumi & Hiyoko & Kotoko", event_type=CharacterEventType.FRIEND, char_list=[Character.HIFUMI_YAMADA, Character.HIYOKO_SAIONJI, Character.KOTOKO_UTSUGI])
    HIFUMI_AND_NAGISA = _CharacterEventData(event_name="Hifumi & Nagisa", event_type=CharacterEventType.FRIEND, char_list=[Character.HIFUMI_YAMADA, Character.NAGISA_SHINGETSU])
    HIFUMI_AND_PEKO = _CharacterEventData(event_name="Hifumi & Peko", event_type=CharacterEventType.FRIEND, char_list=[Character.HIFUMI_YAMADA, Character.PEKO_PEKOYAMA])
    HIFUMI_AND_TERUTERU = _CharacterEventData(event_name="Hifumi & Teruteru", event_type=CharacterEventType.FRIEND, char_list=[Character.HIFUMI_YAMADA, Character.TERUTERU_HANAMURA])
    HIFUMI_AND_TOKO = _CharacterEventData(event_name="Hifumi & Toko", event_type=CharacterEventType.FRIEND, char_list=[Character.HIFUMI_YAMADA, Character.TOKO_FUKAWA])
    HIMIKO_AND_AKANE_AND_KOTOKO = _CharacterEventData(event_name="Himiko & Akane & Kotoko", event_type=CharacterEventType.FRIEND, char_list=[Character.HIMIKO_YUMENO, Character.AKANE_OWARI, Character.KOTOKO_UTSUGI])
    HIMIKO_AND_CELESTIA_AND_TERUTERU = _CharacterEventData(event_name="Himiko & Celestia & Teruteru", event_type=CharacterEventType.FRIEND, char_list=[Character.HIMIKO_YUMENO, Character.CELESTIA_LUDENBERG, Character.TERUTERU_HANAMURA])
    HIMIKO_AND_HAJIME = _CharacterEventData(event_name="Himiko & Hajime", event_type=CharacterEventType.FRIEND, char_list=[Character.HIMIKO_YUMENO, Character.HAJIME_HINATA])
    HIMIKO_AND_HIYOKO_AND_MAHIRU = _CharacterEventData(event_name="Himiko & Hiyoko & Mahiru", event_type=CharacterEventType.FRIEND, char_list=[Character.HIMIKO_YUMENO, Character.HIYOKO_SAIONJI, Character.MAHIRU_KOIZUMI])
    HIMIKO_AND_IBUKI = _CharacterEventData(event_name="Himiko & Ibuki", event_type=CharacterEventType.FRIEND, char_list=[Character.HIMIKO_YUMENO, Character.IBUKI_MIODA])
    HIMIKO_AND_MASARU = _CharacterEventData(event_name="Himiko & Masaru", event_type=CharacterEventType.FRIEND, char_list=[Character.HIMIKO_YUMENO, Character.MASARU_DAIMON])
    HIMIKO_AND_SAKURA_AND_NEKOMARU = _CharacterEventData(event_name="Himiko & Sakura & Nekomaru", event_type=CharacterEventType.FRIEND, char_list=[Character.HIMIKO_YUMENO, Character.SAKURA_OGAMI, Character.NEKOMARU_NIDAI])
    HIMIKO_AND_TENKO = _CharacterEventData(event_name="Himiko & Tenko", event_type=CharacterEventType.FRIEND, char_list=[Character.HIMIKO_YUMENO, Character.TENKO_CHABASHIRA])
    HIMIKO_AND_YASUHIRO = _CharacterEventData(event_name="Himiko & Yasuhiro", event_type=CharacterEventType.FRIEND, char_list=[Character.HIMIKO_YUMENO, Character.YASUHIRO_HAGAKURE])
    HIYOKO_AND_MONACA = _CharacterEventData(event_name="Hiyoko & Monaca", event_type=CharacterEventType.FRIEND, char_list=[Character.HIYOKO_SAIONJI, Character.MONACA_TOWA])
    HIYOKO_AND_SHIROKUMA_AND_HIROKO = _CharacterEventData(event_name="Hiyoko & Shirokuma & Hiroko", event_type=CharacterEventType.FRIEND, char_list=[Character.HIMIKO_YUMENO, Character.SHIROKUMA, Character.HIROKO_HAGAKURE])
    IBUKI_AND_KUROKUMA = _CharacterEventData(event_name="Ibuki & Kurokuma", event_type=CharacterEventType.FRIEND, char_list=[Character.IBUKI_MIODA, Character.KUROKUMA])
    IBUKI_AND_MONOMI = _CharacterEventData(event_name="Ibuki & Monomi", event_type=CharacterEventType.FRIEND, char_list=[Character.IBUKI_MIODA, Character.MONOMI])
    IZURU_AND_BYAKUYA = _CharacterEventData(event_name="Izuru & Byakuya", event_type=CharacterEventType.FRIEND, char_list=[Character.IZURU_KAMUKURA, Character.BYAKUYA_TOGAMI])
    IZURU_AND_GONTA = _CharacterEventData(event_name="Izuru & Gonta", event_type=CharacterEventType.FRIEND, char_list=[Character.IZURU_KAMUKURA, Character.GONTA_GOKUHARA])
    IZURU_AND_GUNDHAM = _CharacterEventData(event_name="Izuru & Gundham", event_type=CharacterEventType.FRIEND, char_list=[Character.IZURU_KAMUKURA, Character.GUNDHAM_TANAKA])
    IZURU_AND_HIMIKO = _CharacterEventData(event_name="Izuru & Himiko", event_type=CharacterEventType.FRIEND, char_list=[Character.IZURU_KAMUKURA, Character.HIMIKO_YUMENO])
    IZURU_AND_HIYOKO = _CharacterEventData(event_name="Izuru & Hiyoko", event_type=CharacterEventType.FRIEND, char_list=[Character.IZURU_KAMUKURA, Character.HIYOKO_SAIONJI])
    IZURU_AND_KIRUMI_AND_CHIAKI = _CharacterEventData(event_name="Izuru & Kirumi & Chiaki", event_type=CharacterEventType.FRIEND, char_list=[Character.IZURU_KAMUKURA, Character.KIRUMI_TOJO, Character.CHIAKI_NANAMI])
    IZURU_AND_LEON_AND_CHIHIRO = _CharacterEventData(event_name="Izuru & Leon & Chihiro", event_type=CharacterEventType.FRIEND, char_list=[Character.IZURU_KAMUKURA, Character.LEON_KUWATA, Character.CHIHIRO_FUJISAKI])
    IZURU_AND_MAHIRU_AND_MIKAN = _CharacterEventData(event_name="Izuru & Mahiru & Mikan", event_type=CharacterEventType.FRIEND, char_list=[Character.IZURU_KAMUKURA, Character.MAHIRU_KOIZUMI, Character.MIKAN_TSUMIKI])
    IZURU_AND_MONOKUMA = _CharacterEventData(event_name="Izuru & Monokuma", event_type=CharacterEventType.FRIEND, char_list=[Character.IZURU_KAMUKURA, Character.MONOKUMA])
    IZURU_AND_RYOMA_AND_NAGITO = _CharacterEventData(event_name="Izuru & Ryoma & Nagito", event_type=CharacterEventType.FRIEND, char_list=[Character.IZURU_KAMUKURA, Character.RYOMA_HOSHI, Character.NAGITO_KOMAEDA])
    IZURU_AND_SAYAKA = _CharacterEventData(event_name="Izuru & Sayaka", event_type=CharacterEventType.FRIEND, char_list=[Character.IZURU_KAMUKURA, Character.SAYAKA_MAIZONO])
    JATARO_AND_KOTOKO = _CharacterEventData(event_name="Jataro & Kotoko", event_type=CharacterEventType.FRIEND, char_list=[Character.JATARO_KEMURI, Character.KOTOKO_UTSUGI])
    JATARO_AND_KUROKUMA = _CharacterEventData(event_name="Jataro & Kurokuma", event_type=CharacterEventType.FRIEND, char_list=[Character.JATARO_KEMURI, Character.KUROKUMA])
    JUNKO_AND_AOI = _CharacterEventData(event_name="Junko & Aoi", event_type=CharacterEventType.FRIEND, char_list=[Character.JUNKO_ENOSHIMA, Character.AOI_ASAHINA])
    JUNKO_AND_BYAKUYA = _CharacterEventData(event_name="Junko & Byakuya", event_type=CharacterEventType.FRIEND, char_list=[Character.JUNKO_ENOSHIMA, Character.BYAKUYA_TOGAMI])
    JUNKO_AND_GONTA_AND_MONACA = _CharacterEventData(event_name="Junko & Gonta & Monaca", event_type=CharacterEventType.FRIEND, char_list=[Character.JUNKO_ENOSHIMA, Character.GONTA_GOKUHARA, Character.MONACA_TOWA])
    JUNKO_AND_MAHIRU = _CharacterEventData(event_name="Junko & Mahiru", event_type=CharacterEventType.FRIEND, char_list=[Character.JUNKO_ENOSHIMA, Character.MAHIRU_KOIZUMI])
    JUNKO_AND_MONDO = _CharacterEventData(event_name="Junko & Mondo", event_type=CharacterEventType.FRIEND, char_list=[Character.JUNKO_ENOSHIMA, Character.MONDO_OWADA])
    JUNKO_AND_SAKURA_AND_IBUKI = _CharacterEventData(event_name="Junko & Sakura & Ibuki", event_type=CharacterEventType.FRIEND, char_list=[Character.JUNKO_ENOSHIMA, Character.SAKURA_OGAMI, Character.IBUKI_MIODA])
    JUNKO_AND_TENKO_AND_AKANE = _CharacterEventData(event_name="Junko & Tenko & Akane", event_type=CharacterEventType.FRIEND, char_list=[Character.JUNKO_ENOSHIMA, Character.TENKO_CHABASHIRA, Character.AKANE_OWARI])
    JUNKO_AND_TOKO_AND_MIKAN = _CharacterEventData(event_name="Junko & Toko & Mikan", event_type=CharacterEventType.FRIEND, char_list=[Character.JUNKO_ENOSHIMA, Character.TOKO_FUKAWA, Character.MIKAN_TSUMIKI])
    JUNKO_AND_YASUHIRO = _CharacterEventData(event_name="Junko & Yasuhiro", event_type=CharacterEventType.FRIEND, char_list=[Character.JUNKO_ENOSHIMA, Character.YASUHIRO_HAGAKURE])
    MUKURO_AND_MAHIRU = _CharacterEventData(event_name="Mukuro & Mahiru", event_type=CharacterEventType.FRIEND, char_list=[Character.MUKURO_IKUSABA, Character.MAHIRU_KOIZUMI])
    K1_B0_AND_ANGIE = _CharacterEventData(event_name="K1-B0 & Angie", event_type=CharacterEventType.FRIEND, char_list=[Character.K1_B0, Character.ANGIE_YONAGA])
    K1_B0_AND_IMPOSTER = _CharacterEventData(event_name="K1-B0 & The Ultimate Imposter", event_type=CharacterEventType.FRIEND, char_list=[Character.K1_B0, Character.THE_ULTIMATE_IMPOSTER])
    K1_B0_AND_CELESTIA = _CharacterEventData(event_name="K1-B0 & Celestia", event_type=CharacterEventType.FRIEND, char_list=[Character.K1_B0, Character.CELESTIA_LUDENBERG])
    K1_B0_AND_CHIAKI = _CharacterEventData(event_name="K1-B0 & Chiaki", event_type=CharacterEventType.FRIEND, char_list=[Character.K1_B0, Character.CHIAKI_NANAMI])
    K1_B0_AND_CHIHIRO_AND_KAZUICHI = _CharacterEventData(event_name="K1-B0 & Chihiro & Kazuichi", event_type=CharacterEventType.FRIEND, char_list=[Character.K1_B0, Character.CHIHIRO_FUJISAKI, Character.KAZUICHI_SODA])
    K1_B0_AND_LEON = _CharacterEventData(event_name="K1-B0 & Leon", event_type=CharacterEventType.FRIEND, char_list=[Character.K1_B0, Character.LEON_KUWATA])
    K1_B0_AND_MASARU_AND_JATARO = _CharacterEventData(event_name="K1-B0 & Masaru & Jataro", event_type=CharacterEventType.FRIEND, char_list=[Character.K1_B0, Character.MASARU_DAIMON, Character.JATARO_KEMURI])
    K1_B0_AND_TERUTERU = _CharacterEventData(event_name="K1-B0 & Teruteru", event_type=CharacterEventType.FRIEND, char_list=[Character.K1_B0, Character.TERUTERU_HANAMURA])
    KAEDE_AND_FUYUHIKO = _CharacterEventData(event_name="Kaede & Fuyuhiko", event_type=CharacterEventType.FRIEND, char_list=[Character.KAEDE_AKAMATSU, Character.FUYUHIKO_KUZURYU])
    KAEDE_AND_KOMARU = _CharacterEventData(event_name="Kaede & Komaru", event_type=CharacterEventType.FRIEND, char_list=[Character.KAEDE_AKAMATSU, Character.KOMARU_NAEGI])
    KAEDE_AND_MAKOTO_AND_MASARU = _CharacterEventData(event_name="Kaede & Makoto & Masaru", event_type=CharacterEventType.FRIEND, char_list=[Character.KAEDE_AKAMATSU, Character.MAKOTO_NAEGI, Character.MASARU_DAIMON])
    KAEDE_AND_SAYAKA_AND_IBUKI = _CharacterEventData(event_name="Kaede & Sayaka & Ibuki", event_type=CharacterEventType.FRIEND, char_list=[Character.KAEDE_AKAMATSU, Character.SAYAKA_MAIZONO, Character.IBUKI_MIODA])
    KAITO_AND_AKANE = _CharacterEventData(event_name="Kaito & Akane", event_type=CharacterEventType.FRIEND, char_list=[Character.KAITO_MOMOTA, Character.AKANE_OWARI])
    KAITO_AND_AOI = _CharacterEventData(event_name="Kaito & Aoi", event_type=CharacterEventType.FRIEND, char_list=[Character.KAITO_MOMOTA, Character.AOI_ASAHINA])
    KAITO_AND_BYAKUYA_AND_IBUKI = _CharacterEventData(event_name="Kaito & Byakuya & Ibuki", event_type=CharacterEventType.FRIEND, char_list=[Character.KAITO_MOMOTA, Character.BYAKUYA_TOGAMI, Character.IBUKI_MIODA])
    KAITO_AND_GUNDHAM = _CharacterEventData(event_name="Kaito & Gundham", event_type=CharacterEventType.FRIEND, char_list=[Character.KAITO_MOMOTA, Character.GUNDHAM_TANAKA])
    KAITO_AND_JATARO = _CharacterEventData(event_name="Kaito & Jataro", event_type=CharacterEventType.FRIEND, char_list=[Character.KAITO_MOMOTA, Character.JATARO_KEMURI])
    KAITO_AND_KAEDE = _CharacterEventData(event_name="Kaito & Kaede", event_type=CharacterEventType.FRIEND, char_list=[Character.KAITO_MOMOTA, Character.KAEDE_AKAMATSU])
    KAITO_AND_KIYOTAKA_AND_MASARU = _CharacterEventData(event_name="Kaito & Kiyotaka & Masaru", event_type=CharacterEventType.FRIEND, char_list=[Character.KAITO_MOMOTA, Character.KIYOTAKA_ISHIMARU, Character.MASARU_DAIMON])
    KAITO_AND_RYOMA = _CharacterEventData(event_name="Kaito & Ryoma", event_type=CharacterEventType.FRIEND, char_list=[Character.KAITO_MOMOTA, Character.RYOMA_HOSHI])
    KAITO_AND_TENKO_AND_LEON = _CharacterEventData(event_name="Kaito & Tenko & Leon", event_type=CharacterEventType.FRIEND, char_list=[Character.KAITO_MOMOTA, Character.TENKO_CHABASHIRA, Character.LEON_KUWATA])
    KAZUICHI_AND_FUYUHIKO_AND_NAGISA = _CharacterEventData(event_name="Kazuichi & Fuyuhiko & Nagisa", event_type=CharacterEventType.FRIEND, char_list=[Character.KAZUICHI_SODA, Character.FUYUHIKO_KUZURYU, Character.NAGISA_SHINGETSU])
    KAZUICHI_AND_JATARO = _CharacterEventData(event_name="Kazuichi & Jataro", event_type=CharacterEventType.FRIEND, char_list=[Character.KAZUICHI_SODA, Character.JATARO_KEMURI])
    KAZUICHI_AND_MAHIRU = _CharacterEventData(event_name="Kazuichi & Mahiru", event_type=CharacterEventType.FRIEND, char_list=[Character.KAZUICHI_SODA, Character.MAHIRU_KOIZUMI])
    KIRUMI_AND_CHIHIRO = _CharacterEventData(event_name="Kirumi & Chihiro", event_type=CharacterEventType.FRIEND, char_list=[Character.KIRUMI_TOJO, Character.CHIHIRO_FUJISAKI])
    KIRUMI_AND_HAJIME_AND_CHIAKI = _CharacterEventData(event_name="Kirumi & Hajime & Chiaki", event_type=CharacterEventType.FRIEND, char_list=[Character.KIRUMI_TOJO, Character.HAJIME_HINATA, Character.CHIAKI_NANAMI])
    KIRUMI_AND_KOMARU = _CharacterEventData(event_name="Kirumi & Komaru", event_type=CharacterEventType.FRIEND, char_list=[Character.KIRUMI_TOJO, Character.KOMARU_NAEGI])
    KIRUMI_AND_LEON_AND_KYOKO = _CharacterEventData(event_name="Kirumi & Leon & Kyoko", event_type=CharacterEventType.FRIEND, char_list=[Character.KIRUMI_TOJO, Character.LEON_KUWATA, Character.KYOKO_KIRIGIRI])
    KIRUMI_AND_MAHIRU = _CharacterEventData(event_name="Kirumi & Mahiru", event_type=CharacterEventType.FRIEND, char_list=[Character.KIRUMI_TOJO, Character.MAHIRU_KOIZUMI])
    KIRUMI_AND_SAKURA = _CharacterEventData(event_name="Kirumi & Sakura", event_type=CharacterEventType.FRIEND, char_list=[Character.KIRUMI_TOJO, Character.SAKURA_OGAMI])
    KIRUMI_AND_SONIA = _CharacterEventData(event_name="Kirumi & Sonia", event_type=CharacterEventType.FRIEND, char_list=[Character.KIRUMI_TOJO, Character.SONIA_NEVERMIND])
    KIRUMI_AND_TERUTERU_AND_SONIA = _CharacterEventData(event_name="Kirumi & Teruteru & Sonia", event_type=CharacterEventType.FRIEND, char_list=[Character.KIRUMI_TOJO, Character.TERUTERU_HANAMURA, Character.SONIA_NEVERMIND])
    KIRUMI_AND_TSUMUGI = _CharacterEventData(event_name="Kirumi & Tsumugi", event_type=CharacterEventType.FRIEND, char_list=[Character.KIRUMI_TOJO, Character.TSUMUGI_SHIROGANE])
    KIYOTAKA_AND_AKANE = _CharacterEventData(event_name="Kiyotaka & Akane", event_type=CharacterEventType.FRIEND, char_list=[Character.KIYOTAKA_ISHIMARU, Character.AKANE_OWARI])
    KIYOTAKA_AND_CELESTIA = _CharacterEventData(event_name="Kiyotaka & Celestia", event_type=CharacterEventType.FRIEND, char_list=[Character.KIYOTAKA_ISHIMARU, Character.CELESTIA_LUDENBERG])
    KIYOTAKA_AND_MONDO_AND_SAYAKA = _CharacterEventData(event_name="Kiyotaka & Mondo & Sayaka", event_type=CharacterEventType.FRIEND, char_list=[Character.KIYOTAKA_ISHIMARU, Character.MONDO_OWADA, Character.SAYAKA_MAIZONO])
    KIYOTAKA_AND_NAGISA = _CharacterEventData(event_name="Kiyotaka & Nagisa", event_type=CharacterEventType.FRIEND, char_list=[Character.KIYOTAKA_ISHIMARU, Character.NAGISA_SHINGETSU])
    KIYOTAKA_AND_NEKOMARU = _CharacterEventData(event_name="Kiyotaka & Nekomaru", event_type=CharacterEventType.FRIEND, char_list=[Character.KIYOTAKA_ISHIMARU, Character.NEKOMARU_NIDAI])
    KOKICHI_AND_BYAKUYA_AND_IMPOSTER = _CharacterEventData(event_name="Kokichi & Byakuya & The Ultimate Imposter", event_type=CharacterEventType.FRIEND, char_list=[Character.KOKICHI_OMA, Character.BYAKUYA_TOGAMI, Character.THE_ULTIMATE_IMPOSTER])
    KOKICHI_AND_JACK = _CharacterEventData(event_name="Kokichi & Genocide Jack", event_type=CharacterEventType.FRIEND, char_list=[Character.KOKICHI_OMA, Character.GENOCIDE_JACK])
    KOKICHI_AND_HIYOKO = _CharacterEventData(event_name="Kokichi & Hiyoko", event_type=CharacterEventType.FRIEND, char_list=[Character.KOKICHI_OMA, Character.HIYOKO_SAIONJI])
    KOKICHI_AND_KAZUICHI = _CharacterEventData(event_name="Kokichi & Kazuichi", event_type=CharacterEventType.FRIEND, char_list=[Character.KOKICHI_OMA, Character.KAZUICHI_SODA])
    KOKICHI_AND_MAHIRU = _CharacterEventData(event_name="Kokichi & Mahiru", event_type=CharacterEventType.FRIEND, char_list=[Character.KOKICHI_OMA, Character.MAHIRU_KOIZUMI])
    KOKICHI_AND_MAKOTO_AND_HIROKO = _CharacterEventData(event_name="Kokichi & Makoto & Hiroko", event_type=CharacterEventType.FRIEND, char_list=[Character.KOKICHI_OMA, Character.MAKOTO_NAEGI, Character.HIROKO_HAGAKURE])
    KOKICHI_AND_MONACA = _CharacterEventData(event_name="Kokichi & Monaca", event_type=CharacterEventType.FRIEND, char_list=[Character.KOKICHI_OMA, Character.MONACA_TOWA])
    KOKICHI_AND_MONOKUMA_AND_CHIAKI = _CharacterEventData(event_name="Kokichi & Monokuma & Chiaki", event_type=CharacterEventType.FRIEND, char_list=[Character.KOKICHI_OMA, Character.MONOKUMA, Character.CHIAKI_NANAMI])
    KOMARU_AND_KOTOKO_AND_MONACA = _CharacterEventData(event_name="Komaru & Kotoko & Monaca", event_type=CharacterEventType.FRIEND, char_list=[Character.KOMARU_NAEGI, Character.KOTOKO_UTSUGI, Character.MONACA_TOWA])
    KOREKIYO_AND_ANGIE_AND_TOKO = _CharacterEventData(event_name="Korekiyo & Angie & Toko", event_type=CharacterEventType.FRIEND, char_list=[Character.KOREKIYO_SHINGUJI, Character.ANGIE_YONAGA, Character.TOKO_FUKAWA])
    KOREKIYO_AND_HIFUMI = _CharacterEventData(event_name="Korekiyo & Hifumi", event_type=CharacterEventType.FRIEND, char_list=[Character.KOREKIYO_SHINGUJI, Character.HIFUMI_YAMADA])
    KOREKIYO_AND_HIFUMI_AND_SONIA = _CharacterEventData(event_name="Korekiyo & Hifumi & Sonia", event_type=CharacterEventType.FRIEND, char_list=[Character.KOREKIYO_SHINGUJI, Character.HIFUMI_YAMADA, Character.SONIA_NEVERMIND])
    KOREKIYO_AND_MIKAN = _CharacterEventData(event_name="Korekiyo & Mikan", event_type=CharacterEventType.FRIEND, char_list=[Character.KOREKIYO_SHINGUJI, Character.MIKAN_TSUMIKI])
    KOREKIYO_AND_NAGITO = _CharacterEventData(event_name="Korekiyo & Nagito", event_type=CharacterEventType.FRIEND, char_list=[Character.KOREKIYO_SHINGUJI, Character.NAGITO_KOMAEDA])
    KOREKIYO_AND_SAYAKA = _CharacterEventData(event_name="Korekiyo & Sayaka", event_type=CharacterEventType.FRIEND, char_list=[Character.KOREKIYO_SHINGUJI, Character.SAYAKA_MAIZONO])
    KOREKIYO_AND_SHIROKUMA = _CharacterEventData(event_name="Korekiyo & Shirokuma", event_type=CharacterEventType.FRIEND, char_list=[Character.KOREKIYO_SHINGUJI, Character.SHIROKUMA])
    KOREKIYO_AND_TSUMUGI = _CharacterEventData(event_name="Korekiyo & Tsumugi", event_type=CharacterEventType.FRIEND, char_list=[Character.KOREKIYO_SHINGUJI, Character.TSUMUGI_SHIROGANE])
    KYOKO_AND_FUYUHIKO_AND_KUROKUMA = _CharacterEventData(event_name="Kyoko & Fuyuhiko & Kurokuma", event_type=CharacterEventType.FRIEND, char_list=[Character.KYOKO_KIRIGIRI, Character.FUYUHIKO_KUZURYU, Character.KUROKUMA])
    KYOKO_AND_GUNDHAM = _CharacterEventData(event_name="Kyoko & Gundham", event_type=CharacterEventType.FRIEND, char_list=[Character.KYOKO_KIRIGIRI, Character.GUNDHAM_TANAKA])
    KYOKO_AND_MAHIRU = _CharacterEventData(event_name="Kyoko & Mahiru", event_type=CharacterEventType.FRIEND, char_list=[Character.KYOKO_KIRIGIRI, Character.MAHIRU_KOIZUMI])
    KYOKO_AND_MONACA = _CharacterEventData(event_name="Kyoko & Monaca", event_type=CharacterEventType.FRIEND, char_list=[Character.KYOKO_KIRIGIRI, Character.MONACA_TOWA])
    LEON_AND_CHIAKI = _CharacterEventData(event_name="Leon & Chiaki", event_type=CharacterEventType.FRIEND, char_list=[Character.LEON_KUWATA, Character.CHIAKI_NANAMI])
    LEON_AND_HAJIME_AND_CHIHIRO = _CharacterEventData(event_name="Leon & Hajime & Chihiro", event_type=CharacterEventType.FRIEND, char_list=[Character.LEON_KUWATA, Character.HAJIME_HINATA, Character.CHIHIRO_FUJISAKI])
    LEON_AND_HIFUMI = _CharacterEventData(event_name="Leon & Hifumi", event_type=CharacterEventType.FRIEND, char_list=[Character.LEON_KUWATA, Character.HIFUMI_YAMADA])
    LEON_AND_NAGITO = _CharacterEventData(event_name="Leon & Nagito", event_type=CharacterEventType.FRIEND, char_list=[Character.LEON_KUWATA, Character.NAGITO_KOMAEDA])
    LEON_AND_SAKURA = _CharacterEventData(event_name="Leon & Sakura", event_type=CharacterEventType.FRIEND, char_list=[Character.LEON_KUWATA, Character.SAKURA_OGAMI])
    MAHIRU_AND_NAGISA = _CharacterEventData(event_name="Mahiru & Nagisa", event_type=CharacterEventType.FRIEND, char_list=[Character.MAHIRU_KOIZUMI, Character.NAGISA_SHINGETSU])
    MAKI_AND_IMPOSTER = _CharacterEventData(event_name="Maki & The Ultimate Imposter", event_type=CharacterEventType.FRIEND, char_list=[Character.MAKI_HARUKAWA, Character.THE_ULTIMATE_IMPOSTER])
    MAKI_AND_CHIHIRO_AND_CHIAKI = _CharacterEventData(event_name="Maki & Chihiro & Chiaki", event_type=CharacterEventType.FRIEND, char_list=[Character.MAKI_HARUKAWA, Character.CHIHIRO_FUJISAKI, Character.CHIAKI_NANAMI])
    MAKI_AND_KAEDE = _CharacterEventData(event_name="Maki & Kaede", event_type=CharacterEventType.FRIEND, char_list=[Character.MAKI_HARUKAWA, Character.KAEDE_AKAMATSU])
    MAKI_AND_KOMARU = _CharacterEventData(event_name="Maki & Komaru", event_type=CharacterEventType.FRIEND, char_list=[Character.MAKI_HARUKAWA, Character.KOMARU_NAEGI])
    MAKI_AND_MAKOTO = _CharacterEventData(event_name="Maki & Makoto", event_type=CharacterEventType.FRIEND, char_list=[Character.MAKI_HARUKAWA, Character.MAKOTO_NAEGI])
    MAKI_AND_MONOMI = _CharacterEventData(event_name="Maki & Monomi", event_type=CharacterEventType.FRIEND, char_list=[Character.MAKI_HARUKAWA, Character.MONOMI])
    MAKI_AND_NEKOMARU_AND_PEKO = _CharacterEventData(event_name="Maki & Nekomaru & Peko", event_type=CharacterEventType.FRIEND, char_list=[Character.MAKI_HARUKAWA, Character.NEKOMARU_NIDAI, Character.PEKO_PEKOYAMA])
    MAKI_AND_SAKURA_AND_NAGISA = _CharacterEventData(event_name="Maki & Sakura & Nagisa", event_type=CharacterEventType.FRIEND, char_list=[Character.MAKI_HARUKAWA, Character.SAKURA_OGAMI, Character.NAGISA_SHINGETSU])
    MAKI_AND_SAYAKA = _CharacterEventData(event_name="Maki & Sayaka", event_type=CharacterEventType.FRIEND, char_list=[Character.MAKI_HARUKAWA, Character.SAYAKA_MAIZONO])
    MAKI_AND_YASUHIRO_AND_HIYOKO = _CharacterEventData(event_name="Maki & Yasuhiro & Hiyoko", event_type=CharacterEventType.FRIEND, char_list=[Character.MAKI_HARUKAWA, Character.YASUHIRO_HAGAKURE, Character.HIYOKO_SAIONJI])
    MAKOTO_AND_BYAKUYA = _CharacterEventData(event_name="Makoto & Byakuya", event_type=CharacterEventType.FRIEND, char_list=[Character.MAKOTO_NAEGI, Character.BYAKUYA_TOGAMI])
    MAKOTO_AND_CHIAKI = _CharacterEventData(event_name="Makoto & Chiaki", event_type=CharacterEventType.FRIEND, char_list=[Character.MAKOTO_NAEGI, Character.CHIAKI_NANAMI])
    MAKOTO_AND_GUNDHAM = _CharacterEventData(event_name="Makoto & Gundham", event_type=CharacterEventType.FRIEND, char_list=[Character.MAKOTO_NAEGI, Character.GUNDHAM_TANAKA])
    MAKOTO_AND_MUKURO = _CharacterEventData(event_name="Makoto & Mukuro", event_type=CharacterEventType.FRIEND, char_list=[Character.MAKOTO_NAEGI, Character.MUKURO_IKUSABA])
    MAKOTO_AND_SAYAKA_AND_KOMARU = _CharacterEventData(event_name="Makoto & Sayaka & Komaru", event_type=CharacterEventType.FRIEND, char_list=[Character.MAKOTO_NAEGI, Character.SAYAKA_MAIZONO, Character.KOMARU_NAEGI])
    MASARU_AND_JATARO_AND_NAGISA = _CharacterEventData(event_name="Masaru & Jataro & Nagisa", event_type=CharacterEventType.FRIEND, char_list=[Character.MASARU_DAIMON, Character.JATARO_KEMURI, Character.NAGISA_SHINGETSU])
    MASARU_AND_KOTOKO = _CharacterEventData(event_name="Masaru & Kotoko", event_type=CharacterEventType.FRIEND, char_list=[Character.MASARU_DAIMON, Character.KOTOKO_UTSUGI])
    MIKAN_AND_SHIROKUMA = _CharacterEventData(event_name="Mikan & Shirokuma", event_type=CharacterEventType.FRIEND, char_list=[Character.MIKAN_TSUMIKI, Character.SHIROKUMA])
    MIU_AND_BYAKUYA_JACK = _CharacterEventData(event_name="Miu & Byakuya & Genocide Jack", event_type=CharacterEventType.FRIEND, char_list=[Character.MIU_IRUMA, Character.BYAKUYA_TOGAMI, Character.GENOCIDE_JACK])
    MIU_AND_JATARO = _CharacterEventData(event_name="Miu & Jataro", event_type=CharacterEventType.FRIEND, char_list=[Character.MIU_IRUMA, Character.JATARO_KEMURI])
    MIU_AND_KAEDE = _CharacterEventData(event_name="Miu & Kaede", event_type=CharacterEventType.FRIEND, char_list=[Character.MIU_IRUMA, Character.KAEDE_AKAMATSU])
    MIU_AND_KAZUICHI_AND_MONOMI = _CharacterEventData(event_name="Miu & Kazuichi & Monomi", event_type=CharacterEventType.FRIEND, char_list=[Character.MIU_IRUMA, Character.KAZUICHI_SODA, Character.MONOMI])
    MIU_AND_KUROKUMA = _CharacterEventData(event_name="Miu & Kurokuma", event_type=CharacterEventType.FRIEND, char_list=[Character.MIU_IRUMA, Character.KUROKUMA])
    MIU_AND_MIKAN = _CharacterEventData(event_name="Miu & Mikan", event_type=CharacterEventType.FRIEND, char_list=[Character.MIU_IRUMA, Character.MIKAN_TSUMIKI])
    MIU_AND_MONDO_AND_HIROKO = _CharacterEventData(event_name="Miu & Mondo & Hiroko", event_type=CharacterEventType.FRIEND, char_list=[Character.MIU_IRUMA, Character.MONDO_OWADA, Character.HIROKO_HAGAKURE])
    MIU_AND_MONOMI = _CharacterEventData(event_name="Miu & Monomi", event_type=CharacterEventType.FRIEND, char_list=[Character.MIU_IRUMA, Character.MONOMI])
    MIU_AND_YASUHIRO = _CharacterEventData(event_name="Miu & Yasuhiro", event_type=CharacterEventType.FRIEND, char_list=[Character.MIU_IRUMA, Character.YASUHIRO_HAGAKURE])
    MONACA_AND_HIROKO = _CharacterEventData(event_name="Monaca & Hiroko", event_type=CharacterEventType.FRIEND, char_list=[Character.MONACA_TOWA, Character.HIROKO_HAGAKURE])
    MONDO_AND_FUYUHIKO = _CharacterEventData(event_name="Mondo & Fuyuhiko", event_type=CharacterEventType.FRIEND, char_list=[Character.MONDO_OWADA, Character.FUYUHIKO_KUZURYU])
    MONDO_AND_MUKURO = _CharacterEventData(event_name="Mondo & Mukuro", event_type=CharacterEventType.FRIEND, char_list=[Character.MONDO_OWADA, Character.MUKURO_IKUSABA])
    MONDO_AND_KAZUICHI = _CharacterEventData(event_name="Mondo & Kazuichi", event_type=CharacterEventType.FRIEND, char_list=[Character.MONDO_OWADA, Character.KAZUICHI_SODA])
    MONDO_AND_MIKAN = _CharacterEventData(event_name="Mondo & Mikan", event_type=CharacterEventType.FRIEND, char_list=[Character.MONDO_OWADA, Character.MIKAN_TSUMIKI])
    MONDO_AND_NAGISA = _CharacterEventData(event_name="Mondo & Nagisa", event_type=CharacterEventType.FRIEND, char_list=[Character.MONDO_OWADA, Character.NAGISA_SHINGETSU])
    MONDO_AND_NEKOMARU_AND_KUROKUMA = _CharacterEventData(event_name="Mondo & Nekomaru & Kurokuma", event_type=CharacterEventType.FRIEND, char_list=[Character.MONDO_OWADA, Character.NEKOMARU_NIDAI, Character.KUROKUMA])
    MONOKUMA_AND_CHIHIRO = _CharacterEventData(event_name="Monokuma & Chihiro", event_type=CharacterEventType.FRIEND, char_list=[Character.MONOKUMA, Character.CHIHIRO_FUJISAKI])
    MONOKUMA_AND_JACK = _CharacterEventData(event_name="Monokuma & Genocide Jack", event_type=CharacterEventType.FRIEND, char_list=[Character.MONOKUMA, Character.GENOCIDE_JACK])
    MONOKUMA_AND_HAJIME = _CharacterEventData(event_name="Monokuma & Hajime", event_type=CharacterEventType.FRIEND, char_list=[Character.MONOKUMA, Character.HAJIME_HINATA])
    MONOKUMA_AND_HIYOKO = _CharacterEventData(event_name="Monokuma & Hiyoko", event_type=CharacterEventType.FRIEND, char_list=[Character.MONOKUMA, Character.HIYOKO_SAIONJI])
    MONOKUMA_AND_KOMARU_AND_HIROKO = _CharacterEventData(event_name="Monokuma & Komaru & Hiroko", event_type=CharacterEventType.FRIEND, char_list=[Character.MONOKUMA, Character.KOMARU_NAEGI, Character.HIROKO_HAGAKURE])
    MONOKUMA_AND_MONOMI = _CharacterEventData(event_name="Monokuma & Monomi", event_type=CharacterEventType.FRIEND, char_list=[Character.MONOKUMA, Character.MONOMI])
    MONOKUMA_AND_SHIROKUMA_AND_KUROKUMA = _CharacterEventData(event_name="Monokuma & Shirokuma & Kurokuma", event_type=CharacterEventType.FRIEND, char_list=[Character.MONOKUMA, Character.SHIROKUMA, Character.KUROKUMA])
    MONOMI_AND_KUROKUMA = _CharacterEventData(event_name="Monomi & Kurokuma", event_type=CharacterEventType.FRIEND, char_list=[Character.MONOMI, Character.KUROKUMA])
    NAGISA_AND_MONACA = _CharacterEventData(event_name="Nagisa & Monaca", event_type=CharacterEventType.FRIEND, char_list=[Character.NAGISA_SHINGETSU, Character.MONACA_TOWA])
    NAGISA_AND_SHIROKUMA = _CharacterEventData(event_name="Nagisa & Shirokuma", event_type=CharacterEventType.FRIEND, char_list=[Character.NAGISA_SHINGETSU, Character.SHIROKUMA])
    NAGITO_AND_KAZUICHI = _CharacterEventData(event_name="Nagito & Kazuichi", event_type=CharacterEventType.FRIEND, char_list=[Character.NAGITO_KOMAEDA, Character.KAZUICHI_SODA])
    NAGITO_AND_MIKAN = _CharacterEventData(event_name="Nagito & Mikan", event_type=CharacterEventType.FRIEND, char_list=[Character.NAGITO_KOMAEDA, Character.MIKAN_TSUMIKI])
    NAGITO_AND_MONACA = _CharacterEventData(event_name="Nagito & Monaca", event_type=CharacterEventType.FRIEND, char_list=[Character.NAGITO_KOMAEDA, Character.MONACA_TOWA])
    NEKOMARU_AND_MASARU = _CharacterEventData(event_name="Nekomaru & Masaru", event_type=CharacterEventType.FRIEND, char_list=[Character.NEKOMARU_NIDAI, Character.MASARU_DAIMON])
    PEKO_AND_MASARU = _CharacterEventData(event_name="Peko & Masaru", event_type=CharacterEventType.FRIEND, char_list=[Character.PEKO_PEKOYAMA, Character.MASARU_DAIMON])
    RANTARO_AND_GONTA = _CharacterEventData(event_name="Rantaro & Gonta", event_type=CharacterEventType.FRIEND, char_list=[Character.RANTARO_AMAMI, Character.GONTA_GOKUHARA])
    RANTARO_AND_HIROKO = _CharacterEventData(event_name="Rantaro & Hiroko", event_type=CharacterEventType.FRIEND, char_list=[Character.RANTARO_AMAMI, Character.HIROKO_HAGAKURE])
    RANTARO_AND_IBUKI = _CharacterEventData(event_name="Rantaro & Ibuki", event_type=CharacterEventType.FRIEND, char_list=[Character.RANTARO_AMAMI, Character.IBUKI_MIODA])
    RANTARO_AND_KAEDE = _CharacterEventData(event_name="Rantaro & Kaede", event_type=CharacterEventType.FRIEND, char_list=[Character.RANTARO_AMAMI, Character.KAEDE_AKAMATSU])
    RANTARO_AND_KIYOTAKA_AND_IMPOSTER = _CharacterEventData(event_name="Rantaro & Kiyotaka & The Ultimate Imposter", event_type=CharacterEventType.FRIEND, char_list=[Character.RANTARO_AMAMI, Character.KIYOTAKA_ISHIMARU, Character.THE_ULTIMATE_IMPOSTER])
    RANTARO_AND_KOREKIYO_AND_FUYUHIKO = _CharacterEventData(event_name="Rantaro & Korekiyo & Fuyuhiko", event_type=CharacterEventType.FRIEND, char_list=[Character.RANTARO_AMAMI, Character.KOREKIYO_SHINGUJI, Character.FUYUHIKO_KUZURYU])
    RANTARO_AND_LEON = _CharacterEventData(event_name="Rantaro & Leon", event_type=CharacterEventType.FRIEND, char_list=[Character.RANTARO_AMAMI, Character.LEON_KUWATA])
    RANTARO_AND_MAHIRU = _CharacterEventData(event_name="Rantaro & Mahiru", event_type=CharacterEventType.FRIEND, char_list=[Character.RANTARO_AMAMI, Character.MAHIRU_KOIZUMI])
    RANTARO_AND_PEKO_AND_SHIROKUMA = _CharacterEventData(event_name="Rantaro & Peko & Shirokuma", event_type=CharacterEventType.FRIEND, char_list=[Character.RANTARO_AMAMI, Character.PEKO_PEKOYAMA, Character.SHIROKUMA])
    RANTARO_AND_TERUTERU = _CharacterEventData(event_name="Rantaro & Teruteru", event_type=CharacterEventType.FRIEND, char_list=[Character.RANTARO_AMAMI, Character.TERUTERU_HANAMURA])
    RANTARO_AND_YASUHIRO_AND_NAGITO = _CharacterEventData(event_name="Rantaro & Yasuhiro & Nagito", event_type=CharacterEventType.FRIEND, char_list=[Character.RANTARO_AMAMI, Character.YASUHIRO_HAGAKURE, Character.NAGITO_KOMAEDA])
    RYOMA_AND_IMPOSTER = _CharacterEventData(event_name="Ryoma & The Ultimate Imposter", event_type=CharacterEventType.FRIEND, char_list=[Character.RYOMA_HOSHI, Character.THE_ULTIMATE_IMPOSTER])
    RYOMA_AND_HAJIME_AND_NAGITO = _CharacterEventData(event_name="Ryoma & Hajime & Nagito", event_type=CharacterEventType.FRIEND, char_list=[Character.RYOMA_HOSHI, Character.HAJIME_HINATA, Character.NAGITO_KOMAEDA])
    RYOMA_AND_HIMIKO = _CharacterEventData(event_name="Ryoma & Himiko", event_type=CharacterEventType.FRIEND, char_list=[Character.RYOMA_HOSHI, Character.HIMIKO_YUMENO])
    RYOMA_AND_KUROKUMA = _CharacterEventData(event_name="Ryoma & Kurokuma", event_type=CharacterEventType.FRIEND, char_list=[Character.RYOMA_HOSHI, Character.KUROKUMA])
    RYOMA_AND_KYOKO = _CharacterEventData(event_name="Ryoma & Kyoko", event_type=CharacterEventType.FRIEND, char_list=[Character.RYOMA_HOSHI, Character.KYOKO_KIRIGIRI])
    RYOMA_AND_MIU_AND_MONOKUMA = _CharacterEventData(event_name="Ryoma & Miu & Monokuma", event_type=CharacterEventType.FRIEND, char_list=[Character.RYOMA_HOSHI, Character.MIU_IRUMA, Character.MONOKUMA])
    RYOMA_AND_MONDO = _CharacterEventData(event_name="Ryoma & Mondo", event_type=CharacterEventType.FRIEND, char_list=[Character.RYOMA_HOSHI, Character.MONDO_OWADA])
    RYOMA_AND_NEKOMARU_AND_MIKAN = _CharacterEventData(event_name="Ryoma & Nekomaru & Mikan", event_type=CharacterEventType.FRIEND, char_list=[Character.RYOMA_HOSHI, Character.NEKOMARU_NIDAI, Character.MIKAN_TSUMIKI])
    RYOMA_AND_PEKO = _CharacterEventData(event_name="Ryoma & Peko", event_type=CharacterEventType.FRIEND, char_list=[Character.RYOMA_HOSHI, Character.PEKO_PEKOYAMA])
    RYOMA_AND_YASUHIRO_AND_MONACA = _CharacterEventData(event_name="Ryoma & Yasuhiro & Monaca", event_type=CharacterEventType.FRIEND, char_list=[Character.RYOMA_HOSHI, Character.YASUHIRO_HAGAKURE, Character.MONACA_TOWA])
    SAKURA_AND_AKANE = _CharacterEventData(event_name="Sakura & Akane", event_type=CharacterEventType.FRIEND, char_list=[Character.SAKURA_OGAMI, Character.AKANE_OWARI])
    SAKURA_AND_CELESTIA = _CharacterEventData(event_name="Sakura & Celestia", event_type=CharacterEventType.FRIEND, char_list=[Character.SAKURA_OGAMI, Character.CELESTIA_LUDENBERG])
    SAKURA_AND_GUNDHAM = _CharacterEventData(event_name="Sakura & Gundham", event_type=CharacterEventType.FRIEND, char_list=[Character.SAKURA_OGAMI, Character.GUNDHAM_TANAKA])
    SAKURA_AND_MUKURO_AND_IBUKI = _CharacterEventData(event_name="Sakura & Mukuro & Ibuki", event_type=CharacterEventType.FRIEND, char_list=[Character.SAKURA_OGAMI, Character.MUKURO_IKUSABA, Character.IBUKI_MIODA])
    SAKURA_AND_NEKOMARU = _CharacterEventData(event_name="Sakura & Nekomaru", event_type=CharacterEventType.FRIEND, char_list=[Character.SAKURA_OGAMI, Character.NEKOMARU_NIDAI])
    SAYAKA_AND_HAJIME = _CharacterEventData(event_name="Sayaka & Hajime", event_type=CharacterEventType.FRIEND, char_list=[Character.SAYAKA_MAIZONO, Character.HAJIME_HINATA])
    SAYAKA_AND_KAZUICHI = _CharacterEventData(event_name="Sayaka & Kazuichi", event_type=CharacterEventType.FRIEND, char_list=[Character.SAYAKA_MAIZONO, Character.KAZUICHI_SODA])
    SAYAKA_AND_KOTOKO = _CharacterEventData(event_name="Sayaka & Kotoko", event_type=CharacterEventType.FRIEND, char_list=[Character.SAYAKA_MAIZONO, Character.KOTOKO_UTSUGI])
    SAYAKA_AND_KYOKO_AND_AOI = _CharacterEventData(event_name="Sayaka & Kyoko & Aoi", event_type=CharacterEventType.FRIEND, char_list=[Character.SAKURA_OGAMI, Character.KYOKO_KIRIGIRI, Character.AOI_ASAHINA])
    SAYAKA_AND_PEKO = _CharacterEventData(event_name="Sayaka & Peko", event_type=CharacterEventType.FRIEND, char_list=[Character.SAYAKA_MAIZONO, Character.PEKO_PEKOYAMA])
    SHIROKUMA_AND_KUROKUMA = _CharacterEventData(event_name="Shirokuma & Kurokuma", event_type=CharacterEventType.FRIEND, char_list=[Character.SHIROKUMA, Character.KUROKUMA])
    SHUICHI_AND_IMPOSTER = _CharacterEventData(event_name="Shuichi & The Ultimate Imposter", event_type=CharacterEventType.FRIEND, char_list=[Character.SHUICHI_SAIHARA, Character.THE_ULTIMATE_IMPOSTER])
    SHUICHI_AND_KAEDE_AND_TOKO = _CharacterEventData(event_name="Shuichi & Kaede & Toko", event_type=CharacterEventType.FRIEND, char_list=[Character.SHUICHI_SAIHARA, Character.KAEDE_AKAMATSU, Character.TOKO_FUKAWA])
    SHUICHI_AND_KAITO_AND_MAKI = _CharacterEventData(event_name="Shuichi & Kaito & Maki", event_type=CharacterEventType.FRIEND, char_list=[Character.SHUICHI_SAIHARA, Character.KAITO_MOMOTA, Character.MAKI_HARUKAWA])
    SHUICHI_AND_KIRUMI = _CharacterEventData(event_name="Shuichi & Kirumi", event_type=CharacterEventType.FRIEND, char_list=[Character.SHUICHI_SAIHARA, Character.KIRUMI_TOJO])
    SHUICHI_AND_KIYOTAKA = _CharacterEventData(event_name="Shuichi & Kiyotaka", event_type=CharacterEventType.FRIEND, char_list=[Character.SHUICHI_SAIHARA, Character.KIYOTAKA_ISHIMARU])
    SHUICHI_AND_KOKICHI_AND_K1_B0 = _CharacterEventData(event_name="Shuichi & Kokichi & K1-B0", event_type=CharacterEventType.FRIEND, char_list=[Character.SHUICHI_SAIHARA, Character.KOKICHI_OMA, Character.K1_B0])
    SHUICHI_AND_KOMARU = _CharacterEventData(event_name="Shuichi & Komaru", event_type=CharacterEventType.FRIEND, char_list=[Character.SHUICHI_SAIHARA, Character.KOMARU_NAEGI])
    SHUICHI_AND_KOREKIYO = _CharacterEventData(event_name="Shuichi & Korekiyo", event_type=CharacterEventType.FRIEND, char_list=[Character.SHUICHI_SAIHARA, Character.KOREKIYO_SHINGUJI])
    SHUICHI_AND_KYOKO_AND_MAKOTO = _CharacterEventData(event_name="Shuichi & Kyoko & Makoto", event_type=CharacterEventType.FRIEND, char_list=[Character.SHUICHI_SAIHARA, Character.KYOKO_KIRIGIRI, Character.MAKOTO_NAEGI])
    SHUICHI_AND_NAGITO_AND_MAHIRU = _CharacterEventData(event_name="Shuichi & Nagito & Mahiru", event_type=CharacterEventType.FRIEND, char_list=[Character.SHUICHI_SAIHARA, Character.NAGITO_KOMAEDA, Character.MAHIRU_KOIZUMI])
    TENKO_AND_AOI = _CharacterEventData(event_name="Tenko & Aoi", event_type=CharacterEventType.FRIEND, char_list=[Character.TENKO_CHABASHIRA, Character.AOI_ASAHINA])
    TENKO_AND_HIROKO = _CharacterEventData(event_name="Tenko & Hiroko", event_type=CharacterEventType.FRIEND, char_list=[Character.TENKO_CHABASHIRA, Character.HIROKO_HAGAKURE])
    TENKO_AND_IBUKI = _CharacterEventData(event_name="Tenko & Ibuki", event_type=CharacterEventType.FRIEND, char_list=[Character.TENKO_CHABASHIRA, Character.IBUKI_MIODA])
    TENKO_AND_MUKURO_AND_AKANE = _CharacterEventData(event_name="Tenko & Mukuro & Akane", event_type=CharacterEventType.FRIEND, char_list=[Character.TENKO_CHABASHIRA, Character.MUKURO_IKUSABA, Character.AKANE_OWARI])
    TENKO_AND_MAKOTO_AND_IMPOSTER = _CharacterEventData(event_name="Tenko & Makoto & The Ultimate Imposter", event_type=CharacterEventType.FRIEND, char_list=[Character.TENKO_CHABASHIRA, Character.MAKOTO_NAEGI, Character.THE_ULTIMATE_IMPOSTER])
    TENKO_AND_MASARU = _CharacterEventData(event_name="Tenko & Masaru", event_type=CharacterEventType.FRIEND, char_list=[Character.TENKO_CHABASHIRA, Character.MASARU_DAIMON])
    TENKO_AND_MONDO_AND_CHIHIRO = _CharacterEventData(event_name="Tenko & Mondo & Chihiro", event_type=CharacterEventType.FRIEND, char_list=[Character.TENKO_CHABASHIRA, Character.MONDO_OWADA, Character.CHIHIRO_FUJISAKI])
    TENKO_AND_NEKOMARU = _CharacterEventData(event_name="Tenko & Nekomaru", event_type=CharacterEventType.FRIEND, char_list=[Character.TENKO_CHABASHIRA, Character.NEKOMARU_NIDAI])
    TERUTERU_AND_HIROKO = _CharacterEventData(event_name="Teruteru & Hiroko", event_type=CharacterEventType.FRIEND, char_list=[Character.TENKO_CHABASHIRA, Character.HIROKO_HAGAKURE])
    TERUTERU_AND_KOTOKO = _CharacterEventData(event_name="Teruteru & Kotoko", event_type=CharacterEventType.FRIEND, char_list=[Character.TENKO_CHABASHIRA, Character.KOTOKO_UTSUGI])
    TERUTERU_AND_NEKOMARU = _CharacterEventData(event_name="Teruteru & Nekomaru", event_type=CharacterEventType.FRIEND, char_list=[Character.TERUTERU_HANAMURA, Character.NEKOMARU_NIDAI])
    TOKO_AND_HIYOKO = _CharacterEventData(event_name="Toko & Hiyoko", event_type=CharacterEventType.FRIEND, char_list=[Character.TOKO_FUKAWA, Character.HIYOKO_SAIONJI])
    TOKO_AND_MUKURO_AND_MIKAN = _CharacterEventData(event_name="Toko & Mukuro & Mikan", event_type=CharacterEventType.FRIEND, char_list=[Character.TOKO_FUKAWA, Character.MUKURO_IKUSABA, Character.MIKAN_TSUMIKI])
    TOKO_AND_KOMARU = _CharacterEventData(event_name="Toko & Komaru", event_type=CharacterEventType.FRIEND, char_list=[Character.TOKO_FUKAWA, Character.KOMARU_NAEGI])
    TOKO_AND_MONACA = _CharacterEventData(event_name="Toko & Monaca", event_type=CharacterEventType.FRIEND, char_list=[Character.TOKO_FUKAWA, Character.MONACA_TOWA])
    TOKO_AND_NAGITO = _CharacterEventData(event_name="Toko & Nagito", event_type=CharacterEventType.FRIEND, char_list=[Character.TOKO_FUKAWA, Character.NAGITO_KOMAEDA])
    TSUMUGI_AND_AOI_AND_AKANE = _CharacterEventData(event_name="Tsumugi & Aoi & Akane", event_type=CharacterEventType.FRIEND, char_list=[Character.TSUMUGI_SHIROGANE, Character.AOI_ASAHINA, Character.AKANE_OWARI])
    TSUMUGI_AND_IMPOSTER = _CharacterEventData(event_name="Tsumugi & The Ultimate Imposter", event_type=CharacterEventType.FRIEND, char_list=[Character.TSUMUGI_SHIROGANE, Character.THE_ULTIMATE_IMPOSTER])
    TSUMUGI_AND_JACK_AND_GUNDHAM = _CharacterEventData(event_name="Tsumugi & Genocide Jack & Gundham", event_type=CharacterEventType.FRIEND, char_list=[Character.TSUMUGI_SHIROGANE, Character.GENOCIDE_JACK, Character.GUNDHAM_TANAKA])
    TSUMUGI_AND_HIFUMI_AND_MAHIRU = _CharacterEventData(event_name="Tsumugi & Hifumi & Mahiru", event_type=CharacterEventType.FRIEND, char_list=[Character.TSUMUGI_SHIROGANE, Character.HIFUMI_YAMADA, Character.MAHIRU_KOIZUMI])
    TSUMUGI_AND_KIYOTAKA_AND_YASUHIRO = _CharacterEventData(event_name="Tsumugi & Kiyotaka & Yasuhiro", event_type=CharacterEventType.FRIEND, char_list=[Character.TSUMUGI_SHIROGANE, Character.KIYOTAKA_ISHIMARU, Character.YASUHIRO_HAGAKURE])
    TSUMUGI_AND_KOTOKO = _CharacterEventData(event_name="Tsumugi & Kotoko", event_type=CharacterEventType.FRIEND, char_list=[Character.TSUMUGI_SHIROGANE, Character.KOTOKO_UTSUGI])
    TSUMUGI_AND_KYOKO = _CharacterEventData(event_name="Tsumugi & Kyoko", event_type=CharacterEventType.FRIEND, char_list=[Character.TSUMUGI_SHIROGANE, Character.KYOKO_KIRIGIRI])
    TSUMUGI_AND_MAKOTO = _CharacterEventData(event_name="Tsumugi & Makoto", event_type=CharacterEventType.FRIEND, char_list=[Character.TSUMUGI_SHIROGANE, Character.MAKOTO_NAEGI])
    TSUMUGI_AND_MONOMI = _CharacterEventData(event_name="Tsumugi & Monomi", event_type=CharacterEventType.FRIEND, char_list=[Character.TSUMUGI_SHIROGANE, Character.MONOMI])
    USAMI_AND_ANGIE_AND_JATARO = _CharacterEventData(event_name="Usami & Angie & Jataro", event_type=CharacterEventType.FRIEND, char_list=[Character.USAMI, Character.ANGIE_YONAGA, Character.JATARO_KEMURI])
    USAMI_AND_JACK_AND_TERUTERU = _CharacterEventData(event_name="Usami & Genocide Jack & Teruteru", event_type=CharacterEventType.FRIEND, char_list=[Character.USAMI, Character.GENOCIDE_JACK, Character.TERUTERU_HANAMURA])
    USAMI_AND_IBUKI = _CharacterEventData(event_name="Usami & Ibuki", event_type=CharacterEventType.FRIEND, char_list=[Character.USAMI , Character.IBUKI_MIODA])
    USAMI_AND_KUROKUMA = _CharacterEventData(event_name="Usami & Kurokuma", event_type=CharacterEventType.FRIEND, char_list=[Character.USAMI , Character.KUROKUMA])
    USAMI_AND_MAKI = _CharacterEventData(event_name="Usami & Maki", event_type=CharacterEventType.FRIEND, char_list=[Character.USAMI , Character.MAKI_HARUKAWA])
    USAMI_AND_MIU = _CharacterEventData(event_name="Usami & Miu", event_type=CharacterEventType.FRIEND, char_list=[Character.USAMI , Character.MIU_IRUMA])
    USAMI_AND_MIU_AND_KAZUICHI = _CharacterEventData(event_name="Usami & Miu & Kazuichi", event_type=CharacterEventType.FRIEND, char_list=[Character.USAMI, Character.MIU_IRUMA, Character.KAZUICHI_SODA])
    USAMI_AND_MONOKUMA = _CharacterEventData(event_name="Usami & Monokuma", event_type=CharacterEventType.FRIEND, char_list=[Character.USAMI , Character.MONOKUMA])
    USAMI_AND_TSUMUGI = _CharacterEventData(event_name="Usami & Tsumugi", event_type=CharacterEventType.FRIEND, char_list=[Character.USAMI , Character.TSUMUGI_SHIROGANE])
    YASUHIRO_AND_AOI = _CharacterEventData(event_name="Yasuhiro & Aoi", event_type=CharacterEventType.FRIEND, char_list=[Character.YASUHIRO_HAGAKURE , Character.AOI_ASAHINA])
    YASUHIRO_AND_GUNDHAM = _CharacterEventData(event_name="Yasuhiro & Gundham", event_type=CharacterEventType.FRIEND, char_list=[Character.YASUHIRO_HAGAKURE , Character.GUNDHAM_TANAKA])
    YASUHIRO_AND_HIROKO = _CharacterEventData(event_name="Yasuhiro & Hiroko", event_type=CharacterEventType.FRIEND, char_list=[Character.YASUHIRO_HAGAKURE , Character.HIROKO_HAGAKURE])
    YASUHIRO_AND_MUKURO = _CharacterEventData(event_name="Yasuhiro & Mukuro", event_type=CharacterEventType.FRIEND, char_list=[Character.YASUHIRO_HAGAKURE , Character.MUKURO_IKUSABA])
    YASUHIRO_AND_MIKAN = _CharacterEventData(event_name="Yasuhiro & Mikan", event_type=CharacterEventType.FRIEND, char_list=[Character.YASUHIRO_HAGAKURE , Character.MIKAN_TSUMIKI])
    MAKOTO_CAMPFIRE = _CharacterEventData(event_name="Campfire - Makoto", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.MAKOTO_NAEGI])
    AKANE_CAMPFIRE = _CharacterEventData(event_name="Campfire - Akane", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.AKANE_OWARI])
    ANGIE_CAMPFIRE = _CharacterEventData(event_name="Campfire - Angie", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.ANGIE_YONAGA])
    AOI_CAMPFIRE = _CharacterEventData(event_name="Campfire - Aoi", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.AOI_ASAHINA])
    BYAKUYA_CAMPFIRE = _CharacterEventData(event_name="Campfire - Byakuya", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.BYAKUYA_TOGAMI])
    IMPOSTER_CAMPFIRE = _CharacterEventData(event_name="Campfire - The Ultimate Imposter", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.THE_ULTIMATE_IMPOSTER])
    CELESTIA_CAMPFIRE = _CharacterEventData(event_name="Campfire - Celestia", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.CELESTIA_LUDENBERG])
    CHIAKI_CAMPFIRE = _CharacterEventData(event_name="Campfire - Chiaki", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.CHIAKI_NANAMI])
    CHIHIRO_CAMPFIRE = _CharacterEventData(event_name="Campfire - Chihiro", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.CHIHIRO_FUJISAKI])
    FUYUHIKO_CAMPFIRE = _CharacterEventData(event_name="Campfire - Fuyuhiko", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.FUYUHIKO_KUZURYU])
    GONTA_CAMPFIRE = _CharacterEventData(event_name="Campfire - Gonta", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.GONTA_GOKUHARA])
    GUNDHAM_CAMPFIRE = _CharacterEventData(event_name="Campfire - Gundham", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.GUNDHAM_TANAKA])
    HAJIME_CAMPFIRE = _CharacterEventData(event_name="Campfire - Hajime", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.HAJIME_HINATA])
    HIFUMI_CAMPFIRE = _CharacterEventData(event_name="Campfire - Hifumi", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.HIFUMI_YAMADA])
    HIMIKO_CAMPFIRE = _CharacterEventData(event_name="Campfire - Himiko", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.HIMIKO_YUMENO])
    HIROKO_CAMPFIRE = _CharacterEventData(event_name="Campfire - Hiroko", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.HIROKO_HAGAKURE])
    HIYOKO_CAMPFIRE = _CharacterEventData(event_name="Campfire - Hiyoko", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.HIYOKO_SAIONJI])
    IBUKI_CAMPFIRE = _CharacterEventData(event_name="Campfire - Ibuki", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.IBUKI_MIODA])
    IZURU_CAMPFIRE = _CharacterEventData(event_name="Campfire - Izuru", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.IZURU_KAMUKURA])
    JACK_CAMPFIRE = _CharacterEventData(event_name="Campfire - Jack", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.GENOCIDE_JACK])
    JATARO_CAMPFIRE = _CharacterEventData(event_name="Campfire - Jataro", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.JATARO_KEMURI])
    JUNKO_CAMPFIRE = _CharacterEventData(event_name="Campfire - Junko", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.JUNKO_ENOSHIMA])
    MUKURO_CAMPFIRE = _CharacterEventData(event_name="Campfire - Mukuro", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.MUKURO_IKUSABA])
    K1_B0_CAMPFIRE = _CharacterEventData(event_name="Campfire - K1-B0", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.K1_B0])
    KAEDE_CAMPFIRE = _CharacterEventData(event_name="Campfire - Kaede", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.KAEDE_AKAMATSU])
    KAITO_CAMPFIRE = _CharacterEventData(event_name="Campfire - Kaito", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.KAITO_MOMOTA])
    KAZUICHI_CAMPFIRE = _CharacterEventData(event_name="Campfire - Kazuichi", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.KAZUICHI_SODA])
    KIRUMI_CAMPFIRE = _CharacterEventData(event_name="Campfire - Kirumi", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.KIRUMI_TOJO])
    KIYOTAKA_CAMPFIRE = _CharacterEventData(event_name="Campfire - Kiyotaka", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.KIYOTAKA_ISHIMARU])
    KOKICHI_CAMPFIRE = _CharacterEventData(event_name="Campfire - Kokichi", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.KOKICHI_OMA])
    KOMARU_CAMPFIRE = _CharacterEventData(event_name="Campfire - Komaru", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.KOMARU_NAEGI])
    KOREKIYO_CAMPFIRE = _CharacterEventData(event_name="Campfire - Korekiyo", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.KOREKIYO_SHINGUJI])
    KOTOKO_CAMPFIRE = _CharacterEventData(event_name="Campfire - Kotoko", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.KOTOKO_UTSUGI])
    KUROKUMA_CAMPFIRE = _CharacterEventData(event_name="Campfire - Kurokuma", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.KUROKUMA])
    KYOKO_CAMPFIRE = _CharacterEventData(event_name="Campfire - Kyoko", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.KYOKO_KIRIGIRI])
    LEON_CAMPFIRE = _CharacterEventData(event_name="Campfire - Leon", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.LEON_KUWATA])
    MAHIRU_CAMPFIRE = _CharacterEventData(event_name="Campfire - Mahiru", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.MAHIRU_KOIZUMI])
    MAKI_CAMPFIRE = _CharacterEventData(event_name="Campfire - Maki", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.MAKI_HARUKAWA])
    MASARU_CAMPFIRE = _CharacterEventData(event_name="Campfire - Masaru", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.MASARU_DAIMON])
    MIKAN_CAMPFIRE = _CharacterEventData(event_name="Campfire - Mikan", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.MIKAN_TSUMIKI])
    MIU_CAMPFIRE = _CharacterEventData(event_name="Campfire - Miu", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.MIU_IRUMA])
    MONACA_CAMPFIRE = _CharacterEventData(event_name="Campfire - Monaca", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.MONACA_TOWA])
    MONDO_CAMPFIRE = _CharacterEventData(event_name="Campfire - Mondo", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.MONDO_OWADA])
    MONOKUMA_CAMPFIRE = _CharacterEventData(event_name="Campfire - Monokuma", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.MONOKUMA])
    MONOMI_CAMPFIRE = _CharacterEventData(event_name="Campfire - Monomi", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.MONOMI])
    NAGISA_CAMPFIRE = _CharacterEventData(event_name="Campfire - Nagisa", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.NAGISA_SHINGETSU])
    NAGITO_CAMPFIRE = _CharacterEventData(event_name="Campfire - Nagito", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.NAGITO_KOMAEDA])
    NEKOMARU_CAMPFIRE = _CharacterEventData(event_name="Campfire - Nekomaru", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.NEKOMARU_NIDAI])
    PEKO_CAMPFIRE = _CharacterEventData(event_name="Campfire - Peko", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.PEKO_PEKOYAMA])
    RANTARO_CAMPFIRE = _CharacterEventData(event_name="Campfire - Rantaro", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.RANTARO_AMAMI])
    RYOMA_CAMPFIRE = _CharacterEventData(event_name="Campfire - Ryoma", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.RYOMA_HOSHI])
    SAKURA_CAMPFIRE = _CharacterEventData(event_name="Campfire - Sakura", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.SAKURA_OGAMI])
    SAYAKA_CAMPFIRE = _CharacterEventData(event_name="Campfire - Sayaka", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.SAYAKA_MAIZONO])
    SHIROKUMA_CAMPFIRE = _CharacterEventData(event_name="Campfire - Shirokuma", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.SHIROKUMA])
    SHUICHI_CAMPFIRE = _CharacterEventData(event_name="Campfire - Shuichi", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.SHUICHI_SAIHARA])
    SONIA_CAMPFIRE = _CharacterEventData(event_name="Campfire - Sonia", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.SONIA_NEVERMIND])
    TENKO_CAMPFIRE = _CharacterEventData(event_name="Campfire - Tenko", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.TENKO_CHABASHIRA])
    TERUTERU_CAMPFIRE = _CharacterEventData(event_name="Campfire - Teruteru", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.TERUTERU_HANAMURA])
    TOKO_CAMPFIRE = _CharacterEventData(event_name="Campfire - Toko", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.TOKO_FUKAWA])
    TSUMUGI_CAMPFIRE = _CharacterEventData(event_name="Campfire - Tsumugi", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.TSUMUGI_SHIROGANE])
    USAMI_CAMPFIRE = _CharacterEventData(event_name="Campfire - Usami", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.USAMI])
    YASUHIRO_CAMPFIRE = _CharacterEventData(event_name="Campfire - Yasuhiro", event_type=CharacterEventType.CAMPFIRE, char_list=[Character.YASUHIRO_HAGAKURE])
    MAKOTO_FUTURE = _CharacterEventData(event_name="My Future... - Makoto", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.MAKOTO_NAEGI])
    AKANE_FUTURE = _CharacterEventData(event_name="My Future... - Akane", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.AKANE_OWARI])
    ANGIE_FUTURE = _CharacterEventData(event_name="My Future... - Angie", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.ANGIE_YONAGA])
    AOI_FUTURE = _CharacterEventData(event_name="My Future... - Aoi", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.AOI_ASAHINA])
    BYAKUYA_FUTURE = _CharacterEventData(event_name="My Future... - Byakuya", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.BYAKUYA_TOGAMI])
    IMPOSTER_FUTURE = _CharacterEventData(event_name="My Future... - The Ultimate Imposter", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.THE_ULTIMATE_IMPOSTER])
    CELESTIA_FUTURE = _CharacterEventData(event_name="My Future... - Celestia", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.CELESTIA_LUDENBERG])
    CHIAKI_FUTURE = _CharacterEventData(event_name="My Future... - Chiaki", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.CHIAKI_NANAMI])
    CHIHIRO_FUTURE = _CharacterEventData(event_name="My Future... - Chihiro", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.CHIHIRO_FUJISAKI])
    FUYUHIKO_FUTURE = _CharacterEventData(event_name="My Future... - Fuyuhiko", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.FUYUHIKO_KUZURYU])
    GONTA_FUTURE = _CharacterEventData(event_name="My Future... - Gonta", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.GONTA_GOKUHARA])
    GUNDHAM_FUTURE = _CharacterEventData(event_name="My Future... - Gundham", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.GUNDHAM_TANAKA])
    HAJIME_FUTURE = _CharacterEventData(event_name="My Future... - Hajime", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.HAJIME_HINATA])
    HIFUMI_FUTURE = _CharacterEventData(event_name="My Future... - Hifumi", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.HIFUMI_YAMADA])
    HIMIKO_FUTURE = _CharacterEventData(event_name="My Future... - Himiko", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.HIMIKO_YUMENO])
    HIROKO_FUTURE = _CharacterEventData(event_name="My Future... - Hiroko", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.HIROKO_HAGAKURE])
    HIYOKO_FUTURE = _CharacterEventData(event_name="My Future... - Hiyoko", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.HIYOKO_SAIONJI])
    IBUKI_FUTURE = _CharacterEventData(event_name="My Future... - Ibuki", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.IBUKI_MIODA])
    IZURU_FUTURE = _CharacterEventData(event_name="My Future... - Izuru", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.IZURU_KAMUKURA])
    JACK_FUTURE = _CharacterEventData(event_name="My Future... - Jack", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.GENOCIDE_JACK])
    JATARO_FUTURE = _CharacterEventData(event_name="My Future... - Jataro", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.JATARO_KEMURI])
    JUNKO_FUTURE = _CharacterEventData(event_name="My Future... - Junko", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.JUNKO_ENOSHIMA])
    MUKURO_FUTURE = _CharacterEventData(event_name="My Future... - Mukuro", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.MUKURO_IKUSABA])
    K1_B0_FUTURE = _CharacterEventData(event_name="My Future... - K1-B0", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.K1_B0])
    KAEDE_FUTURE = _CharacterEventData(event_name="My Future... - Kaede", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.KAEDE_AKAMATSU])
    KAITO_FUTURE = _CharacterEventData(event_name="My Future... - Kaito", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.KAITO_MOMOTA])
    KAZUICHI_FUTURE = _CharacterEventData(event_name="My Future... - Kazuichi", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.KAZUICHI_SODA])
    KIRUMI_FUTURE = _CharacterEventData(event_name="My Future... - Kirumi", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.KIRUMI_TOJO])
    KIYOTAKA_FUTURE = _CharacterEventData(event_name="My Future... - Kiyotaka", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.KIYOTAKA_ISHIMARU])
    KOKICHI_FUTURE = _CharacterEventData(event_name="My Future... - Kokichi", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.KOKICHI_OMA])
    KOMARU_FUTURE = _CharacterEventData(event_name="My Future... - Komaru", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.KOMARU_NAEGI])
    KOREKIYO_FUTURE = _CharacterEventData(event_name="My Future... - Korekiyo", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.KOREKIYO_SHINGUJI])
    KOTOKO_FUTURE = _CharacterEventData(event_name="My Future... - Kotoko", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.KOTOKO_UTSUGI])
    KUROKUMA_FUTURE = _CharacterEventData(event_name="My Future... - Kurokuma", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.KUROKUMA])
    KYOKO_FUTURE = _CharacterEventData(event_name="My Future... - Kyoko", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.KYOKO_KIRIGIRI])
    LEON_FUTURE = _CharacterEventData(event_name="My Future... - Leon", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.LEON_KUWATA])
    MAHIRU_FUTURE = _CharacterEventData(event_name="My Future... - Mahiru", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.MAHIRU_KOIZUMI])
    MAKI_FUTURE = _CharacterEventData(event_name="My Future... - Maki", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.MAKI_HARUKAWA])
    MASARU_FUTURE = _CharacterEventData(event_name="My Future... - Masaru", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.MASARU_DAIMON])
    MIKAN_FUTURE = _CharacterEventData(event_name="My Future... - Mikan", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.MIKAN_TSUMIKI])
    MIU_FUTURE = _CharacterEventData(event_name="My Future... - Miu", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.MIU_IRUMA])
    MONACA_FUTURE = _CharacterEventData(event_name="My Future... - Monaca", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.MONACA_TOWA])
    MONDO_FUTURE = _CharacterEventData(event_name="My Future... - Mondo", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.MONDO_OWADA])
    MONOKUMA_FUTURE = _CharacterEventData(event_name="My Future... - Monokuma", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.MONOKUMA])
    MONOMI_FUTURE = _CharacterEventData(event_name="My Future... - Monomi", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.MONOMI])
    NAGISA_FUTURE = _CharacterEventData(event_name="My Future... - Nagisa", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.NAGISA_SHINGETSU])
    NAGITO_FUTURE = _CharacterEventData(event_name="My Future... - Nagito", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.NAGITO_KOMAEDA])
    NEKOMARU_FUTURE = _CharacterEventData(event_name="My Future... - Nekomaru", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.NEKOMARU_NIDAI])
    PEKO_FUTURE = _CharacterEventData(event_name="My Future... - Peko", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.PEKO_PEKOYAMA])
    RANTARO_FUTURE = _CharacterEventData(event_name="My Future... - Rantaro", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.RANTARO_AMAMI])
    RYOMA_FUTURE = _CharacterEventData(event_name="My Future... - Ryoma", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.RYOMA_HOSHI])
    SAKURA_FUTURE = _CharacterEventData(event_name="My Future... - Sakura", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.SAKURA_OGAMI])
    SAYAKA_FUTURE = _CharacterEventData(event_name="My Future... - Sayaka", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.SAYAKA_MAIZONO])
    SHIROKUMA_FUTURE = _CharacterEventData(event_name="My Future... - Shirokuma", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.SHIROKUMA])
    SHUICHI_FUTURE = _CharacterEventData(event_name="My Future... - Shuichi", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.SHUICHI_SAIHARA])
    SONIA_FUTURE = _CharacterEventData(event_name="My Future... - Sonia", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.SONIA_NEVERMIND])
    TENKO_FUTURE = _CharacterEventData(event_name="My Future... - Tenko", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.TENKO_CHABASHIRA])
    TERUTERU_FUTURE = _CharacterEventData(event_name="My Future... - Teruteru", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.TERUTERU_HANAMURA])
    TOKO_FUTURE = _CharacterEventData(event_name="My Future... - Toko", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.TOKO_FUKAWA])
    TSUMUGI_FUTURE = _CharacterEventData(event_name="My Future... - Tsumugi", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.TSUMUGI_SHIROGANE])
    USAMI_FUTURE = _CharacterEventData(event_name="My Future... - Usami", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.USAMI])
    YASUHIRO_FUTURE = _CharacterEventData(event_name="My Future... - Yasuhiro", event_type=CharacterEventType.MY_FUTURE, char_list=[Character.YASUHIRO_HAGAKURE])
    MAKOTO_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Makoto", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.MAKOTO_NAEGI])
    AKANE_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Akane", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.AKANE_OWARI])
    ANGIE_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Angie", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.ANGIE_YONAGA])
    AOI_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Aoi", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.AOI_ASAHINA])
    BYAKUYA_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Byakuya", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.BYAKUYA_TOGAMI])
    IMPOSTER_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - The Ultimate Imposter", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.THE_ULTIMATE_IMPOSTER])
    CELESTIA_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Celestia", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.CELESTIA_LUDENBERG])
    CHIAKI_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Chiaki", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.CHIAKI_NANAMI])
    CHIHIRO_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Chihiro", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.CHIHIRO_FUJISAKI])
    FUYUHIKO_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Fuyuhiko", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.FUYUHIKO_KUZURYU])
    GONTA_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Gonta", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.GONTA_GOKUHARA])
    GUNDHAM_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Gundham", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.GUNDHAM_TANAKA])
    HAJIME_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Hajime", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.HAJIME_HINATA])
    HIFUMI_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Hifumi", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.HIFUMI_YAMADA])
    HIMIKO_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Himiko", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.HIMIKO_YUMENO])
    HIROKO_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Hiroko", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.HIROKO_HAGAKURE])
    HIYOKO_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Hiyoko", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.HIYOKO_SAIONJI])
    IBUKI_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Ibuki", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.IBUKI_MIODA])
    IZURU_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Izuru", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.IZURU_KAMUKURA])
    JACK_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Jack", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.GENOCIDE_JACK])
    JATARO_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Jataro", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.JATARO_KEMURI])
    JUNKO_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Junko", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.JUNKO_ENOSHIMA])
    MUKURO_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Mukuro", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.MUKURO_IKUSABA])
    K1_B0_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - K1-B0", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.K1_B0])
    KAEDE_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Kaede", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.KAEDE_AKAMATSU])
    KAITO_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Kaito", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.KAITO_MOMOTA])
    KAZUICHI_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Kazuichi", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.KAZUICHI_SODA])
    KIRUMI_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Kirumi", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.KIRUMI_TOJO])
    KIYOTAKA_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Kiyotaka", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.KIYOTAKA_ISHIMARU])
    KOKICHI_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Kokichi", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.KOKICHI_OMA])
    KOMARU_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Komaru", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.KOMARU_NAEGI])
    KOREKIYO_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Korekiyo", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.KOREKIYO_SHINGUJI])
    KOTOKO_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Kotoko", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.KOTOKO_UTSUGI])
    KUROKUMA_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Kurokuma", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.KUROKUMA])
    KYOKO_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Kyoko", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.KYOKO_KIRIGIRI])
    LEON_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Leon", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.LEON_KUWATA])
    MAHIRU_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Mahiru", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.MAHIRU_KOIZUMI])
    MAKI_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Maki", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.MAKI_HARUKAWA])
    MASARU_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Masaru", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.MASARU_DAIMON])
    MIKAN_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Mikan", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.MIKAN_TSUMIKI])
    MIU_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Miu", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.MIU_IRUMA])
    MONACA_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Monaca", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.MONACA_TOWA])
    MONDO_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Mondo", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.MONDO_OWADA])
    MONOKUMA_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Monokuma", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.MONOKUMA])
    MONOMI_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Monomi", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.MONOMI])
    NAGISA_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Nagisa", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.NAGISA_SHINGETSU])
    NAGITO_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Nagito", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.NAGITO_KOMAEDA])
    NEKOMARU_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Nekomaru", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.NEKOMARU_NIDAI])
    PEKO_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Peko", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.PEKO_PEKOYAMA])
    RANTARO_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Rantaro", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.RANTARO_AMAMI])
    RYOMA_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Ryoma", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.RYOMA_HOSHI])
    SAKURA_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Sakura", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.SAKURA_OGAMI])
    SAYAKA_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Sayaka", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.SAYAKA_MAIZONO])
    SHIROKUMA_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Shirokuma", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.SHIROKUMA])
    SHUICHI_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Shuichi", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.SHUICHI_SAIHARA])
    SONIA_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Sonia", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.SONIA_NEVERMIND])
    TENKO_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Tenko", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.TENKO_CHABASHIRA])
    TERUTERU_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Teruteru", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.TERUTERU_HANAMURA])
    TOKO_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Toko", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.TOKO_FUKAWA])
    TSUMUGI_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Tsumugi", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.TSUMUGI_SHIROGANE])
    USAMI_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Usami", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.USAMI])
    YASUHIRO_POTENTIAL = _CharacterEventData(event_name="Potential of Talent - Yasuhiro", event_type=CharacterEventType.POTENTIAL_TALENT, char_list=[Character.YASUHIRO_HAGAKURE])
    MAKOTO_SUMMER = _CharacterEventData(event_name="Summer Festival - Makoto", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.MAKOTO_NAEGI])
    AKANE_SUMMER = _CharacterEventData(event_name="Summer Festival - Akane", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.AKANE_OWARI])
    ANGIE_SUMMER = _CharacterEventData(event_name="Summer Festival - Angie", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.ANGIE_YONAGA])
    AOI_SUMMER = _CharacterEventData(event_name="Summer Festival - Aoi", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.AOI_ASAHINA])
    BYAKUYA_SUMMER = _CharacterEventData(event_name="Summer Festival - Byakuya", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.BYAKUYA_TOGAMI])
    IMPOSTER_SUMMER = _CharacterEventData(event_name="Summer Festival - The Ultimate Imposter", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.THE_ULTIMATE_IMPOSTER])
    CELESTIA_SUMMER = _CharacterEventData(event_name="Summer Festival - Celestia", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.CELESTIA_LUDENBERG])
    CHIAKI_SUMMER = _CharacterEventData(event_name="Summer Festival - Chiaki", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.CHIAKI_NANAMI])
    CHIHIRO_SUMMER = _CharacterEventData(event_name="Summer Festival - Chihiro", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.CHIHIRO_FUJISAKI])
    FUYUHIKO_SUMMER = _CharacterEventData(event_name="Summer Festival - Fuyuhiko", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.FUYUHIKO_KUZURYU])
    GONTA_SUMMER = _CharacterEventData(event_name="Summer Festival - Gonta", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.GONTA_GOKUHARA])
    GUNDHAM_SUMMER = _CharacterEventData(event_name="Summer Festival - Gundham", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.GUNDHAM_TANAKA])
    HAJIME_SUMMER = _CharacterEventData(event_name="Summer Festival - Hajime", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.HAJIME_HINATA])
    HIFUMI_SUMMER = _CharacterEventData(event_name="Summer Festival - Hifumi", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.HIFUMI_YAMADA])
    HIMIKO_SUMMER = _CharacterEventData(event_name="Summer Festival - Himiko", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.HIMIKO_YUMENO])
    HIROKO_SUMMER = _CharacterEventData(event_name="Summer Festival - Hiroko", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.HIROKO_HAGAKURE])
    HIYOKO_SUMMER = _CharacterEventData(event_name="Summer Festival - Hiyoko", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.HIYOKO_SAIONJI])
    IBUKI_SUMMER = _CharacterEventData(event_name="Summer Festival - Ibuki", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.IBUKI_MIODA])
    IZURU_SUMMER = _CharacterEventData(event_name="Summer Festival - Izuru", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.IZURU_KAMUKURA])
    JACK_SUMMER = _CharacterEventData(event_name="Summer Festival - Jack", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.GENOCIDE_JACK])
    JATARO_SUMMER = _CharacterEventData(event_name="Summer Festival - Jataro", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.JATARO_KEMURI])
    JUNKO_SUMMER = _CharacterEventData(event_name="Summer Festival - Junko", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.JUNKO_ENOSHIMA])
    MUKURO_SUMMER = _CharacterEventData(event_name="Summer Festival - Mukuro", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.MUKURO_IKUSABA])
    K1_B0_SUMMER = _CharacterEventData(event_name="Summer Festival - K1-B0", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.K1_B0])
    KAEDE_SUMMER = _CharacterEventData(event_name="Summer Festival - Kaede", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.KAEDE_AKAMATSU])
    KAITO_SUMMER = _CharacterEventData(event_name="Summer Festival - Kaito", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.KAITO_MOMOTA])
    KAZUICHI_SUMMER = _CharacterEventData(event_name="Summer Festival - Kazuichi", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.KAZUICHI_SODA])
    KIRUMI_SUMMER = _CharacterEventData(event_name="Summer Festival - Kirumi", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.KIRUMI_TOJO])
    KIYOTAKA_SUMMER = _CharacterEventData(event_name="Summer Festival - Kiyotaka", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.KIYOTAKA_ISHIMARU])
    KOKICHI_SUMMER = _CharacterEventData(event_name="Summer Festival - Kokichi", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.KOKICHI_OMA])
    KOMARU_SUMMER = _CharacterEventData(event_name="Summer Festival - Komaru", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.KOMARU_NAEGI])
    KOREKIYO_SUMMER = _CharacterEventData(event_name="Summer Festival - Korekiyo", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.KOREKIYO_SHINGUJI])
    KOTOKO_SUMMER = _CharacterEventData(event_name="Summer Festival - Kotoko", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.KOTOKO_UTSUGI])
    KUROKUMA_SUMMER = _CharacterEventData(event_name="Summer Festival - Kurokuma", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.KUROKUMA])
    KYOKO_SUMMER = _CharacterEventData(event_name="Summer Festival - Kyoko", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.KYOKO_KIRIGIRI])
    LEON_SUMMER = _CharacterEventData(event_name="Summer Festival - Leon", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.LEON_KUWATA])
    MAHIRU_SUMMER = _CharacterEventData(event_name="Summer Festival - Mahiru", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.MAHIRU_KOIZUMI])
    MAKI_SUMMER = _CharacterEventData(event_name="Summer Festival - Maki", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.MAKI_HARUKAWA])
    MASARU_SUMMER = _CharacterEventData(event_name="Summer Festival - Masaru", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.MASARU_DAIMON])
    MIKAN_SUMMER = _CharacterEventData(event_name="Summer Festival - Mikan", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.MIKAN_TSUMIKI])
    MIU_SUMMER = _CharacterEventData(event_name="Summer Festival - Miu", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.MIU_IRUMA])
    MONACA_SUMMER = _CharacterEventData(event_name="Summer Festival - Monaca", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.MONACA_TOWA])
    MONDO_SUMMER = _CharacterEventData(event_name="Summer Festival - Mondo", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.MONDO_OWADA])
    MONOKUMA_SUMMER = _CharacterEventData(event_name="Summer Festival - Monokuma", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.MONOKUMA])
    MONOMI_SUMMER = _CharacterEventData(event_name="Summer Festival - Monomi", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.MONOMI])
    NAGISA_SUMMER = _CharacterEventData(event_name="Summer Festival - Nagisa", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.NAGISA_SHINGETSU])
    NAGITO_SUMMER = _CharacterEventData(event_name="Summer Festival - Nagito", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.NAGITO_KOMAEDA])
    NEKOMARU_SUMMER = _CharacterEventData(event_name="Summer Festival - Nekomaru", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.NEKOMARU_NIDAI])
    PEKO_SUMMER = _CharacterEventData(event_name="Summer Festival - Peko", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.PEKO_PEKOYAMA])
    RANTARO_SUMMER = _CharacterEventData(event_name="Summer Festival - Rantaro", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.RANTARO_AMAMI])
    RYOMA_SUMMER = _CharacterEventData(event_name="Summer Festival - Ryoma", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.RYOMA_HOSHI])
    SAKURA_SUMMER = _CharacterEventData(event_name="Summer Festival - Sakura", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.SAKURA_OGAMI])
    SAYAKA_SUMMER = _CharacterEventData(event_name="Summer Festival - Sayaka", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.SAYAKA_MAIZONO])
    SHIROKUMA_SUMMER = _CharacterEventData(event_name="Summer Festival - Shirokuma", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.SHIROKUMA])
    SHUICHI_SUMMER = _CharacterEventData(event_name="Summer Festival - Shuichi", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.SHUICHI_SAIHARA])
    SONIA_SUMMER = _CharacterEventData(event_name="Summer Festival - Sonia", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.SONIA_NEVERMIND])
    TENKO_SUMMER = _CharacterEventData(event_name="Summer Festival - Tenko", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.TENKO_CHABASHIRA])
    TERUTERU_SUMMER = _CharacterEventData(event_name="Summer Festival - Teruteru", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.TERUTERU_HANAMURA])
    TOKO_SUMMER = _CharacterEventData(event_name="Summer Festival - Toko", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.TOKO_FUKAWA])
    TSUMUGI_SUMMER = _CharacterEventData(event_name="Summer Festival - Tsumugi", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.TSUMUGI_SHIROGANE])
    USAMI_SUMMER = _CharacterEventData(event_name="Summer Festival - Usami", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.USAMI])
    YASUHIRO_SUMMER = _CharacterEventData(event_name="Summer Festival - Yasuhiro", event_type=CharacterEventType.SUMMER_FESTIVAL, char_list=[Character.YASUHIRO_HAGAKURE])
    MAKOTO_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Makoto", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.MAKOTO_NAEGI])
    AKANE_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Akane", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.AKANE_OWARI])
    ANGIE_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Angie", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.ANGIE_YONAGA])
    AOI_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Aoi", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.AOI_ASAHINA])
    BYAKUYA_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Byakuya", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.BYAKUYA_TOGAMI])
    IMPOSTER_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - The Ultimate Imposter", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.THE_ULTIMATE_IMPOSTER])
    CELESTIA_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Celestia", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.CELESTIA_LUDENBERG])
    CHIAKI_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Chiaki", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.CHIAKI_NANAMI])
    CHIHIRO_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Chihiro", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.CHIHIRO_FUJISAKI])
    FUYUHIKO_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Fuyuhiko", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.FUYUHIKO_KUZURYU])
    GONTA_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Gonta", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.GONTA_GOKUHARA])
    GUNDHAM_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Gundham", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.GUNDHAM_TANAKA])
    HAJIME_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Hajime", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.HAJIME_HINATA])
    HIFUMI_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Hifumi", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.HIFUMI_YAMADA])
    HIMIKO_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Himiko", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.HIMIKO_YUMENO])
    HIROKO_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Hiroko", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.HIROKO_HAGAKURE])
    HIYOKO_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Hiyoko", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.HIYOKO_SAIONJI])
    IBUKI_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Ibuki", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.IBUKI_MIODA])
    IZURU_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Izuru", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.IZURU_KAMUKURA])
    JACK_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Jack", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.GENOCIDE_JACK])
    JATARO_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Jataro", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.JATARO_KEMURI])
    JUNKO_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Junko", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.JUNKO_ENOSHIMA])
    MUKURO_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Mukuro", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.MUKURO_IKUSABA])
    K1_B0_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - K1-B0", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.K1_B0])
    KAEDE_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Kaede", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.KAEDE_AKAMATSU])
    KAITO_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Kaito", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.KAITO_MOMOTA])
    KAZUICHI_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Kazuichi", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.KAZUICHI_SODA])
    KIRUMI_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Kirumi", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.KIRUMI_TOJO])
    KIYOTAKA_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Kiyotaka", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.KIYOTAKA_ISHIMARU])
    KOKICHI_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Kokichi", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.KOKICHI_OMA])
    KOMARU_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Komaru", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.KOMARU_NAEGI])
    KOREKIYO_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Korekiyo", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.KOREKIYO_SHINGUJI])
    KOTOKO_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Kotoko", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.KOTOKO_UTSUGI])
    KUROKUMA_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Kurokuma", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.KUROKUMA])
    KYOKO_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Kyoko", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.KYOKO_KIRIGIRI])
    LEON_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Leon", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.LEON_KUWATA])
    MAHIRU_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Mahiru", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.MAHIRU_KOIZUMI])
    MAKI_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Maki", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.MAKI_HARUKAWA])
    MASARU_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Masaru", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.MASARU_DAIMON])
    MIKAN_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Mikan", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.MIKAN_TSUMIKI])
    MIU_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Miu", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.MIU_IRUMA])
    MONACA_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Monaca", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.MONACA_TOWA])
    MONDO_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Mondo", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.MONDO_OWADA])
    MONOKUMA_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Monokuma", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.MONOKUMA])
    MONOMI_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Monomi", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.MONOMI])
    NAGISA_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Nagisa", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.NAGISA_SHINGETSU])
    NAGITO_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Nagito", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.NAGITO_KOMAEDA])
    NEKOMARU_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Nekomaru", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.NEKOMARU_NIDAI])
    PEKO_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Peko", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.PEKO_PEKOYAMA])
    RANTARO_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Rantaro", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.RANTARO_AMAMI])
    RYOMA_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Ryoma", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.RYOMA_HOSHI])
    SAKURA_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Sakura", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.SAKURA_OGAMI])
    SAYAKA_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Sayaka", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.SAYAKA_MAIZONO])
    SHIROKUMA_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Shirokuma", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.SHIROKUMA])
    SHUICHI_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Shuichi", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.SHUICHI_SAIHARA])
    SONIA_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Sonia", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.SONIA_NEVERMIND])
    TENKO_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Tenko", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.TENKO_CHABASHIRA])
    TERUTERU_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Teruteru", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.TERUTERU_HANAMURA])
    TOKO_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Toko", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.TOKO_FUKAWA])
    TSUMUGI_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Tsumugi", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.TSUMUGI_SHIROGANE])
    USAMI_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Usami", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.USAMI])
    YASUHIRO_SWIMSUIT = _CharacterEventData(event_name="With Swimsuits - Yasuhiro", event_type=CharacterEventType.SWIMSUIT, char_list=[Character.YASUHIRO_HAGAKURE])

    def __new__(cls, info: _CharacterEventData) -> Self:
        obj = object.__new__(cls)
        obj._value_ = info
        return obj

    def __init__(self, info: _CharacterEventData) -> None:
        self.event_name: str = info.event_name
        self.event_type: CharacterEventType = info.event_type
        self.char_list: list[Character] = info.char_list


    def get_logically_needed_characters(self) -> list[Character]:
        _result: list[Character] = []

        special_chars: list[Character] = \
        [
            Character.JUNKO_ENOSHIMA,
            Character.USAMI,
            Character.IZURU_KAMUKURA,
        ]

        has_junko_usami_izuru: bool = False
        """Does this event have Junko, Usami, or Izuru"""
        has_other_char: bool = False

        for character in self.char_list:
            if character in special_chars:
                has_junko_usami_izuru = True
            else:
                has_other_char = True
            _result.append(character)

        if has_junko_usami_izuru and has_other_char:
            _result = [character for character in _result if character in special_chars]
        return _result









