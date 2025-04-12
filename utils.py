TRANSLATE_TABLE = str.maketrans(
    "áéúíóü",
    "aeuiou"
)

MAX_LETTERS = 10


def is_letter(c: str):
    return (97 <= ord(c) <= 122) or c == "ñ"
