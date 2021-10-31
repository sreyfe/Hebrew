from typing import List, TypeVar

from .grapheme_string import GraphemeString

HebrewStringT = TypeVar("HebrewStringT", bound="HebrewString")


class HebrewString(GraphemeString):
    # Letters of the hebrew alphabet
    ALEPH = "א"
    VET = "ב"
    GIMEL = "ג"
    DALET = "ד"
    HE = "ה"
    VAV = "ו"
    ZAYIN = "ז"
    HET = "ח"
    TET = "ט"
    YOD = "י"
    KAF = "כ"
    FINAL_KAF = "ך"
    LAMED = "ל"
    MEM = "מ"
    FINAL_MEM = "ם"
    NUN = "נ"
    FINAL_NUN = "ן"
    SAMEKH = "ס"
    AYIN = "ע"
    PE = "פ"
    FINAL_PE = "ף"
    TSADI = "צ"
    FINAL_TSADI = "ץ"
    QOF = "ק"
    RESH = "ר"
    SHIN = "ש"
    TAV = "ת"

    # Yiddish specific letters
    DOUBLE_YUD = "ײ"
    DOUBLE_VAV = "װ"
    VAV_YUD = "ױ"

    YIDDISH_LETTERS = [DOUBLE_YUD, DOUBLE_VAV, VAV_YUD]
    HEBREW_LETTERS = [
        ALEPH,
        VET,
        GIMEL,
        DALET,
        HE,
        VAV,
        ZAYIN,
        HET,
        TET,
        YOD,
        KAF,
        FINAL_KAF,
        LAMED,
        MEM,
        FINAL_MEM,
        NUN,
        FINAL_NUN,
        SAMEKH,
        AYIN,
        PE,
        FINAL_PE,
        TSADI,
        FINAL_TSADI,
        QOF,
        RESH,
        SHIN,
        TAV,
    ]
    LETTERS = YIDDISH_LETTERS + HEBREW_LETTERS

    # Niqqudot or Vowel characters
    NIQQUD = ["ׂ", "ׁ", "ּ", "ֻ", "ֹ", "ָ", "ַ", "ֶ", "ֵ", "ִ", "ֳ", "ֲ", "ֱ", "ְ", "ׄ"]
    MAQAF = "־"
    PASEQ = "׀"
    SOF_PASSUK = "׃"
    PUNCTUATION = [
        MAQAF,
        PASEQ,
        SOF_PASSUK,
        "״",
        "׳",
        "ׂ",
        "ֿ",
        "ֽ",
        "֑",
        "֒",
        "֓",
        "֔",
        "֕",
        "֖",
        "֗",
        "֘",
        "֙",
        "֚",
        "֛",
        "֜",
        "֝",
        "֞",
        "֟",
        "֠",
        "֡",
        "֣",
        "֤",
        "֥",
        "֦",
        "֧",
        "֨",
        "֩",
        "֪",
        "֫",
        "֬",
        "֭",
        "֮",
        "֯",
    ]

    def __init__(self, string: str):
        super().__init__(string)

    def __str__(self) -> str:
        return self.string

    def __repr__(self) -> str:
        return self.__str__()

    def no_maqaf(self) -> HebrewStringT:
        """
        Replaces all maqafs with spaces.

        This is useful for splitting a string into words when you want words connected by maqafs to be considered as one word.
        Example: You may think of "עַל־פְּנֵ֥י" as one word in some cases but want to split it into "עַל" and "פְּנֵי" in other cases.

        :return:
        """
        return HebrewString(self.string.replace(self.MAQAF, " "))

    def no_sof_passuk(self) -> HebrewStringT:
        """
        Removes all sof_passuk chars.

        :return:
        """
        return HebrewString(self.string.replace(self.SOF_PASSUK, ""))

    def words(self, split_maqaf: bool = False) -> List[HebrewStringT]:
        """
        Splits the string into a list of words.

        :param split_maqaf: Whether to split a single word such as "עַל־פְּנֵ֥י" into "עַל" and "פְּנֵי" when a maqaf is encountered.
        :return:
        """
        string = self.string if not split_maqaf else self.no_maqaf().string
        return [HebrewString(s) for s in string.split()]

    def text_only(self, remove_maqaf: bool = False) -> HebrewStringT:
        """
        Returns a string with all non-letter characters removed.
        This will remove both niqqud and punctuation.

        :param remove_maqaf: Wheather to remove the maqaf characters if they are encountered
        :return:
        """
        string = self.no_maqaf().string if remove_maqaf else self.string
        chars_to_remove = self.NIQQUD + [
            p for p in self.PUNCTUATION if p not in (self.MAQAF, self.PASEQ)
        ]
        string = string.replace(
            " ׀ ", " "
        )  # Handled separately to avoid double spaces.
        for char in chars_to_remove:
            string = string.replace(char, "")
        return HebrewString(string)

    def no_niqqud(self) -> HebrewStringT:
        """
        Removes all niqqud characters.
        This may be useful to practice reading from the torah.

        :return:
        """
        string = self.string
        for char in self.NIQQUD:
            string = string.replace(char, "")
        return HebrewString(string)

    def no_punctuation(
        self, remove_maqaf: bool = False, remove_sof_passuk: bool = False
    ) -> HebrewStringT:
        """
        Removes all punctuation characters.
        Result is a string with just letters and Nekkudot.

        :param remove_maqaf: Whether to remove the maqaf characters if they are encountered.
        :param remove_sof_passuk: Whether to remove the remove_sof_passuk character if they are encountered.
        :return:
        """
        string = self.no_maqaf().string if remove_maqaf else self.string
        string = (
            HebrewString(string).no_sof_passuk().string if remove_sof_passuk else string
        )
        chars_to_remove = [
            p
            for p in self.PUNCTUATION
            if p not in (self.MAQAF, self.PASEQ, self.SOF_PASSUK)
        ]
        string = string.replace(
            " ׀ ", " "
        )  # Handled separately to avoid double spaces.
        for char in chars_to_remove:
            string = string.replace(char, "")
        return HebrewString(string)