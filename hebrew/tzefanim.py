from enum import Enum
from typing import Dict


class Tzefanim(Enum):
    """
    Tzefanim supported in this library.
    """
    TZOFEN_ATBASH = "tzofen_atbash"
    TZOFEN_ALBAM = "tzofen_albam"
    TZOFEN_AVGAD = "tzofen_avgad"


"""
A dictionary of values with each letter of the alphabet as a key, and the alphabetical value used in the tzofen_atbash
tzefanim method as its value.
"""
TZOFEN_ATBASH: Dict[str, str] = {
    "א": "ת",
    "ב": "ש",
    "ג": "ר",
    "ד": "ק",
    "ה": "צ",
    "ו": "פ",
    "ז": "ע",
    "ח": "ס",
    "ט": "נ",
    "י": "מ",
    "כ": "ל",
    "ך": "ל",
    "ל": "כ",
    "מ": "י",
    "ם": "י",
    "נ": "ט",
    "ן": "ט",
    "ס": "ח",
    "ע": "ז",
    "פ": "ו",
    "ף": "ו",
    "צ": "ה",
    "ץ": "ה",
    "ק": "ד",
    "ר": "ג",
    "ש": "ב",
    "ת": "א",
}

"""
A dictionary of values with each letter of the alphabet as a key, and the alphabetical value used in the tzofen_albam
tzefanim method as its value.
"""
TZOFEN_ALBAM: Dict[str, str] = {
    "א": "ל",
    "ב": "מ",
    "ג": "נ",
    "ד": "ס",
    "ה": "ע",
    "ו": "פ",
    "ז": "צ",
    "ח": "ק",
    "ט": "ר",
    "י": "ש",
    "כ": "ת",
    "ך": "ת",
    "ל": "א",
    "מ": "ב",
    "ם": "ב",
    "נ": "ג",
    "ן": "ג",
    "ס": "ד",
    "ע": "ה",
    "פ": "ו",
    "ף": "ו",
    "צ": "ז",
    "ץ": "ז",
    "ק": "ח",
    "ר": "ט",
    "ש": "י",
    "ת": "כ",
}

"""
A dictionary of values with each letter of the alphabet as a key, and the alphabetical value used in the tzofen_avgad
tzefanim method as its value.
"""
TZOFEN_AVGAD: Dict[str, str] = {
    "א": "ב",
    "ב": "ג",
    "ג": "ד",
    "ד": "ה",
    "ה": "ו",
    "ו": "ז",
    "ז": "ח",
    "ח": "ט",
    "ט": "י",
    "י": "כ",
    "כ": "ל",
    "ך": "ל",
    "ל": "מ",
    "מ": "נ",
    "ם": "נ",
    "נ": "ס",
    "ן": "ס",
    "ס": "ע",
    "ע": "פ",
    "פ": "צ",
    "ף": "צ",
    "צ": "ק",
    "ץ": "ק",
    "ק": "ר",
    "ר": "ש",
    "ש": "ת",
    "ת": "א",
}
