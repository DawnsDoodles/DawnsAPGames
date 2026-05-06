from enum import StrEnum

from worlds.AutoWorld import World

DANGANRONPA_S = "DanganronpaS"















# Mess.
##class CraftingMaterialType(StrEnum):
##    MONSTERFANG = "Monster Fang"
##    MONSTERMEAT = "Monster Meat"
##    MONSTEREYE = "Monster Eye"
##    MONSTERFUR = "Monster Fur"
##    MONSTERSKIN = "Monster Skin"


##class CraftingMaterialQuality(StrEnum):
##    SMALL = "Small"
##    NORMAL = ""
##    BIG = "Big"
##    STURDY = "Sturdy"
##    DIVINE = "Divine"
##    LAVISH = "Lavish"
##    COPPER = "Copper"
##    SILVER = "Silver"
##    GOLD = "Gold"
##    PLATINUM = "Platinum"


##def crafting_mat_name(type: CraftingMaterialType, quality: CraftingMaterialQuality) -> str:
##    result: str = f"{quality}"
##    if quality != CraftingMaterialQuality.NORMAL:
##        result += " "
##    result += f"{type}"
##    return result




##KATANAWORN: str = "Worn Katana"
##KATANA: str = "Katana"
##KATANASUPER: str = "Super Katana"
##KATANAV: str = "V Katana"
##KATANAEXTREME: str = "Katana Extreme"
##KATANAEND: str = "The End of Katana"
##KATANAV3: str = "Katana V3"
##GUNWORN: str = "Worn Gun"
##GUN: str = "Hacking Gun"
##GUNSUPER: str = "Super Hacking Gun"
##GUNV: str = "Hacking Gun V"
##GUNEXTREME: str = "Hacking Gun Extreme"
##GUNEND: str = "The End of Hacking Gun"
##GUNV3: str = "Hacking Gun V3"
##STAFFWORN: str = "Worn Staff"
##STAFF: str = "Staff"
##STAFFSUPER: str = "Super Staff"
##STAFFV: str = "V Staff"
##STAFFEXTREME: str = "Extreme Staff"
##STAFFEND: str = "The End of Staff"
##STAFFV3: str = "Staff V3"
##SHIELDWORN: str = "Worn Shield"
##SHIELD: str = "Shield"
##SHIELDSUPER: str = "Super Shield"
##SHIELDV: str = "V Shield"
##SHIELDEXTREME: str = "Extreme Shield"
##SHIELDEND: str = "The End of Shield"
##SHIELDV3: str = "Shield V3"
##REPLICASWORD: str = "Replica Sword"
##KITCHENKNIFE: str = "Kitchen Knife"
##DUMBBELL: str = "Dumbbell"
##JUSTICEHAMMER: str = "JUSTICE HAMMER"
##POISON: str = "Poison"
##IRONSKEWER: str = "Iron Skewer"
##METALBAT: str = "Metal Bat"
##ROPEUSEDFORHANGING: str = "Rope Used for Hanging"
##HAMMER: str = "Hammer"
##ARMYKNIFE: str = "Army Knife"
##SPEARSOFGUNGNIR: str = "Spears of Gungnir"
##MONOKUMASPECIALPOISON: str = "Monokuma's Special Poison"
##SCISSORS: str = "Scissors"
##SHOTPUTBALL: str = "Shot Put Ball"
##PIRANHA: str = "Piranha"
##GOLDLEAFKATANA: str = "Gold Leaf Katana"
##SICKLE: str = "Sickle"
##TOILETPAPER: str = "Toilet Paper"
##CROSSBOW: str = "Crossbow"
##HYDRAULICPRESS: str = "Hydraulic Press"
##HATTATTERED: str = "Tattered Hat"
##HATHIGHSCHOOLER: str = "High Schooler's Hat"
##HATOVERFLOWINGTALENT: str = "Hat of Overflowing Talent"
##HATULTIMATE: str = "Ultimate Hat"
##HATOFHOPE: str = "Hat of Hope"
##HATOFLEGEND: str = "Hat of Legend"
##HATV3: str = "Hat V3"
##UNIFORMTATTERED: str = "Tattered Uniform"
##UNIFORMHIGHSCHOOLER: str = "High Schooler's Uniform"
##UNIFORMOVERFLOWINGTALENT: str = "Uniform of Overflowing Talent"
##UNIFORMULTIMATE: str = "Ultimate Uniform"
##UNIFORMOFHOPE: str = "Uniform of Hope"
##UNIFORMOFLEGEND: str = "Uniform of Legend"
##UNIFORMV3: str = "Uniform V3"
##SHOESTATTERED: str = "Tattered Shoes"
##SHOESHIGHSCHOOLER: str = "High Schooler's Shoes"
##SHOESOVERFLOWINGTALENT: str = "Shoes of Overflowing Talent"
##SHOESULTIMATE: str = "Ultimate Shoes"
##SHOESOFHOPE: str = "Shoes of Hope"
##SHOESOFLEGEND: str = "Shoes of Legend"
##SHOESV3: str = "Shoes V3"
##TALISMANTATTERED: str = "Tattered Talisman"
##TALISMANHIGHSCHOOLER: str = "High Schooler's Talisman"
##TALISMANOVERFLOWINGTALENT: str = "Talisman of Overflowing Talent"
##TALISMANULTIMATE: str = "Ultimate Talisman"
##TALISMANOFHOPE: str = "Talisman of Hope"
##TALISMANOFLEGEND: str = "Talisman of Legend"
##TALISMANV3: str = "Talisman V3"
##ULTIMATELUCKYSTUDENTPROOF: str = "Ultimate Lucky Student Proof"
##ULTIMATEAFFLUENTPROGENYPROOF: str = "Ultimate Affluent Progeny Proof"
##ULTIMATECLAIRVOYANTPROOF: str = "Ultimate Clairvoyant Proof"
##ULTIMATEDETECTIVEPROOF: str = "Ultimate Detective Proof"
##ULTIMATESWIMMINGPROPROOF: str = "Ultimate Swimming Pro Proof"
##ULTIMATEWRITINGPRODIGYPROOF: str = "Ultimate Writing Prodigy Proof"
##ULTIMATEMURDEROUSFIENDPROOF: str = "Ultimate Murderous Fiend Proof"
##ULTIMATE___PROOF: str = "Ultimate ??? Proof"
##ULTIMATEMECHANICPROOF: str = "Ultimate Mechanic Proof"
##ULTIMATEYAKUZAPROOF: str = "Ultimate Yakuza Proof"
##ULTIMATEGYMNASTPROOF: str = "Ultimate Gymnast Proof"
##ULTIMATEPRINCESSPROOF: str = "Ultimate Princess Proof"
##ULTIMATEMAGICIANPROOF: str = "Ultimate Magician Proof"
##ULTIMATECHILDCAREGIVERPROOF: str = "Ultimate Child Caregiver Proof"
##ULTIMATEHOPEPROOF: str = "Ultimate Hope Proof"
##ULTIMATEDESPAIRPROOF: str = "Ultimate Despair Proof"




##crafted_item_requirements: dict[str, list[str]] = \
##{
##    KATANAWORN: [crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.SMALL)],
##    KATANA: [crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.SMALL), crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.NORMAL)],
##    KATANASUPER: [crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.NORMAL), crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.BIG)],
##    KATANAV: [crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.BIG), crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.STURDY)],
##    KATANAEXTREME: [crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.BIG), crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.STURDY)],
##    KATANAEND: [crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.DIVINE), crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.LAVISH)],
##    KATANAV3: [crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.DIVINE), crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.LAVISH), KATANAV],
##
##    GUNWORN: [crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.SMALL)],
##    GUN: [crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.SMALL), crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.NORMAL)],
##    GUNSUPER: [crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.NORMAL), crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.BIG)],
##    GUNV: [crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.BIG), crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.STURDY)],
##    GUNEXTREME: [crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.BIG), crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.STURDY)],
##    GUNEND: [crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.DIVINE), crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.LAVISH)],
##    GUNV3: [crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.DIVINE), crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.LAVISH), GUNV],
##
##    STAFFWORN: [crafting_mat_name(CraftingMaterialType.MONSTERMEAT, CraftingMaterialQuality.SMALL)],
##    STAFF: [crafting_mat_name(CraftingMaterialType.MONSTERMEAT, CraftingMaterialQuality.SMALL), crafting_mat_name(CraftingMaterialType.MONSTERMEAT, CraftingMaterialQuality.NORMAL)],
##    STAFFSUPER: [crafting_mat_name(CraftingMaterialType.MONSTERMEAT, CraftingMaterialQuality.NORMAL), crafting_mat_name(CraftingMaterialType.MONSTERMEAT, CraftingMaterialQuality.BIG)],
##    STAFFV: [crafting_mat_name(CraftingMaterialType.MONSTERMEAT, CraftingMaterialQuality.BIG), crafting_mat_name(CraftingMaterialType.MONSTERMEAT, CraftingMaterialQuality.STURDY)],
##    STAFFEXTREME: [crafting_mat_name(CraftingMaterialType.MONSTERMEAT, CraftingMaterialQuality.BIG), crafting_mat_name(CraftingMaterialType.MONSTERMEAT, CraftingMaterialQuality.STURDY)],
##    STAFFEND: [crafting_mat_name(CraftingMaterialType.MONSTERMEAT, CraftingMaterialQuality.DIVINE), crafting_mat_name(CraftingMaterialType.MONSTERMEAT, CraftingMaterialQuality.LAVISH)],
##    STAFFV3: [crafting_mat_name(CraftingMaterialType.MONSTERMEAT, CraftingMaterialQuality.DIVINE), crafting_mat_name(CraftingMaterialType.MONSTERMEAT, CraftingMaterialQuality.LAVISH), STAFFV],

##    SHIELDWORN: [crafting_mat_name(CraftingMaterialType.MONSTEREYE, CraftingMaterialQuality.SMALL)],
##    SHIELD: [crafting_mat_name(CraftingMaterialType.MONSTEREYE, CraftingMaterialQuality.SMALL), crafting_mat_name(CraftingMaterialType.MONSTEREYE, CraftingMaterialQuality.NORMAL)],
##    SHIELDSUPER: [crafting_mat_name(CraftingMaterialType.MONSTEREYE, CraftingMaterialQuality.NORMAL), crafting_mat_name(CraftingMaterialType.MONSTEREYE, CraftingMaterialQuality.BIG)],
##    SHIELDV: [crafting_mat_name(CraftingMaterialType.MONSTEREYE, CraftingMaterialQuality.BIG), crafting_mat_name(CraftingMaterialType.MONSTEREYE, CraftingMaterialQuality.STURDY)],
##    SHIELDEXTREME: [crafting_mat_name(CraftingMaterialType.MONSTEREYE, CraftingMaterialQuality.BIG), crafting_mat_name(CraftingMaterialType.MONSTEREYE, CraftingMaterialQuality.STURDY)],
##    SHIELDEND: [crafting_mat_name(CraftingMaterialType.MONSTEREYE, CraftingMaterialQuality.DIVINE), crafting_mat_name(CraftingMaterialType.MONSTEREYE, CraftingMaterialQuality.LAVISH)],
##    SHIELDV3: [crafting_mat_name(CraftingMaterialType.MONSTEREYE, CraftingMaterialQuality.DIVINE), crafting_mat_name(CraftingMaterialType.MONSTEREYE, CraftingMaterialQuality.LAVISH), SHIELDV],

##    REPLICASWORD: [crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.COPPER)],
##    KITCHENKNIFE: [crafting_mat_name(CraftingMaterialType.MONSTEREYE, CraftingMaterialQuality.COPPER)],
##    DUMBBELL: [crafting_mat_name(CraftingMaterialType.MONSTERMEAT, CraftingMaterialQuality.COPPER)],
##    JUSTICEHAMMER: [crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.COPPER)],
##    POISON: [crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.COPPER)],
##    IRONSKEWER: [crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.COPPER), crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.COPPER)],
##    METALBAT: [crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.SILVER)],
##    ROPEUSEDFORHANGING: [crafting_mat_name(CraftingMaterialType.MONSTEREYE, CraftingMaterialQuality.SILVER)],
##    HAMMER: [crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.SILVER)],
##    ARMYKNIFE: [crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.GOLD)],
##    SPEARSOFGUNGNIR: [crafting_mat_name(CraftingMaterialType.MONSTEREYE, CraftingMaterialQuality.GOLD)],
##    MONOKUMASPECIALPOISON: [crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.GOLD)],
##    SCISSORS: [crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.GOLD), crafting_mat_name(CraftingMaterialType.MONSTEREYE, CraftingMaterialQuality.GOLD), crafting_mat_name(CraftingMaterialType.MONSTERMEAT, CraftingMaterialQuality.GOLD)],
##    SHOTPUTBALL: [crafting_mat_name(CraftingMaterialType.MONSTERMEAT, CraftingMaterialQuality.SILVER)],
##    PIRANHA: [crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.SILVER)],
##    GOLDLEAFKATANA: [crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.SILVER)],
##    SICKLE: [crafting_mat_name(CraftingMaterialType.MONSTERMEAT, CraftingMaterialQuality.GOLD)],
##    TOILETPAPER: [crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.GOLD)],
##    CROSSBOW: [crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.GOLD)],
##    HYDRAULICPRESS: [crafting_mat_name(CraftingMaterialType.MONSTERMEAT, CraftingMaterialQuality.GOLD), crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.GOLD), crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.GOLD)],
##    HATTATTERED: [crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.SMALL)],
##    HATHIGHSCHOOLER: [crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.SMALL), crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.NORMAL)],
##    HATOVERFLOWINGTALENT: [crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.NORMAL), crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.BIG)],
##    HATULTIMATE: [crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.BIG), crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.STURDY)],
##    HATOFHOPE: [crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.LAVISH)],
##    HATOFLEGEND: [crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.BIG), crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.STURDY), crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.LAVISH)],
##    HATV3: [crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.DIVINE), HATULTIMATE],
##    UNIFORMTATTERED: [crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.SMALL)],
##    UNIFORMHIGHSCHOOLER: [crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.SMALL), crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.NORMAL)],
##    UNIFORMOVERFLOWINGTALENT: [crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.NORMAL), crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.BIG)],
##    UNIFORMULTIMATE: [crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.BIG), crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.STURDY)],
##    UNIFORMOFHOPE: [crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.LAVISH)],
##    UNIFORMOFLEGEND: [crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.BIG), crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.STURDY), crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.LAVISH)],
##    UNIFORMV3: [crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.DIVINE), UNIFORMULTIMATE],
##    SHOESTATTERED: [crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.SMALL)],
##    SHOESHIGHSCHOOLER: [crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.SMALL), crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.NORMAL)],
##    SHOESOVERFLOWINGTALENT: [crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.NORMAL), crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.BIG)],
##    SHOESULTIMATE: [crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.BIG), crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.STURDY)],
##    SHOESOFHOPE: [crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.LAVISH)],
##    SHOESOFLEGEND: [crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.BIG), crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.STURDY), crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.LAVISH)],
##    SHOESV3: [crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.DIVINE), SHOESULTIMATE],
##    TALISMANTATTERED: [crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.SMALL)],
##    TALISMANHIGHSCHOOLER: [crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.SMALL), crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.NORMAL)],
##    TALISMANOVERFLOWINGTALENT: [crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.NORMAL), crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.BIG)],
##    TALISMANULTIMATE: [crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.BIG), crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.STURDY)],
##    TALISMANOFHOPE: [crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.LAVISH)],
##    TALISMANOFLEGEND: [crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.BIG), crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.STURDY), crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.LAVISH)],
##    TALISMANV3: [crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.DIVINE), TALISMANULTIMATE],
##    ULTIMATELUCKYSTUDENTPROOF: [crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.COPPER), crafting_mat_name(CraftingMaterialType.MONSTEREYE, CraftingMaterialQuality.COPPER)],
##    ULTIMATEAFFLUENTPROGENYPROOF: [crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.COPPER), crafting_mat_name(CraftingMaterialType.MONSTERMEAT, CraftingMaterialQuality.COPPER)],


##    ULTIMATECLAIRVOYANTPROOF: [crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.COPPER), crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.COPPER)],
##    ULTIMATEDETECTIVEPROOF: [crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.COPPER), crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.COPPER)],
##    ULTIMATESWIMMINGPROPROOF: [crafting_mat_name(CraftingMaterialType.MONSTEREYE, CraftingMaterialQuality.COPPER), crafting_mat_name(CraftingMaterialType.MONSTERMEAT, CraftingMaterialQuality.COPPER)],
##    ULTIMATEWRITINGPRODIGYPROOF: [crafting_mat_name(CraftingMaterialType.MONSTEREYE, CraftingMaterialQuality.COPPER), crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.COPPER)],
##    ULTIMATEMURDEROUSFIENDPROOF: [crafting_mat_name(CraftingMaterialType.MONSTEREYE, CraftingMaterialQuality.COPPER), crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.COPPER)],
##    ULTIMATE___PROOF: [crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.SILVER), crafting_mat_name(CraftingMaterialType.MONSTEREYE, CraftingMaterialQuality.SILVER)],
##    ULTIMATEMECHANICPROOF: [crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.SILVER), crafting_mat_name(CraftingMaterialType.MONSTERMEAT, CraftingMaterialQuality.SILVER)],
##    ULTIMATEYAKUZAPROOF: [crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.SILVER), crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.SILVER)],
##    ULTIMATEGYMNASTPROOF: [crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.SILVER), crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.SILVER)],
##    ULTIMATEPRINCESSPROOF: [crafting_mat_name(CraftingMaterialType.MONSTEREYE, CraftingMaterialQuality.SILVER), crafting_mat_name(CraftingMaterialType.MONSTERMEAT, CraftingMaterialQuality.SILVER)],
##    ULTIMATEMAGICIANPROOF: [crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.GOLD), crafting_mat_name(CraftingMaterialType.MONSTEREYE, CraftingMaterialQuality.GOLD)],
##    ULTIMATECHILDCAREGIVERPROOF: [crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.GOLD), crafting_mat_name(CraftingMaterialType.MONSTERMEAT, CraftingMaterialQuality.GOLD)],
##    ULTIMATEHOPEPROOF: [crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.PLATINUM), crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.COPPER), crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.GOLD), crafting_mat_name(CraftingMaterialType.MONSTERFANG, CraftingMaterialQuality.SILVER)],
##    ULTIMATEDESPAIRPROOF: [crafting_mat_name(CraftingMaterialType.MONSTERMEAT, CraftingMaterialQuality.PLATINUM), crafting_mat_name(CraftingMaterialType.MONSTERSKIN, CraftingMaterialQuality.PLATINUM), crafting_mat_name(CraftingMaterialType.MONSTERFUR, CraftingMaterialQuality.PLATINUM)],
##}






##ALMIGHTYJABBERWOCKBOSS: str = "the Almighty Jabberwock"
##MONOKUMASECTBOSS: str = "the Monokumasect"
##EXISALBLUEBOSS: str = "the Exisal Blue"
##MONOKUMATANKBOSS: str = "the Monokuma Tank"
##MONOKUMABOSSBOSS: str = "the Monokuma Boss"
##MONDUBABOSS: str = "the Mon'Duba"
##MONOKOPPABOSS: str = "the Monokoppa"
##MONOKIDSHOPEBOSS: str = "Monokid's Hope"
##MONOTAROSHOPEBOSS: str = "Monotaro's Hope"
##MONOSUKESHOPEBOSS: str = "Monosuke's Hope"
##MONODAMSHOPEBOSS: str = "Monodam's Hope"
##MONOPHANIESHOPBOSS: str = "Monophanie's Hope"
##ARENAOFDESPAIRBOSS: str = "Arena of Despair"






