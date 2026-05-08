import dataclasses
import enum
from dataclasses import dataclass, field
from typing import NamedTuple


class DanganronpaGame(enum.StrEnum):
    TRIGGER_HAPPY_HAVOC = "Trigger Happy Havoc"
    DANGANRONPA_1 = TRIGGER_HAPPY_HAVOC
    GOODBYE_DESPAIR = "Goodbye Despair"
    DANGANRONPA_2 = GOODBYE_DESPAIR
    ULTRA_DESPAIR_GIRLS = "Ultra Despair Girls"
    UDG = ULTRA_DESPAIR_GIRLS
    KILLING_HARMONY = "Killing Harmony"
    DANGANRONPA_3 = KILLING_HARMONY


class CharacterMainStat(enum.Enum):
    BALANCED = "Balanced"
    ATHLETIC = "Athletic"
    CEREBRAL = "Cerebral"


class Gender(enum.Enum):
    MALE = "Male"
    FEMALE = "Female"


class Character(enum.Enum):
    AKANE_OWARI = ("Akane Owari", [DanganronpaGame.DANGANRONPA_2], CharacterMainStat.ATHLETIC, Gender.FEMALE)
    ANGIE_YONAGA = ("Angie Yonaga", [DanganronpaGame.DANGANRONPA_3], CharacterMainStat.BALANCED, Gender.FEMALE)
    AOI_ASAHINA = ("Aoi Asahina", [DanganronpaGame.DANGANRONPA_1], CharacterMainStat.ATHLETIC, Gender.FEMALE)
    BYAKUYA_TOGAMI = ("Byakuya Togami", [DanganronpaGame.DANGANRONPA_1], CharacterMainStat.CEREBRAL, Gender.MALE)
    CELESTIA_LUDENBERG = ("Celestia Ludenberg", [DanganronpaGame.DANGANRONPA_1], CharacterMainStat.CEREBRAL, Gender.FEMALE)
    CHIAKI_NANAMI = ("Chiaki Nanami", [DanganronpaGame.DANGANRONPA_2], CharacterMainStat.CEREBRAL, Gender.FEMALE)
    CHIHIRO_FUJISAKI = ("Chihiro Fujisaki", [DanganronpaGame.DANGANRONPA_1], CharacterMainStat.CEREBRAL, Gender.MALE)
    FUYUHIKO_KUZURYU = ("Fuyuhiko Kuzuryu", [DanganronpaGame.DANGANRONPA_2], CharacterMainStat.BALANCED, Gender.MALE)
    GENOCIDE_JACK = ("Genocide Jack", [DanganronpaGame.DANGANRONPA_1, DanganronpaGame.ULTRA_DESPAIR_GIRLS], CharacterMainStat.ATHLETIC, Gender.FEMALE)
    GONTA_GOKUHARA = ("Gonta Gokuhara", [DanganronpaGame.DANGANRONPA_3], CharacterMainStat.ATHLETIC, Gender.MALE)
    GUNDHAM_TANAKA = ("Gundham Tanaka", [DanganronpaGame.DANGANRONPA_3], CharacterMainStat.BALANCED, Gender.MALE)
    HAJIME_HINATA = ("Hajime Hinata", [DanganronpaGame.DANGANRONPA_2], CharacterMainStat.ATHLETIC, Gender.MALE)
    HIFUMI_YAMADA = ("Hifumi Yamada", [DanganronpaGame.DANGANRONPA_1], CharacterMainStat.BALANCED, Gender.MALE)
    HIMIKO_YUMENO = ("Himiko Yumeno", [DanganronpaGame.DANGANRONPA_3], CharacterMainStat.BALANCED, Gender.FEMALE)
    HIROKO_HAGAKURE = ("Hiroko Hagakure", [DanganronpaGame.ULTRA_DESPAIR_GIRLS], CharacterMainStat.ATHLETIC, Gender.FEMALE)
    HIYOKO_SAIONJI = ("Hiyoko Saionji", [DanganronpaGame.DANGANRONPA_2], CharacterMainStat.BALANCED, Gender.FEMALE)
    IBUKI_MIODA = ("Ibuki Mioda", [DanganronpaGame.DANGANRONPA_2], CharacterMainStat.BALANCED, Gender.FEMALE)
    IZURU_KAMUKURA = ("Izuru Kamukura", [DanganronpaGame.DANGANRONPA_2], CharacterMainStat.ATHLETIC, Gender.MALE)
    JATARO_KEMURI = ("Jataro Kemuri", [DanganronpaGame.ULTRA_DESPAIR_GIRLS], CharacterMainStat.BALANCED, Gender.MALE)
    JUNKO_ENOSHIMA = ("Junko Enoshima", [DanganronpaGame.DANGANRONPA_1], CharacterMainStat.CEREBRAL, Gender.FEMALE)
    K1_B0 = ("K1-B0", [DanganronpaGame.DANGANRONPA_3], CharacterMainStat.BALANCED, Gender.MALE)
    KAEDE_AKAMATSU = ("Kaede Akamatsu", [DanganronpaGame.DANGANRONPA_3], CharacterMainStat.BALANCED, Gender.FEMALE)
    KAITO_MOMOTA = ("Kaito Momota", [DanganronpaGame.DANGANRONPA_3], CharacterMainStat.ATHLETIC, Gender.MALE)
    KAZUICHI_SODA = ("Kazuichi Soda", [DanganronpaGame.DANGANRONPA_2], CharacterMainStat.CEREBRAL, Gender.MALE)
    KIRUMI_TOJO = ("Kirumi Tojo", [DanganronpaGame.DANGANRONPA_3], CharacterMainStat.CEREBRAL, Gender.FEMALE)
    KIYOTAKA_ISHIMARU = ("Kiyotaka Ishimaru", [DanganronpaGame.DANGANRONPA_1], CharacterMainStat.BALANCED, Gender.MALE)
    KOKICHI_OMA = ("Kokichi Oma", [DanganronpaGame.DANGANRONPA_3], CharacterMainStat.CEREBRAL, Gender.MALE)
    KOMARU_NAEGI = ("Komaru Naegi", [DanganronpaGame.ULTRA_DESPAIR_GIRLS], CharacterMainStat.ATHLETIC, Gender.FEMALE)
    KOREKIYO_SHINGUJI = ("Korekiyo Shinguji", [DanganronpaGame.DANGANRONPA_3], CharacterMainStat.CEREBRAL, Gender.MALE)
    KOTOKO_UTSUGI = ("Kotoko Utsugi", [DanganronpaGame.ULTRA_DESPAIR_GIRLS], CharacterMainStat.BALANCED, Gender.FEMALE)
    KUROKUMA = ("Kurokuma", [DanganronpaGame.ULTRA_DESPAIR_GIRLS], CharacterMainStat.BALANCED, Gender.MALE)
    KYOKO_KIRIGIRI = ("Kyoko Kirigiri", [DanganronpaGame.DANGANRONPA_1], CharacterMainStat.CEREBRAL, Gender.FEMALE)
    LEON_KUWATA = ("Leon Kuwata", [DanganronpaGame.DANGANRONPA_1], CharacterMainStat.ATHLETIC, Gender.MALE)
    MAHIRU_KOIZUMI = ("Mahiru Koizumi", [DanganronpaGame.DANGANRONPA_2], CharacterMainStat.CEREBRAL, Gender.FEMALE)
    MAKI_HARUKAWA = ("Maki Harukawa", [DanganronpaGame.DANGANRONPA_3], CharacterMainStat.ATHLETIC, Gender.FEMALE)
    MAKOTO_NAEGI = ("Makoto Naegi", [DanganronpaGame.DANGANRONPA_1], CharacterMainStat.BALANCED, Gender.MALE)
    MASARU_DAIMON = ("Masaru Daimon", [DanganronpaGame.ULTRA_DESPAIR_GIRLS], CharacterMainStat.ATHLETIC, Gender.MALE)
    MIKAN_TSUMIKI = ("Mikan Tsumiki", [DanganronpaGame.DANGANRONPA_2], CharacterMainStat.BALANCED, Gender.FEMALE)
    MIU_IRUMA = ("Miu Iruma", [DanganronpaGame.DANGANRONPA_3], CharacterMainStat.CEREBRAL, Gender.FEMALE)
    MONACA_TOWA = ("Monaca Towa", [DanganronpaGame.ULTRA_DESPAIR_GIRLS], CharacterMainStat.CEREBRAL, Gender.FEMALE)
    MONDO_OWADA = ("Mondo Owada", [DanganronpaGame.DANGANRONPA_1], CharacterMainStat.ATHLETIC, Gender.MALE)
    MONOKUMA = ("Monokuma", [DanganronpaGame.DANGANRONPA_1], CharacterMainStat.ATHLETIC, Gender.MALE)
    MONOMI = ("Monomi", [DanganronpaGame.DANGANRONPA_2], CharacterMainStat.BALANCED, Gender.FEMALE)
    MUKURO_IKUSABA = ("Mukuro Ikusaba", [DanganronpaGame.DANGANRONPA_1], CharacterMainStat.ATHLETIC, Gender.FEMALE)
    NAGISA_SHINGETSU = ("Nagisa Shingetsu", [DanganronpaGame.ULTRA_DESPAIR_GIRLS], CharacterMainStat.CEREBRAL, Gender.MALE)
    NAGITO_KOMAEDA = ("Nagito Komaeda", [DanganronpaGame.DANGANRONPA_2], CharacterMainStat.BALANCED, Gender.MALE)
    NEKOMARU_NIDAI = ("Nekomaru Nidai", [DanganronpaGame.DANGANRONPA_2], CharacterMainStat.ATHLETIC, Gender.MALE)
    PEKO_PEKOYAMA = ("Peko Pekoyama", [DanganronpaGame.DANGANRONPA_2], CharacterMainStat.ATHLETIC, Gender.FEMALE)
    RANTARO_AMAMI = ("Rantaro Amami", [DanganronpaGame.DANGANRONPA_3], CharacterMainStat.BALANCED, Gender.MALE)
    RYOMA_HOSHI = ("Ryoma Hoshi", [DanganronpaGame.DANGANRONPA_3], CharacterMainStat.ATHLETIC, Gender.MALE)
    SAKURA_OGAMI = ("Sakura Ogami", [DanganronpaGame.DANGANRONPA_1], CharacterMainStat.ATHLETIC, Gender.FEMALE)
    SAYAKA_MAIZONO = ("Sayaka Maizono", [DanganronpaGame.DANGANRONPA_1], CharacterMainStat.BALANCED, Gender.FEMALE)
    SHIROKUMA = ("Shirokuma", [DanganronpaGame.ULTRA_DESPAIR_GIRLS], CharacterMainStat.CEREBRAL, Gender.MALE)
    SHUICHI_SAIHARA = ("Shuichi Saihara", [DanganronpaGame.DANGANRONPA_3], CharacterMainStat.CEREBRAL, Gender.MALE)
    SONIA_NEVERMIND = ("Sonia Nevermind", [DanganronpaGame.DANGANRONPA_2], CharacterMainStat.CEREBRAL, Gender.FEMALE)
    TENKO_CHABASHIRA = ("Tenko Chabashira", [DanganronpaGame.DANGANRONPA_3], CharacterMainStat.ATHLETIC, Gender.FEMALE)
    TERUTERU_HANAMURA = ("Teruteru Hanamura", [DanganronpaGame.DANGANRONPA_2], CharacterMainStat.BALANCED, Gender.MALE)
    THE_ULTIMATE_IMPOSTER = ("The Ultimate Imposter", [DanganronpaGame.DANGANRONPA_2], CharacterMainStat.CEREBRAL, Gender.MALE)
    TOKO_FUKAWA = ("Toko Fukawa", [DanganronpaGame.DANGANRONPA_1, DanganronpaGame.ULTRA_DESPAIR_GIRLS], CharacterMainStat.CEREBRAL, Gender.FEMALE)
    TSUMUGI_SHIROGANE = ("Tsumugi Shirogane", [DanganronpaGame.DANGANRONPA_3], CharacterMainStat.CEREBRAL, Gender.FEMALE)
    USAMI = ("Usami", [DanganronpaGame.DANGANRONPA_2], CharacterMainStat.CEREBRAL, Gender.FEMALE)
    YASUHIRO_HAGAKURE = ("Yasuhiro Hagakure", [DanganronpaGame.DANGANRONPA_1], CharacterMainStat.BALANCED, Gender.MALE)

    def __init__(self, char_name: str, games_list: list[DanganronpaGame], main_stat: CharacterMainStat, gender: Gender) -> None:
        self.char_name: str = char_name
        self.games_list: list[DanganronpaGame] = games_list
        self.main_stat: CharacterMainStat = main_stat
        self.gender: Gender = gender

    @property
    def main_game(self) -> DanganronpaGame:
        return self.games_list[0]


class CharacterRarity(enum.StrEnum):
    NORMAL = "Normal"
    N = NORMAL
    RARE = "Rare"
    R = RARE
    SUPER_RARE = "Super Rare"
    S = SUPER_RARE
    ULTRA_RARE = "Ultra Rare"
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


# TODO finish crafted item data here
class CraftedItem(enum.Enum):
    ARMY_KNIFE = ("Army Knife", "", [crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.GOLD]], -30, 0, 50, -50, 0, 0, 100, 150)
    CROSSBOW = ("Crossbow", "", [crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.GOLD]], 0, 0, 200, -100, -100, 200, 0, 0)
    DUMBBELL = ("Dumbbell", "", [crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.COPPER]], 30, 0, 50, 70, -50, 0, 100, 0)
    GOLD_LEAF_KATANA = ("Gold Leaf Katana", "", [crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.SILVER]], 0, 0, 150, -50, 0, -50, 0, 0)
    HACKING_GUN = ("Hacking Gun", "", [crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.SMALL], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.NORMAL]], 0, 0, 0, 0, 50, 0, 0, 0)
    HACKING_GUN_EXTREME = ("Hacking Gun Extreme", "", [crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.STURDY]], 0, 0, 0, 0, 150, 0, 0, 0)
    HACKING_GUN_V3 = ("Hacking Gun V3", "V Hacking Gun", [crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.DIVINE], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.LAVISH]], 0, 0, 30, 30, 300, 30, 30, 30)
    HAMMER = ("Hammer", "", [crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.SILVER]], 0, 0, -50, 150, -50, 50, -100, 0)
    HAT_OF_HOPE = ("Hat of Hope", "", [crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.LAVISH]], 80, 0, 80, 80, 80, 80, 80, 80)
    HAT_OF_LEGEND = ("Hat of Legend", "", [crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.STURDY], crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.LAVISH]], 100, 0, 100, 100, 100, 100, 100, 100)
    HAT_OF_OVERFLOWING_TALENT = ("Hat of Overflowing Talent", "", [crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.NORMAL], crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.BIG]], 40, 0, 40, 40, 40, 40, 40, 40)
    HAT_V3 = ("Hat V3", "Ultimate Hat", [crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.DIVINE]], 130, 0, 130, 130, 130, 130, 130, 130)
    HIGH_SCHOOLERS_HAT = ("High Schooler's Hat", "", [crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.SMALL], crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.NORMAL]], 20, 0, 20, 20, 20, 20, 20, 20)
    HIGH_SCHOOLERS_SHOES = ("High Schooler's Shoes", "", [crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.SMALL], crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.NORMAL]], 0, 0, 0, 0, 0, 0, 70, 0)
    HIGH_SCHOOLERS_TALISMAN = ("High Schooler's Talisman", "", [crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.SMALL], crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.NORMAL]], 0, 0, 0, 0, 0, 0, 0, 70)
    HIGH_SCHOOLERS_UNIFORM = ("High Schooler's Uniform", "", [crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.SMALL], crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.NORMAL]], 70, 0, 0, 0, 0, 0, 0, 0)
    SHOES_OF_LEGEND = ("Shoes of Legend", "", [crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.STURDY], crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.LAVISH]], 0, 0, 0, 0, 0, 0, 250, 0)
    HYDRAULIC_PRESS = ("Hydraulic Press", "", [crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.GOLD], crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.GOLD], crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.GOLD]], -50, 0, 250, 250, 250, 250, -999, -999)
    IRON_SKEWER = ("Iron Skewer", "", [crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.COPPER], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.COPPER]], 0, 0, -50, 0, -50, 150, 0, 0)
    JUSTICE_HAMMER = ("JUSTICE HAMMER", "", [crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.COPPER]], 0, 0, -50, 0, -50, 100, 0, 0)
    KATANA = ("Katana", "", [crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.SMALL], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.NORMAL]], 0, 0, 50, 0, 0, 0, 0, 0)
    KATANA_EXTREME = ("Katana Extreme", "", [crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.STURDY]], 0, 0, 150, 0, 0, 0, 0, 0)
    KATANA_V3 = ("Katana V3", "V Katana", [crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.DIVINE], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.LAVISH]], 0, 0, 300, 30, 30, 30, 30, 30)
    KITCHEN_KNIFE = ("Kitchen Knife", "", [crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.COPPER]], 0, 0, 20, -50, 50, -50, 0, -50)
    METAL_BAT = ("Metal Bat", "", [crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.SILVER]], 0, 0, 120, -50, -50, -50, 100, 0)
    MONOKUMAS_SPECIAL_POISON = ("Monokuma's Special Poison", "", [crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.GOLD]], -20, 0, 50, 50, 100, 100, 0, -200)
    PIRANHA = ("Piranha", "", [crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.SILVER]], 0, 0, -50, 0, 150, -50, 0, 0)
    POISON = ("Poison", "", [crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.COPPER]], -60, 0, 120, 50, -100, -120, 20, 0)
    REPLICA_SWORD = ("Replica Sword", "", [crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.COPPER]], 0, 0, 50, -50, 0, -50, 20, -50)
    ROPE_USED_FOR_HANGING = ("Rope Used for Hanging", "", [crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.SILVER]], -50, 0, 0, 0, 150, 150, 0, -100)
    SCISSORS = ("Scissors", "", [crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.GOLD], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.GOLD], crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.GOLD]], 0, 0, 150, 0, -50, -50, 150, 0)
    SHIELD = ("Shield", "", [crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.SMALL], crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.NORMAL]], 0, 0, 0, 50, 0, 0, 0, 0)
    SHIELD_EXTREME = ("Shield Extreme", "", [crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.STURDY]], 0, 0, 0, 150, 0, 0, 0, 0)
    SHIELD_V3 = ("Shield V3", "V Shield", [crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.DIVINE], crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.LAVISH]], 0, 0, 30, 300, 30, 30, 30, 30)
    SHOES_OF_HOPE = ("Shoes of Hope", "", [crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.LAVISH]], 0, 0, 0, 0, 0, 0, 200, 0)
    SHOES_OF_OVERFLOWING_TALENT = ("Shoes of Overflowing Talent", "", [crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.NORMAL], crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.BIG]], 0, 0, 0, 0, 0, 0, 100, 0)
    SHOES_V3 = ("Shoes V3", "Ultimate Shoes", [crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.DIVINE]], 300, 0, 10, 10, 10, 10, 10, 10)
    SHOT_PUT_BALL = ("Shot Put Ball", "", [crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.SILVER]], 0, 0, -50, 200, -50, 0, -100, -100)
    SICKLE = ("Sickle", "", [crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.GOLD]], 0, 0, -50, 0, 50, 150, 0, 0)
    SPEARS_OF_GUNGNIR = ("Spears of Gungnir", "", [crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.GOLD]], 0, 0, 150, 150, -50, -50, 0, -50)
    STAFF = ("Staff", "", [crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.SILVER]], 0, 0, 0, 0, 0, 50, 0, 0)
    STAFF_EXTREME = ("Staff Extreme", "", [crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.STURDY]], 0, 0, 0, 0, 0, 150, 0, 0)
    STAFF_V3 = ("Staff V3", "V Staff", [crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.DIVINE], crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.LAVISH]], 0, 0, 30, 30, 30, 300, 30, 30)
    SUPER_HACKING_GUN = ("Super Hacking Gun", "", [crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.SMALL], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.NORMAL]], 0, 0, 0, 0, 70, 0, 0, 0)
    SUPER_KATANA = ("Super Katana", "", [crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.NORMAL], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.BIG]], 0, 0, 70, 0, 0, 0, 0, 0)
    SUPER_SHIELD = ("Super Shield", "", [crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.NORMAL], crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.BIG]], 0, 0, 0, 70, 0, 0, 0, 0)
    SUPER_STAFF = ("Super Staff", "", [crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.NORMAL], crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.BIG]], 0, 0, 0, 0, 0, 70, 0, 0)
    TALISMAN_OF_HOPE = ("Talisman of Hope", "", [crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.LAVISH]], 0, 0, 0, 0, 0, 0, 0, 200)
    TALISMAN_OF_LEGEND = ("Talisman of Legend", "", [crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.STURDY], crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.LAVISH]], 0, 0, 0, 0, 0, 0, 0, 250)
    TALISMAN_OF_OVERFLOWING_TALENT = ("Talisman of Overflowing Talent", "", [crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.NORMAL], crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.BIG]], 0, 0, 0, 0, 0, 0, 0, 100)
    TALISMAN_V3 = ("Talisman V3", "Ultimate Talisman", [crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.DIVINE]], 10, 0, 10, 10, 10, 10, 10, 300)
    TATTERED_HAT = ("Tattered Hat", "", [crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.SMALL]], 10, 0, 10, 10, 10, 10, 10, 10)
    TATTERED_SHOES = ("Tattered Shoes", "", [crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.SMALL]], 0, 0, 0, 0, 0, 0, 30, 0)
    TATTERED_TALISMAN = ("Tattered Talisman", "", [crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.SMALL]], 0, 0, 0, 0, 0, 0, 0, 30)
    TATTERED_UNIFORM = ("Tattered Uniform", "", [crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.SMALL]], 30, 0, 0, 0, 0, 0, 0, 0)
    THE_END_OF_HACKING_GUN = ("The End of Hacking Gun", "", [crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.DIVINE], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.LAVISH]], 0, 0, 0, 0, 200, 0, 0, 0)
    THE_END_OF_KATANA = ("The End of Katana", "", [crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.DIVINE], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.LAVISH]], 0, 0, 200, 0, 0, 0, 0, 0)
    THE_END_OF_SHIELD = ("The End of Shield", "", [crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.LAVISH], crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.STURDY]], 0, 0, 0, 200, 0, 0, 0, 0)
    THE_END_OF_STAFF = ("The End of Staff", "", [crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.LAVISH], crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.STURDY]], 0, 0, 0, 0, 0, 200, 0, 0)
    TOILET_PAPER = ("Toilet Paper", "", [crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.GOLD]], 0, 0, -50, 200, 200, -50, 0, 0)
    ULTIMATE_____PROOF = ("Ultimate ??? Proof", "", [crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.SILVER], crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.SILVER]], 25, 25, 25, 0, 0, 0, 0, 0)
    ULTIMATE_AFFLUENT_PROGENY_PROOF = ("Ultimate Affluent Progeny Proof", "", [crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.COPPER], crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.COPPER]], 30, 0, 0, 20, 25, 0, 0, 0)
    ULTIMATE_CHILD_CAREGIVER_PROOF = ("Ultimate Child Caregiver Proof", "", [crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.GOLD], crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.GOLD]], 0, 30, 0, 0, 0, 30, 15, 0)
    ULTIMATE_CLAIRVOYANT_PROOF = ("Ultimate Clairvoyant Proof", "", [crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.COPPER], crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.COPPER]], 0, 25, 0, 0, 25, 25, 0, 0)
    ULTIMATE_DESPAIR_PROOF = ("Ultimate Despair Proof", "", [crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.PLATINUM], crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.PLATINUM], crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.PLATINUM]], 75, 75, 0, 0, 0, 0, 0, 0)
    ULTIMATE_GYMNAST_PROOF = ("Ultimate Gymnast Proof", "", [crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.SILVER], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.SILVER]], 0, 25, 25, 25, 0, 0, 0, 0)
    ULTIMATE_HAT = ("Ultimate Hat", "", [crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.STURDY]], 60, 0, 60, 60, 60, 60, 60, 60)
    ULTIMATE_HOPE_PROOF = ("Ultimate Hope Proof", "", [crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.SILVER], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.PLATINUM], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.GOLD], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.COPPER]], 30, 30, 15, 15, 15, 15, 15, 15)
    ULTIMATE_LUCKY_STUDENT_PROOF = ("Ultimate Lucky Student Proof", "", [crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.COPPER], crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.COPPER]], 25, 0, 0, 0, 0, 0, 0, 50)
    ULTIMATE_MAGICIAN_PROOF = ("Ultimate Magician Proof", "", [crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.GOLD], crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.GOLD]], 0, 25, 0, 0, 25, 15, 0, 10)
    ULTIMATE_MECHANIC_PROOF = ("Ultimate Mechanic Proof", "", [crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.SILVER], crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.SILVER]], 0, 20, 0, 15, 20, 0, 0, 20)
    ULTIMATE_MURDEROUS_FIEND_PROOF = ("Ultimate Murderous Fiend Proof", "", [crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.COPPER], crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.COPPER]], 20, -10, 40, 0, 0, -10, 35, 0)
    ULTIMATE_PRINCESS_PROOF = ("Ultimate Princess Proof", "", [crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.SILVER], crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.SILVER]], 50, 0, 0, 0, 15, 10, 0, 0)
    ULTIMATE_SHOES = ("Ultimate Shoes", "", [crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.STURDY]], 5, 0, 5, 5, 5, 5, 150, 5)
    ULTIMATE_SWIMMING_PRO_PROOF = ("Ultimate Swimming Pro Proof", "", [crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.COPPER], crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.COPPER]], 0, 10, 10, 50, 0, 0, 0, 0)
    ULTIMATE_TALISMAN = ("Ultimate Talisman", "", [crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.STURDY]], 5, 0, 5, 5, 5, 5, 5, 150)
    ULTIMATE_UNIFORM = ("Ultimate Uniform", "", [crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.STURDY]], 150, 0, 5, 5, 5, 5, 5, 5)
    ULTIMATE_WRITING_PRODIGY_PROOF = ("Ultimate Writing Prodigy Proof", "", [crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.COPPER], crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.COPPER]], 0, 35, 0, 0, 25, 15, 0, 0)
    ULTIMATE_YAKUZA_PROOF = ("Ultimate Yakuza Proof", "", [crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.SILVER], crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.SILVER]], 20, 0, 0, 15, 0, 40, 0, 0)
    UNIFORM_OF_HOPE = ("Ultimate of Hope", "", [crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.LAVISH]], 200, 0, 0, 0, 0, 0, 0, 0)
    UNIFORM_OF_LEGEND = ("Uniform of Legend", "", [crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.STURDY], crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.LAVISH]], 250, 0, 0, 0, 0, 0, 0, 0)
    UNIFORM_OF_OVERFLOWING_TALENT = ("Uniform of Overflowing Talent", "", [crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.NORMAL], crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.BIG]], 100, 0, 0, 0, 0, 0, 0, 0)
    UNIFORM_V3 = ("Uniform V3", "Ultimate Uniform", [crafting_materials[CraftingMaterialType.MONSTER_SKIN][CraftingMaterialQuality.DIVINE]], 300, 0, 10, 10, 10, 10, 10, 10)
    V_HACKING_GUN = ("V Hacking Gun", "", [crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.STURDY]], 0, 0, 15, 15, 100, 15, 15, 15)
    V_KATANA = ("V Katana", "", [crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.STURDY]], 0, 0, 100, 15, 15, 15, 15, 15)
    V_SHIELD = ("V Shield", "", [crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.STURDY]], 0, 0, 15, 100, 15, 15, 15, 15)
    V_STAFF = ("V Staff", "", [crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.BIG], crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.STURDY]], 0, 0, 15, 15, 15, 100, 15, 15)
    WORN_HACKING_GUN = ("Worn Hacking Gun", "", [crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.SMALL]], 0, 0, 0, 0, 30, 0, 0, 0)
    WORN_KATANA = ("Worn Katana", "", [crafting_materials[CraftingMaterialType.MONSTER_FANG][CraftingMaterialQuality.SMALL]], 0, 0, 30, 0, 0, 0, 0, 0)
    WORN_SHIELD = ("Worn Shield", "", [crafting_materials[CraftingMaterialType.MONSTER_EYE][CraftingMaterialQuality.SMALL]], 0, 0, 0, 30, 0, 0, 0, 0)
    WORN_STAFF = ("Worn Staff", "", [crafting_materials[CraftingMaterialType.MONSTER_MEAT][CraftingMaterialQuality.SMALL]], 0, 0, 0, 0, 0, 30, 0, 0)


##NAME = ("name", "", [crafting_materials[CraftingMaterialType.MONSTER_FUR][CraftingMaterialQuality.SILVER]], 0, 0, 0, 0, 0, 0, 0, 0)

    def __init__(self, item_name: str, prereq_item_name: str, material_list: list[CraftingMaterial], influence: int, focus: int, strength: int, stamina: int, intellect: int, endurance: int, agility: int, luck: int) -> None:
        self.item_name: str = item_name
        self.prereq_item_name: str = prereq_item_name
        self.material_list: list[CraftingMaterial] = material_list
        self.influence: int = influence
        self.focus: int = focus
        self.strength: int = strength
        self.stamina: int = stamina
        self.intellect: int = intellect
        self.endurance: int = endurance
        self.agility: int = agility
        self.luck: int = luck


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







# TODO figure out what data is needed for enemies and map it (similar to Events)
# Enemies

# Floors
# "Combat Score" (how hard are they to kill)
# immunities






enemy_list = [
    "Monokumamel",
    "Monokumamel V",
    "Monokumamel V2",
    "Monokumamel V3",
    "Fluffy Monobunny",
    "Fluffy Monobunny V",
    "Fluffy Monobunny V2",
    "Fluffy Monobunny V3",
    "Monokuma Gather",
    "Monokuma Gather V",
    "Monokuma Gather V2",
    "Monokuma Gather V3",
    "Monokuma Hermit",
    "Monokuma Hermit V",
    "Monokuma Hermit V2",
    "Monokuma Hermit V3",
    "Curse Monogirl",
    "Curse Monogirl V",
    "Curse Monogirl V2",
    "Curse Monogirl V3",
    "Monokumantala",
    "Monokumantala V",
    "Monokumantala V2",
    "Monokumantala V3",
    "Monodragon Head",
    "Monodragon Head V",
    "Monodragon Head V2",
    "Monodragon Head V3",
    "Floor Monodragon",
    "Floor Monodragon V",
    "Floor Monodragon V2",
    "Floor Monodragon V3",
    "Twisty Monokuma",
    "Twisty Monokuma V",
    "Twisty Monokuma V2",
    "Twisty Monokuma V3",
    "Monokumamel B",
    "Monokumamel S",
    "Monokumamel G",
    "Monokumamel P",
    "Exisal Blue",
    "Exisal Yellow",
    "Exisal Green",
    "Exisal Pink",
    "Exisal V3",
    "Monokumasect",
    "Monokumasect V3",
    "Monokuma Tank",
    "Monokuma Tank V3",
    "Monokuma Boss",
    "Monokuma Boss V3",
    "Mon'Duba",
    "Mon'Duba V3",
    "Monokoppa",
    "Monokoppa V3",
    "Monokuma V3",
    "Exisal Red",
    "Vanguard Monokuma",
    "Vanguard Monokuma 2",
    "Vanguard Monokuma ZZ",
    "Vanguard Monokuma V3",
    "Monosludge",
    "Monosludge 2",
    "Monosludge ZZ",
    "Monosludge V3",
    "Monohelper",
    "Monohelper 2",
    "Monohelper ZZ",
    "Monohelper V3",
    "Gangstakuma",
    "Gangstakuma 2",
    "Gangstakuma ZZ",
    "Gangstakuma V3",
    "Aetherkuma",
    "Aetherkuma 2",
    "Aetherkuma ZZ",
    "Aetherkuma V3",
    "Bonykuma",
    "Bonykuma 2",
    "Bonykuma ZZ",
    "Bonykuma V3",
    "Monokuma Samurai",
    "Monokuma Samurai 2",
    "Monokuma Samurai ZZ",
    "Monokuma Samurai V3",
    "Monobel",
    "Monobel 2",
    "Monobel ZZ",
    "Monobel V3",
    "Abyssal Monokuma",
    "Abyssal Monokuma 2",
    "Abyssal Monokuma ZZ",
    "Abyssal Monokuma V3",
    "Volatile Monourchin",
    "Volatile Monourchin 2",
    "Volatile Monourchin ZZ",
    "Volatile Monourchin V3",
    "Monobeast (Tiger)",
    "Monobeast (Tiger Awakened)",
    "Monobeast (Bird)",
    "Monobeast (Bird Awakened)",
    "Monobeast (Horse)",
    "Monobeast (Horse Awakened)",
    "Monobeast (Snake)",
    "Monobeast (Snake Awakened)",
    "Monobeast (Human)",
    "Monobeast (Human Awakened)",
    "Almighty Jabberwock",
    "Almighty Jabberwock Awakened",
    "Monokid",
    "Monosuke",
    "Monodam",
    "Monophanie",
    "Monotaro",
    "Monokuma",
    "Mage Robot",
    "Hero Robot",
    "Priest Robot",
    "Warrior Robot",
    "Sage Robot",
    "Monokubs",
]


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


# TODO finish Event enum
class CharacterEvent(enum.Enum):
    JUNKO_AND_MAKOTO = ("Junko & Makoto", CharacterEventType.FRIEND, [Character.JUNKO_ENOSHIMA, Character.MAKOTO_NAEGI])
    MAKOTO_CAMPFIRE = ("Campfire - Makoto", CharacterEventType.CAMPFIRE, [Character.MAKOTO_NAEGI])
    MAKOTO_FUTURE = ("My Future... - Makoto", CharacterEventType.MY_FUTURE, [Character.MAKOTO_NAEGI])
    MAKOTO_POTENTIAL = ("Potential of Talent - Makoto", CharacterEventType.POTENTIAL_TALENT, [Character.MAKOTO_NAEGI])
    MAKOTO_SUMMER = ("Summer Festival - Makoto", CharacterEventType.SUMMER_FESTIVAL, [Character.MAKOTO_NAEGI])
    MAKOTO_SWIMSUIT = ("With Swimsuits - Makoto", CharacterEventType.SWIMSUIT, [Character.MAKOTO_NAEGI])



    def __init__(self, event_name: str, event_type: CharacterEventType, char_list: list[Character]) -> None:
        self.event_name: str = event_name
        self.event_type: CharacterEventType = event_type
        self.char_list: list[Character] = char_list



friendsanity = [
    "Akane & Chiaki & Peko",
    "Akane & Jataro",
    "Akane & Shirokuma",
    "Akane & Sonia",
    "Angie & Celestia",
    "Angie & Hifumi & Gundham",
    "Angie & Kaede",
    "Angie & Leon",
    "Angie & Monokuma",
    "Angie & Monomi & Jataro",
    "Angie & Nagito",
    "Angie & Sonia",
    "Aoi & Akane",
    "Aoi & Chiaki",
    "Aoi & Mukuro",
    "Aoi & Nagisa",
    "Byakuya & Hajime",
    "Byakuya & Hiroko",
    "Byakuya & Mukuro",
    "Byakuya & Kyoko",
    "Byakuya & Sonia",
    "Byakuya & Toko & Peko",
    "The Ultimate Imposter & Teruteru",
    "Campfire - Akane",
    "Campfire - Angie",
    "Campfire - Aoi",
    "Campfire - Byakuya",
    "Campfire - The Ultimate Imposter",
    "Campfire - Celestia",
    "Campfire - Chiaki",
    "Campfire - Chihiro",
    "Campfire - Fuyuhiko",
    "Campfire - Gonta",
    "Campfire - Gundham",
    "Campfire - Hajime",
    "Campfire - Hifumi",
    "Campfire - Himiko",
    "Campfire - Hiroko",
    "Campfire - Hiyoko",
    "Campfire - Ibuki",
    "Campfire - Izuru",
    "Campfire - Jack",
    "Campfire - Jataro",
    "Campfire - Junko",
    "Campfire - Mukuro",
    "Campfire - K1-B0",
    "Campfire - Kaede",
    "Campfire - Kaito",
    "Campfire - Kazuichi",
    "Campfire - Kirumi",
    "Campfire - Kiyotaka",
    "Campfire - Kokichi",
    "Campfire - Komaru",
    "Campfire - Korekiyo",
    "Campfire - Kotoko",
    "Campfire - Kurokuma",
    "Campfire - Kyoko",
    "Campfire - Leon",
    "Campfire - Mahiru",
    "Campfire - Maki",
    "Campfire - Makoto",
    "Campfire - Masaru",
    "Campfire - Mikan",
    "Campfire - Miu",
    "Campfire - Monaca",
    "Campfire - Mondo",
    "Campfire - Monokuma",
    "Campfire - Monomi",
    "Campfire - Nagisa",
    "Campfire - Nagito",
    "Campfire - Nekomaru",
    "Campfire - Peko",
    "Campfire - Rantaro",
    "Campfire - Ryoma",
    "Campfire - Sakura",
    "Campfire - Sakyaka",
    "Campfire - Shirokuma",
    "Campfire - Shuichi",
    "Campfire - Sonia",
    "Campfire - Tenko",
    "Campfire - Teruteru",
    "Campfire - Toko",
    "Campfire - Tsumugi",
    "Campfire - Usami",
    "Campfire - Yasuhiro",
    "Celestia & Chiaki",
    "Celestia & Fuyuhiko",
    "Celestia & Komaru & Monaca",
    "Celestia & Masaru",
    "Celestia & Sonia",
    "Chiaki & Ibuki",
    "Chihiro & Fuyuhiko",
    "Chihiro & Jataro",
    "Chihiro & Nekomaru",
    "Chihiro & Sakura",
    "Chihiro & Sonia & Shirokuma",
    "Fuyuhiko & Kotoko",
    "Fuyuhiko & Mikan & Ibuki",
    "Fuyuhiko & Peko",
    "Genocide Jack & The Ultimate Imposter",
    "Genocide Jack & Celestia & Kotoko",
    "Genocide Jack & Hiyoko",
    "Genocide Jack & Komaru",
    "Genocide Jack & Sonia",
    "Genocide Jack & Teruteru & Monomi",
    "Gonta & Aoi & Gundham",
    "Gonta & Hajime",
    "Gonta & Mukuro & Monaca",
    "Gonta & K1-B0 & Kurokuma",
    "Gonta & Kiyotaka",
    "Gonta & Kokichi",
    "Gonta & Shirokuma",
    "Gonta & Sonia",
    "Gonta & Toko",
    "Gundham & Kazuichi & Sonia",
    "Gundham & Peko",
    "Hajime & Gundham",
    "Hajime & Hiyoko",
    "Hajime & Mahiru & Mikan",
    "Hifumi & Hiyoko & Kotoko",
    "Hifumi & Nagisa",
    "Hifumi & Peko",
    "Hifumi & Teruteru",
    "Hifumi & Toko",
    "Himiko & Akane & Kotoko",
    "Himiko & Celestia & Teruteru",
    "Himiko & Hajime",
    "Himiko & Hiyoko & Mahiru",
    "Himiko & Ibuki",
    "Himiko & Masaru",
    "Himiko & Sakura & Nekomaru",
    "Himiko & Tenko",
    "Himiko & Yasuhiro",
    "Hiyoko & Monaca",
    "Hiyoko & Shirokuma & Hiroko",
    "Ibuki & Kurokuma",
    "Ibuki & Monomi",
    "Izuru & Byakuya",
    "Izuru & Gonta",
    "Izuru & Gundham",
    "Izuru & Himiko",
    "Izuru & Hiyoko",
    "Izuru & Kirumi & Chiaki",
    "Izuru & Leon & Chihiro",
    "Izuru & Mahiru & Mikan",
    "Izuru & Monokuma",
    "Izuru & Ryoma & Nagito",
    "Izuru & Sayaka",
    "Jataro & Kotoko",
    "Jataro & Kurokuma",
    "Junko & Aoi",
    "Junko & Byakuya",
    "Junko & Gonta & Monaca",
    "Junko & Mahiru",
    "Junko & Makoto",
    "Junko & Mondo",
    "Junko & Sakura & Ibuki",
    "Junko & Tenko & Akane",
    "Junko & Toko & Mikan",
    "Junko & Yasuhiro",
    "Mukuro & Mahiru",
    "K1-B0 & Angie",
    "K1-B0 & The Ultimate Imposter",
    "K1-B0 & Celestia",
    "K1-B0 & Chiaki",
    "K1-B0 & Chihiro & Kazuichi",
    "K1-B0 & Leon",
    "K1-B0 & Masaru & Jataro",
    "K1-B0 & Teruteru",
    "Kaede & Fuyuhiko",
    "Kaede & Komaru",
    "Kaede & Makoto & Masaru",
    "Kaede & Sayaka & Ibuki",
    "Kaito & Akane",
    "Kaito & Aoi",
    "Kaito & Byakuya & Ibuki",
    "Kaito & Gundham",
    "Kaito & Jataro",
    "Kaito & Kaede",
    "Kaito & Kiyotaka & Masaru",
    "Kaito & Ryoma",
    "Kaito & Tenko & Leon",
    "Kazuichi & Fuyuhiko & Nagisa",
    "Kazuichi & Jataro",
    "Kazuichi & Mahiru",
    "Kirumi & Chihiro",
    "Kirumi & Hajime & Chiaki",
    "Kirumi & Komaru",
    "Kirumi & Leon & Kyoko",
    "Kirumi & Mahiru",
    "Kirumi & Sakura",
    "Kirumi & Sonia",
    "Kirumi & Teruteru & Sonia",
    "Kirumi & Tsumugi",
    "Kiyotaka & Akane",
    "Kiyotaka & Celestia",
    "Kiyotaka & Mondo & Sayaka",
    "Kiyotaka & Nagisa",
    "Kiyotaka & Nekomaru",
    "Kokichi & Byakuya & The Ultimate Imposter",
    "Kokichi & Genocide Jack",
    "Kokichi & Hiyoko",
    "Kokichi & Kazuichi",
    "Kokichi & Mahiru",
    "Kokichi & Makoto & Hiroko",
    "Kokichi & Monaca",
    "Kokichi & Monokuma & Chiaki",
    "Komaru & Kotoko & Monaca",
    "Korekiyo & Angie & Toko",
    "Korekiyo & Hifumi",
    "Korekiyo & Hifumi & Sonia",
    "Korekiyo & Mikan",
    "Korekiyo & Nagito",
    "Korekiyo & Sayaka",
    "Korekiyo & Shirokuma",
    "Korekiyo & Tsumugi",
    "Kyoko & Fuyuhiko & Kurokuma",
    "Kyoko & Gundham",
    "Kyoko & Mahiru",
    "Kyoko & Monaca",
    "Leon & Chiaki",
    "Leon & Hajime & Chihiro",
    "Leon & Hifumi",
    "Leon & Nagito",
    "Leon & Sakura",
    "Mahiru & Nagisa",
    "Maki & The Ultimate Imposter",
    "Maki & Chihiro & Chiaki",
    "Maki & Kaede",
    "Maki & Komaru",
    "Maki & Makoto",
    "Maki & Monomi",
    "Maki & Nekomaru & Peko",
    "Maki & Sakura & Nagisa",
    "Maki & Sayaka",
    "Maki & Yasuhiro & Hiyoko",
    "Makoto & Byakuya",
    "Makoto & Chiaki",
    "Makoto & Gundham",
    "Makoto & Mukuro",
    "Makoto & Sayaka & Komaru",
    "Masaru & Jataro & Nagisa",
    "Masaru & Kotoko",
    "Mikan & Shirokuma",
    "Miu & Byakuya & Genocide Jack",
    "Miu & Jataro",
    "Miu & Kaede",
    "Miu & Kazuichi & Monomi",
    "Miu & Kurokuma",
    "Miu & Mikan",
    "Miu & Mondo & Hiroko",
    "Miu & Monomi",
    "Miu & Yasuhiro",
    "Monaca & Hiroko",
    "Mondo & Fuyuhiko",
    "Mondo & Mukuro",
    "Mondo & Kazuichi",
    "Mondo & Mikan",
    "Mondo & Nagisa",
    "Mondo & Nekomaru & Kurokuma",
    "Monokuma & Chihiro",
    "Monokuma & Genocide Jack",
    "Monokuma & Hajime",
    "Monokuma & Hiyoko",
    "Monokuma & Komaru & Hiroko",
    "Monokuma & Monomi",
    "Monokuma & Shirokuma & Kurokuma",
    "Monomi & Kurokuma",
    "My Future... - Akane",
    "My Future... - Angie",
    "My Future... - Aoi",
    "My Future... - Byakuya",
    "My Future... - The Ultimate Imposter",
    "My Future... - Celestia",
    "My Future... - Chiaki",
    "My Future... - Chihiro",
    "My Future... - Fuyuhiko",
    "My Future... - Gonta",
    "My Future... - Gundham",
    "My Future... - Hajime",
    "My Future... - Hifumi",
    "My Future... - Himiko",
    "My Future... - Hiroko",
    "My Future... - Hiyoko",
    "My Future... - Ibuki",
    "My Future... - Izuru",
    "My Future... - Jack",
    "My Future... - Jataro",
    "My Future... - Junko",
    "My Future... - K1-B0",
    "My Future... - Kaede",
    "My Future... - Kaito",
    "My Future... - Kazuichi",
    "My Future... - Kirumi",
    "My Future... - Kiyoko",
    "My Future... - Kiyotaka",
    "My Future... - Kokichi",
    "My Future... - Komaru",
    "My Future... - Korekiyo",
    "My Future... - Kotoko",
    "My Future... - Kurokuma",
    "My Future... - Leon",
    "My Future... - Mahiru",
    "My Future... - Maki",
    "My Future... - Makoto",
    "My Future... - Masaru",
    "My Future... - Mikan",
    "My Future... - Miu",
    "My Future... - Monaca",
    "My Future... - Mondo",
    "My Future... - Monokuma",
    "My Future... - Monomi",
    "My Future... - Nagisa",
    "My Future... - Nagito",
    "My Future... - Nekomaru",
    "My Future... - Peko",
    "My Future... - Rantaro",
    "My Future... - Ryoma",
    "My Future... - Sakura",
    "My Future... - Sayaka",
    "My Future... - Shirokuma",
    "My Future... - Shuichi",
    "My Future... - Sonia",
    "My Future... - Tenko",
    "My Future... - Teruteru",
    "My Future... - Toko",
    "My Future... - Tsumugi",
    "My Future... - Usami",
    "My Future... - Yasuhiro",
    "My Future...- Mukuro",
    "Nagisa & Monaca",
    "Nagisa & Shirokuma",
    "Nagito & Kazuichi",
    "Nagito & Mikan",
    "Nagito & Monaca",
    "Nekomaru & Masaru",
    "Peko & Masaru",
    "Potential of Talent - Akane",
    "Potential of Talent - Angie",
    "Potential of Talent - Aoi",
    "Potential of Talent - Byakuya",
    "Potential of Talent - The Ultimate Imposter",
    "Potential of Talent - Celestia",
    "Potential of Talent - Chiaki",
    "Potential of Talent - Chihiro",
    "Potential of Talent - Fuyuhiko",
    "Potential of Talent - Gonta",
    "Potential of Talent - Gundham",
    "Potential of Talent - Hajime",
    "Potential of Talent - Hifumi",
    "Potential of Talent - Himiko",
    "Potential of Talent - Hiroko",
    "Potential of Talent - Hiyoko",
    "Potential of Talent - Ibuki",
    "Potential of Talent - Izuru",
    "Potential of Talent - Jack",
    "Potential of Talent - Jataro",
    "Potential of Talent - Junko",
    "Potential of Talent - Mukuro",
    "Potential of Talent - K1-B0",
    "Potential of Talent - Kaede",
    "Potential of Talent - Kaito",
    "Potential of Talent - Kazuichi",
    "Potential of Talent - Kirumi",
    "Potential of Talent - Kiyotaka",
    "Potential of Talent - Kokichi",
    "Potential of Talent - Komaru",
    "Potential of Talent - Korekiyo",
    "Potential of Talent - Kotoko",
    "Potential of Talent - Kurokuma",
    "Potential of Talent - Kyoko",
    "Potential of Talent - Leon",
    "Potential of Talent - Mahiru",
    "Potential of Talent - Maki",
    "Potential of Talent - Makoto",
    "Potential of Talent - Masaru",
    "Potential of Talent - Mikan",
    "Potential of Talent - Miu",
    "Potential of Talent - Monaca",
    "Potential of Talent - Mondo",
    "Potential of Talent - Monokuma",
    "Potential of Talent - Monomi",
    "Potential of Talent - Nagisa",
    "Potential of Talent - Nagito",
    "Potential of Talent - Nekomaru",
    "Potential of Talent - Peko",
    "Potential of Talent - Rantaro",
    "Potential of Talent - Ryoma",
    "Potential of Talent - Sakura",
    "Potential of Talent - Sayaka",
    "Potential of Talent - Shirokuma",
    "Potential of Talent - Shuichi",
    "Potential of Talent - Sonia",
    "Potential of Talent - Tenko",
    "Potential of Talent - Teruteru",
    "Potential of Talent - Toko",
    "Potential of Talent - Tsumugi",
    "Potential of Talent - Usami",
    "Potential of Talent - Yasuhiro",
    "Rantaro & Gonta",
    "Rantaro & Hiroko",
    "Rantaro & Ibuki",
    "Rantaro & Kaede",
    "Rantaro & Kiyotaka & The Ultimate Imposter",
    "Rantaro & Korekiyo & Fuyuhiko",
    "Rantaro & Leon",
    "Rantaro & Mahiru",
    "Rantaro & Peko & Shirokuma",
    "Rantaro & Teruteru",
    "Rantaro & Yasuhiro & Nagito",
    "Ryoma & The Ultimate Imposter",
    "Ryoma & Hajime & Nagito",
    "Ryoma & Himiko",
    "Ryoma & Kurokuma",
    "Ryoma & Kyoko",
    "Ryoma & Miu & Monokuma",
    "Ryoma & Mondo",
    "Ryoma & Nekomaru & Mikan",
    "Ryoma & Peko",
    "Ryoma & Yasuhiro & Monaca",
    "Sakura & Akane",
    "Sakura & Celestia",
    "Sakura & Gundham",
    "Sakura & Mukuro & Ibuki",
    "Sakura & Nekomaru",
    "Sayaka & Hajime",
    "Sayaka & Kazuichi",
    "Sayaka & Kotoko",
    "Sayaka & Kyoko & Aoi",
    "Sayaka & Peko",
    "Shirokuma & Kurokuma",
    "Shuichi & The Ultimate Imposter",
    "Shuichi & Kaede & Toko",
    "Shuichi & Kaito & Maki",
    "Shuichi & Kirumi",
    "Shuichi & Kiyotaka",
    "Shuichi & Kokichi & K1-B0",
    "Shuichi & Komaru",
    "Shuichi & Korekiyo",
    "Shuichi & Kyoko & Makoto",
    "Shuichi & Nagito & Mahiru",
    "Summer Festival - Akane",
    "Summer Festival - Angie",
    "Summer Festival - Aoi",
    "Summer Festival - Byakuya",
    "Summer Festival - The Ultimate Imposter",
    "Summer Festival - Celestia",
    "Summer Festival - Chiaki",
    "Summer Festival - Chihiro",
    "Summer Festival - Fuyuhiko",
    "Summer Festival - Gonta",
    "Summer Festival - Gundham",
    "Summer Festival - Hajime",
    "Summer Festival - Hifumi",
    "Summer Festival - Himiko",
    "Summer Festival - Hiroko",
    "Summer Festival - Hiyoko",
    "Summer Festival - Ibuki",
    "Summer Festival - Izuru",
    "Summer Festival - Jack",
    "Summer Festival - Jataro",
    "Summer Festival - Junko",
    "Summer Festival - Mukuro",
    "Summer Festival - K1-B0",
    "Summer Festival - Kaede",
    "Summer Festival - Kaito",
    "Summer Festival - Kazuichi",
    "Summer Festival - Kirumi",
    "Summer Festival - Kiyotaka",
    "Summer Festival - Kokichi",
    "Summer Festival - Komaru",
    "Summer Festival - Korekiyo",
    "Summer Festival - Kotoko",
    "Summer Festival - Kurokuma",
    "Summer Festival - Kyoko",
    "Summer Festival - Leon",
    "Summer Festival - Mahiru",
    "Summer Festival - Maki",
    "Summer Festival - Makoto",
    "Summer Festival - Masaru",
    "Summer Festival - Mikan",
    "Summer Festival - Miu",
    "Summer Festival - Monaca",
    "Summer Festival - Mondo",
    "Summer Festival - Monokuma",
    "Summer Festival - Monomi",
    "Summer Festival - Nagisa",
    "Summer Festival - Nagito",
    "Summer Festival - Nekomaru",
    "Summer Festival - Peko",
    "Summer Festival - Rantaro",
    "Summer Festival - Ryoma",
    "Summer Festival - Sakura",
    "Summer Festival - Sayaka",
    "Summer Festival - Shirokuma",
    "Summer Festival - Shuichi",
    "Summer Festival - Sonia",
    "Summer Festival - Tenko",
    "Summer Festival - Teruteru",
    "Summer Festival - Toko",
    "Summer Festival - Tsumugi",
    "Summer Festival - Usami",
    "Summer Festival - Yasuhiro",
    "Tenko & Aoi",
    "Tenko & Hiroko",
    "Tenko & Ibuki",
    "Tenko & Mukuro & Akane",
    "Tenko & Makoto & The Ultimate Imposter",
    "Tenko & Masaru",
    "Tenko & Mondo & Chihiro",
    "Tenko & Nekomaru",
    "Teruteru & Hiroko",
    "Teruteru & Kotoko",
    "Teruteru & Nekomaru",
    "Toko & Hiyoko",
    "Toko & Mukuro & Mikan",
    "Toko & Komaru",
    "Toko & Monaca",
    "Toko & Nagito",
    "Tsumugi & Aoi & Akane",
    "Tsumugi & The Ultimate Imposter",
    "Tsumugi & Genocide Jack & Gundham",
    "Tsumugi & Hifumi & Mahiru",
    "Tsumugi & Kiyotaka & Yasuhiro",
    "Tsumugi & Kotoko",
    "Tsumugi & Kyoko",
    "Tsumugi & Makoto",
    "Tsumugi & Monomi",
    "Usami & Angie & Jataro",
    "Usami & Genocide Jack & Teruteru",
    "Usami & Ibuki",
    "Usami & Kurokuma",
    "Usami & Maki",
    "Usami & Miu",
    "Usami & Miu & Kazuichi",
    "Usami & Monokuma",
    "Usami & Tsumugi",
    "With Swimsuits - Akane",
    "With Swimsuits - Angie",
    "With Swimsuits - Aoi",
    "With Swimsuits - Byakuya",
    "With Swimsuits - The Ultimate Imposter",
    "With Swimsuits - Celestia",
    "With Swimsuits - Chiaki",
    "With Swimsuits - Chihiro",
    "With Swimsuits - Fuyuhiko",
    "With Swimsuits - Gonta",
    "With Swimsuits - Gundham",
    "With Swimsuits - Hajime",
    "With Swimsuits - Hifumi",
    "With Swimsuits - Himiko",
    "With Swimsuits - Hiroko",
    "With Swimsuits - Hiyoko",
    "With Swimsuits - Ibuki",
    "With Swimsuits - Izuru",
    "With Swimsuits - Jack",
    "With Swimsuits - Jataro",
    "With Swimsuits - Junko",
    "With Swimsuits - Mukuro",
    "With Swimsuits - K1-B0",
    "With Swimsuits - Kaede",
    "With Swimsuits - Kaito",
    "With Swimsuits - Kazuichi",
    "With Swimsuits - Kirumi",
    "With Swimsuits - Kiyotaka",
    "With Swimsuits - Kokichi",
    "With Swimsuits - Komaru",
    "With Swimsuits - Korekiyo",
    "With Swimsuits - Kotoko",
    "With Swimsuits - Kurokuma",
    "With Swimsuits - Kyoko",
    "With Swimsuits - Leon",
    "With Swimsuits - Mahiru",
    "With Swimsuits - Maki",
    "With Swimsuits - Makoto",
    "With Swimsuits - Masaru",
    "With Swimsuits - Mikan",
    "With Swimsuits - Miu",
    "With Swimsuits - Monaca",
    "With Swimsuits - Mondo",
    "With Swimsuits - Monokuma",
    "With Swimsuits - Monomi",
    "With Swimsuits - Nagisa",
    "With Swimsuits - Nagito",
    "With Swimsuits - Nekomaru",
    "With Swimsuits - Peko",
    "With Swimsuits - Rantaro",
    "With Swimsuits - Ryoma",
    "With Swimsuits - Sakura",
    "With Swimsuits - Sayaka",
    "With Swimsuits - Shirokuma",
    "With Swimsuits - Shuichi",
    "With Swimsuits - Sonia",
    "With Swimsuits - Tenko",
    "With Swimsuits - Teruteru",
    "With Swimsuits - Toko",
    "With Swimsuits - Tsumugi",
    "With Swimsuits - Usami",
    "With Swimsuits - Yasuhiro",
    "Yasuhiro & Aoi",
    "Yasuhiro & Gundham",
    "Yasuhiro & Hiroko",
    "Yasuhiro & Mukuro",
    "Yasuhiro & Mikan",
]


